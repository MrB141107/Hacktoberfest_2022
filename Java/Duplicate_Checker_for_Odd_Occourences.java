import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

/* If you have a list which has a single element which occours odd number of times. This program will find it without any extra memory space
    It does the work by taking XOR of the whole list  and the result is the element which occours odd number of times
*/
public class Duplicate_Checker_for_Odd_Occourences {
    private static List<Integer> l1 = new LinkedList<>();

    public static void main(String[] args) {
        Input_taker();
        System.out.println("Duplicate: " + check_duplicate(l1));
    }

    private static Integer check_duplicate(List<Integer> arr) {
        int dup = arr.get(0);
        for (int i = 0; i < arr.size() - 1; i++) {
            dup ^= arr.get(i + 1);
        }
        return dup;
    }

    private static void Input_taker() {
        Scanner sc = new Scanner(System.in);
        Integer tmp, size;
        System.out.println(
                "If you have a list which has a single element which occours odd number of times. This program will find it without any extra memory space");
        System.out.println("====================================================");
        System.out.println("Enter the size of list: ");
        size = sc.nextInt();
        System.out.println("Enter elements in your list.");
        while (l1.size() <= size - 1) {
            tmp = sc.nextInt();
            l1.add(tmp);
        }
        sc.close();
    }
}