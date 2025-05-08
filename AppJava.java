
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AppJava {
    public static void main(String[] args) throws IOException {

        int LOOP_ITERATIONS = (int) Math.pow(10,6);
        int OUTPUT_WRITES = 1000;
        File outputSort = new File("data/outJava/data1_sort_out.txt");
        File outputEmptyLoop = new File("data/outJava/data1_emptyLoop_out.txt");
        File outputArethmic = new File("data/outJava/data1_arethmic_out.txt");
        File input = new File("data/in/data1.txt");
        double time;

        time = testEmptyLoop(outputEmptyLoop, LOOP_ITERATIONS, OUTPUT_WRITES) / 1e9;

        System.out.println("Test: Empty Loop " + time + " seconds");
        
        time = testArithmicLoop(outputArethmic, LOOP_ITERATIONS, OUTPUT_WRITES) / 1e9;
       
        System.out.println("Test: Arithmic Loop " + time + " seconds");

        time = testSort(input, outputSort, OUTPUT_WRITES) / 1e9;

        System.out.println("Test: Sort " + time + " seconds");
    }
    @SuppressWarnings("ConvertToTryWithResources")
    public static long testEmptyLoop(File output, int loopIterations, int n) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(output, false));
        long timeSum = 0;    
        for(int j = 0; j < n; j++) {
            long time = System.nanoTime();
            for(int i = 0; i < loopIterations; i++) {
                // Do nothing
            }
            time = (System.nanoTime() - time);
            timeSum += time;
            writer.write(time + "\n");
        }
        writer.close();
        return timeSum;
    }
    
    @SuppressWarnings("ConvertToTryWithResources")
    public static long testArithmicLoop(File output, int loopIterations, int n) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(output, false));
        long timeSum = 0;
        for(int j = 0; j < n; j++) {
            long time = System.nanoTime();
            int sum = 0;
            for(int i = 0; i < loopIterations; i++) {
                sum += i;
            }
            time = (System.nanoTime() - time);
            timeSum += time;
            writer.write(time + "\n");
        }
        writer.close();
       
        return timeSum;
    }
    @SuppressWarnings("ConvertToTryWithResources")
    public static long  testSort(File input, File output, int n) throws FileNotFoundException, IOException {
        Scanner scanner = new Scanner(input);
        BufferedWriter writer = new BufferedWriter(new FileWriter(output, false));
        List<Integer> list = new ArrayList<>();
    

        while (scanner.hasNextInt()) {
            list.add(scanner.nextInt());
        }
        long timeSum = 0;
        for(int i = 0; i < n; i++) {
            List<Integer> sortedList = new ArrayList<>(list);
            long startTime = System.nanoTime();
            sortedList.sort(null);
            long endTime = System.nanoTime();
            long time = (endTime - startTime);
            timeSum += time;
            writer.write(time + "\n");
        }
        scanner.close();
        writer.close();
        return timeSum;
    }

}
