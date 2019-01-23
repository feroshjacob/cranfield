package edu.kennesaw.cs.readers;

import com.google.gson.annotations.SerializedName;

/**
 * Created by Ferosh Jacob Date: 01/23/19 KSU: CS 7263 Text Mining
 */
public class Query {
    @SerializedName("query number")
    private int id;
    private String query;

    public int getId() {
        return id;
    }

    public String getQuery() {
        return query;
    }
}
