import java.io.*;
import java.util.*;
import java.io.BufferedReader;


public class FileReaderInts {

    public ArrayList<Integer> readIntegersFromFile(String filePath) {
        ArrayList<Integer> numbers = new ArrayList<>();

        try {
            BufferedReader reader = new BufferedReader(new FileReader(filePath));
            String line;

            while ((line = reader.readLine()) != null) {
                numbers.add(Integer.parseInt(line.trim()));
            }

            reader.close();

        } catch (IOException e) {
            System.err.println("An error occurred while reading the file: " + e.getMessage());
        }

        return numbers;
    }
}
