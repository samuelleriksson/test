
import java.util.ArrayList;

public class Iteration {

    public long result;
    public ArrayList resultlist;

    public long iteration(int n) {
        long t1 = System.nanoTime();
        long dummy = 0; // behövs för att inte JIT helt ska eliminera denna loopen
        for (int i = 0; i < n; i++) {
            dummy++;
        }
        long t2 = (System.nanoTime() - t1);
        result = dummy;
        return t2;
    }

    public long arithmetic(int n) {
        long tot = 0;
        long t1 = System.nanoTime();
        for (int i = 0; i < n; i++) {
            tot += i * 2 / 3;
        }
        long t2 = (System.nanoTime() - t1);
        result = tot; //samma här
        return t2;

    }

    public long timsort(ArrayList<Integer> l) {
        long tot = 0;
        long t1 = System.nanoTime();
        l.sort((a, b) -> a - b);
        long t2 = (System.nanoTime() - t1);
        resultlist = l; //samma här
        return t2;

    }
}
