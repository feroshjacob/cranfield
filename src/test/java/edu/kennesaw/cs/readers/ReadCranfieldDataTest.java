package edu.kennesaw.cs.readers;

public class ReadCranfieldDataTest {


    public static void main(String[] args){
       System.out.println(  ReadCranfieldData.readQueries().size());
        System.out.println( ReadCranfieldData.readDocuments().size());
        System.out.println( ReadCranfieldData.readRelevance().size());
    }
}
