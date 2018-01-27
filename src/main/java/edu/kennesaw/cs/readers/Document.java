package edu.kennesaw.cs.readers;

/**
 * Created by Ferosh Jacob
 * Date: 01/27/18
 * KSU: CS 7263 Text Mining
 */
public class Document {

    private int id;
    private String author;
    private String bibliography;
    private String title;
    private String body;

    public int getId() {
        return id;
    }

    public String getAuthor() {
        return author;
    }

    public String getBibliography() {
        return bibliography;
    }

    public String getTitle() {
        return title;
    }

    public String getBody() {
        return body;
    }
}
