import java.util.Scanner;
public class Login 
{
    public static void main(String args[])
    {
        String username, password;
        Scanner s = new Scanner(System.in);
        System.out.print("Enter username:");//username:user
        username = s.nextLine();
        System.out.print("Enter password:");//password:user
        password = s.nextLine();
        if(username.equals("user") && password.equals("user"))
        {
            System.out.println("Welcome");
        }
        else
        {
            System.out.println("Username Or Password wrong");
        }
    }
}