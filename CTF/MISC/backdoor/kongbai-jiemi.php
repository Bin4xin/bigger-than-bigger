<?php
$cache="";
for($i=0;$i<strlen($cache);$i++){
    $out.=chr(bindec(str_replace(array(chr(9),chr(32)),array('1','0'),substr($cache,$i,8))));
    $i+= 7;
  }
echo $out."\n";
#echo $out;

#file_put_contents('tmp2.txt',base64_decode($out));

?>