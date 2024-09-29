import java.util.*;

public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;
    public static final int MAX_N = 100000;

    public static int[] arr = new int[MAX_N + 1];
    public static int n, s;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        s = sc.nextInt();
        for(int i = 1; i <= n; i++)
            arr[i] = sc.nextInt();

        int j = 0, pSum = 0, ans = INT_MAX;
        for(int i = 1; i <= n; i++) {
            while(j + 1 <= n && pSum < s) {
                pSum += arr[j + 1];
                j++;
            }

            if (pSum < s) continue;


            ans = Math.min(ans, j - i + 1);
            pSum -= arr[i];
        }

        System.out.print(ans);
    }
}