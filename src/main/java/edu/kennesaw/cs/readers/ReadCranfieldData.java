package edu.kennesaw.cs.readers;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Type;
import java.util.List;

/**
 * Created by Ferosh Jacob
 * Date: 01/27/18
 * KSU: CS 7263 Text Mining
 */
public class ReadCranfieldData {

    private static InputStream loadResource(String fileName) {
        return ReadCranfieldData.class.getResourceAsStream(fileName);
    }


    public static List<Document> readDocuments() {

        Gson gson = new Gson();
        BufferedReader br = new BufferedReader(new InputStreamReader(loadResource("/cranfield_data.json")));
        Type type = new TypeToken<List<Document>>() {
        }.getType();
        return gson.fromJson(br, type);
    }

    public static List<Query> readQueries() {

        Gson gson = new Gson();
        BufferedReader br = new BufferedReader(new InputStreamReader(loadResource("/cran.qry.json")));
        Type type = new TypeToken<List<Query>>() {
        }.getType();
        return gson.fromJson(br, type);
    }

    public static List<Relevance> readRelevance() {

        Gson gson = new Gson();
        BufferedReader br = new BufferedReader(new InputStreamReader(loadResource("/cranqrel.json")));
        Type type = new TypeToken<List<Relevance>>() {
        }.getType();
        return gson.fromJson(br, type);
    }
}

