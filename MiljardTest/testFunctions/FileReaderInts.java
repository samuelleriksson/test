import java.io.*;
import java.util.*;

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

    public void writeIntegersToFileAppended(String filePath, long toWrite) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath, true))) {
            writer.write(Long.toString(toWrite));
            writer.newLine(); // Ensures it goes to a new line
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
