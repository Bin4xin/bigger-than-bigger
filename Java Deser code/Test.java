import java.io.*;

public class Test {
    public static void main(String[] args) throws Exception {
        // 初始化对象
        People people = new People();
        people.setName("xiaoming");
        people.setAge(18);


        // 序列化步骤
        // 1. 创建一个ObjectOutputStream输出流
        // 2. 调用ObjectOutputStream对象的writeObject输出可序列化对象
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(new File("./People.txt")));
        oos.writeObject(people);
        System.out.println("people对象序列化成功！");

        // 反序列化步骤
        // 1. 创建一个ObjectInputStream输入流
        // 2. 调用ObjectInputStream对象的readObject()得到序列化的对象
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(new File("./People.txt")));
        People people1 = (People) ois.readObject();
        System.out.println("people对象反序列化成功！");
        System.out.println(people1.getName());
        System.out.println(people1.getAge());
    }
}
