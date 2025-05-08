import java.util.ArrayList;

public class Main {
    public static void main(String[] args) { // index 0 = vilken funktion som ska test, måste skickas,

        int iterationNbr = 1000000000;
        Iteration runTime = new Iteration();
        FileReaderInts prep = new FileReaderInts();
        ArrayList<Integer> l = prep.readIntegersFromFile("/home/burk/LTH/UAPprojekt/test/MiljardTest/dataInAndOut/dataIn/RandomInts.txt");

        try {
            int x = Integer.parseInt(args[0]);
            switch (x) {
                case 1 -> {
                    long r1 = runTime.iteration(iterationNbr);
                    prep.writeIntegersToFileAppended("/home/burk/LTH/UAPprojekt/test/MiljardTest/dataInAndOut/dataOut/javaIterationData.txt", r1);

                }

                case 2 -> {
                    long r2 = runTime.arithmetic(iterationNbr);
                    prep.writeIntegersToFileAppended("/home/burk/LTH/UAPprojekt/test/MiljardTest/dataInAndOut/dataOut/javaArithmeticData.txt", r2);

                }
                case 3 -> {
                    long r3 = runTime.timsort(l);
                    prep.writeIntegersToFileAppended("/home/burk/LTH/UAPprojekt/test/MiljardTest/dataInAndOut/dataOut/javaSortData.txt", r3);
                }

                default -> System.out.println("fel val, välj 1 för iteration, 2 för aritmetik, 3 för sort");
            }

        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("fanns ej argument");
        }

    }
}