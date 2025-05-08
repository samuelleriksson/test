import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        int iterationNbr = 1000000000;
        Iteration runTime = new Iteration();
        FileReaderInts prep = new FileReaderInts();
        ArrayList<Integer> l = prep.readIntegersFromFile("dataInAndOut/dataIn/RandomInts.txt");
   
        long r1 = runTime.iteration(iterationNbr);
        long r2 = runTime.arithmetic(iterationNbr);
        long r3 = runTime.timsort(l);
        System.out.println(r1);
        System.out.println(r2);
        System.out.println(r3);
        prep.writeIntegersToFileAppended("dataInAndOut/dataOut/javaIterationData.txt", r1);
        prep.writeIntegersToFileAppended("dataInAndOut/dataOut/javaArithmeticData.txt", r2);
        prep.writeIntegersToFileAppended("dataInAndOut/dataOut/javaSortData.txt", r3);
    }
}