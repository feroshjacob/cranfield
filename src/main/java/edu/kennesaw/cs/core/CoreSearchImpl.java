package edu.kennesaw.cs.core;

import edu.kennesaw.cs.readers.Document;

import java.util.*;

/*
This class is an example implementation of the CoreSearch, you can either modify or write another implementation of the Core Search.
 */

/**
 * Created by Ferosh Jacob
 * Date: 01/27/18
 * KSU: CS 7263 Text Mining
 */
public class CoreSearchImpl implements CoreSearch {


    Map<String, List<Integer>> invertedIndex = new HashMap<String, List<Integer>>();

    public void init() {

    }

    /*
    A very simple tokenization.
     */
    public String[] tokenize(String title) {
        return title.split(" ");
    }

    public void addToIndex(Document document) {

        String[] tokens = tokenize(document.getTitle());
        for (String token : tokens) {
            addTokenToIndex(token, document.getId());
        }

    }

    private void addTokenToIndex(String token, int docId) {

        if (invertedIndex.containsKey(token)) {
            List<Integer> docIds = invertedIndex.get(token);
            docIds.add(docId);
            Collections.sort(docIds);
            invertedIndex.put(token, docIds);
        } else {
            List<Integer> docIds = new ArrayList<Integer>();
            docIds.add(docId);
            invertedIndex.put(token, docIds);
        }
    }

    /*
    A very simple search implementation.
     */
    public List<Integer> search(String query) {
        String[] queryTokens = removeNotIndexTokens(query.split(" "));
        List<Integer> mergedDocIds = new ArrayList<Integer>();
        if (queryTokens.length == 0) return mergedDocIds;
        int index = 1;
        if (queryTokens.length == 1)
            invertedIndex.get(queryTokens[0]);

        List<Integer> initial = invertedIndex.get(queryTokens[0]);
        while (index < queryTokens.length) {
            initial = mergeTwoDocIds(initial, invertedIndex.get(queryTokens[index]));
            index++;
        }

        return initial;
    }

    /*
    Ignore terms in query that are not in Index
     */
    private String[] removeNotIndexTokens(String[] split) {
        List<String> indexedTokens = new ArrayList<String>();
        for (String token : split) {
            if (invertedIndex.containsKey(token)) indexedTokens.add(token);
        }
        return indexedTokens.toArray(new String[indexedTokens.size()]);
    }


    /*
    AND Merging postings!!
     */
    public List<Integer> mergeTwoDocIds(List<Integer> docList1, List<Integer> docList2) {
        int docIndex1 = 0;
        int docIndex2 = 0;
        List<Integer> mergedList = new ArrayList<Integer>();
        while (docIndex1 < docList1.size() && docIndex2 < docList2.size()) {
            if (docList1.get(docIndex1).intValue() == docList2.get(docIndex2).intValue()) {
                mergedList.add(docList1.get(docIndex1));
                docIndex1++;
                docIndex2++;
            } else if (docList1.get(docIndex1) < docList2.get(docIndex2)) {
                docIndex1++;
            } else if (docList1.get(docIndex1) > docList2.get(docIndex2)) {
                docIndex2++;
            }
        }

        return mergedList;
    }
}
