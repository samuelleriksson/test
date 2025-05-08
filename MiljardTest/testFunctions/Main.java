import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        int iterationNbr = 1000000000;
        Iteration runTime = new Iteration();
        FileReaderInts prep = new FileReaderInts();
        ArrayList<Integer> l = prep.readIntegersFromFile("/home/christiant14/LTH/UAPprojekt/MiljardTest/dataInAndOut/dataIn/RandomInts.txt");
   
        long r1 = runTime.iteration(iterationNbr);
        long r2 = runTime.arithmetic(iterationNbr);
        long r3 = runTime.timsort(l);
        System.out.println("Iteration: " + r1);
        System.out.println("Arithmetic: " + r2);
        System.out.println("Timsort: " + r3);

    }
}