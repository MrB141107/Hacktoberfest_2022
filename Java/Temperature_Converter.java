package BaseJava;

import java.util.Scanner;

public class temperaturconver {
    public static void main(String[] args){

        Scanner temp = new Scanner(System.in);
        System.out.println("Enter temperature in C: ");
        float tempC = temp.nextFloat();
        float tempF = (tempC * 9/5) + 32;
        System.out.println("Temperature in Farenhiet: " + tempF);

    }
    
}
