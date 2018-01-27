package edu.kennesaw.cs.readers;

import com.google.gson.annotations.SerializedName;
/**
 * Created by Ferosh Jacob
 * Date: 01/27/18
 * KSU: CS 7263 Text Mining
 */
public class Relevance {
    @SerializedName("query_num")
    private int queryID;
    private int position;
    private int id;

    public int getQueryID() {
        return queryID;
    }

    public int getPosition() {
        return position;
    }

    public int getId() {
        return id;
    }

}
