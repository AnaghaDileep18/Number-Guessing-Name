import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Encryption_Decryption {

    public static void encrypt(int key) {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.showOpenDialog(null);
        File file = fileChooser.getSelectedFile();

        //FileInputStream

        try{
            FileInputStream fis = new FileInputStream(file);
            byte[] data = new byte[fis.available()];
            fis.read(data);
            int i = 0;
            for(byte b:data){
                System.out.println(b);
                data[i] = (byte)(b^key);
                i++;
            }
            FileOutputStream fos = new FileOutputStream(file);
            fos.write(data);
            fos.close();
            fis.close();
            JOptionPane.showMessageDialog(null,"Encryption successful");


        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
    public static  void decrypt(int key){

        JFileChooser fileChooser = new JFileChooser();
        fileChooser.showOpenDialog(null);
        File file2 = fileChooser.getSelectedFile();

        //FileInputStream

        try{
            FileInputStream fis2 = new FileInputStream(file2);
            byte[] data = new byte[fis2.available()];
            fis2.read(data);
            int i = 0;
            for(byte by:data){
                System.out.println(by);
                data[i] = (byte)(by^key);
                i++;
            }
            FileOutputStream fos2 = new FileOutputStream(file2);
            fos2.write(data);
            fos2.close();
            fis2.close();
            JOptionPane.showMessageDialog(null,"Decryption successful");


        }
        catch (Exception e){
            e.printStackTrace();
        }

    }
    public static void main(String[] args) {
        System.out.println("This is testing");

        JFrame f = new JFrame();
        f.setTitle("File Encryption and Decryption");
        f.setSize(400,400);
        f.setLocationRelativeTo(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Font font = new Font("Times new roman",Font.BOLD,25);

        //create button
        JButton button = new JButton();
        button.setText("Encrypt File");
        button.setFont(font);
        JButton button2 = new JButton();
        button2.setText("Decrypt File");
        button2.setFont(font);

        //Creating Text Field

        JTextField textField = new JTextField(10);
        textField.setFont(font);

        JTextField textField2 = new JTextField(10);
        textField2.setFont(font);
        //Using lambda function to call the action listner interface
        button.addActionListener(e->{
            System.out.println("button clicked");
            String text=textField.getText();
            int temp=Integer.parseInt(text);
            encrypt(temp);
        });
        button2.addActionListener(e->{
            System.out.println("button clicked");
            String text2=textField2.getText();
            int temp2=Integer.parseInt(text2);
            decrypt(temp2);
        });

        f.setLayout(new FlowLayout());
        f.add(button);
        f.add(textField);
        f.add(button2);
        f.add(textField2);

        f.setVisible(true);
    }
}
