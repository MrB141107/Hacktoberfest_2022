import java.util.Scanner;

public class Leap_Year_Checker {
    public static void main(String[] args) {

        System.out.print("Enter the year : ");
        Scanner scan = new Scanner(System.in);
        int year = scan.nextInt();

        if( (year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0) ) {
            System.out.println(year + " is a leap year.");
        } else {
            System.out.println(year + " is not a leap year.");
        }
        scan.close();
    }
}
