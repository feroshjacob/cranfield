package edu.kennesaw.cs.readers;

/**
 * Created by Ferosh Jacob Date: 01/23/19 KSU: CS 7263 Text Mining
 */
public class ReadCranfieldDataTest {

    public static void main(String[] args) {
        System.out.println(ReadCranfieldData.readQueries().size());
        System.out.println(ReadCranfieldData.readDocuments().size());
        System.out.println(ReadCranfieldData.readRelevance().size());
    }
}
