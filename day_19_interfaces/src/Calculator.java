import java.io.*;
import java.util.*;

public class Calculator implements AdvancedArithmetic {
    @Override
    public int divisorSum(int n) {
        int sqrtN = (int) Math.round(Math.sqrt(n));
        int divisorSum = 0;

        for(int i = 1; i < sqrtN; i++) {
            if (n % i == 0) {
                divisorSum += i;
            }
        }

        return divisorSum;
    }
}
