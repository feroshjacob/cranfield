package edu.kennesaw.cs.core;

import edu.kennesaw.cs.readers.Document;
import edu.kennesaw.cs.readers.Query;
import edu.kennesaw.cs.readers.ReadCranfieldData;
import edu.kennesaw.cs.readers.Relevance;

import java.util.*;


/*
  CHANGE THIS CLASS ONLY IF YOU DECIDE TO CREATE A CoreSearch implementation!
  OTHERS DO NOT MODIFY THIS CLASS
 */
/**
 * Created by Ferosh Jacob
 * Date: 01/27/18
 * KSU: CS 7263 Text Mining
 */
public class EvalSearch {


    private static double log2 = Math.log(2);
    private static Map<String, Integer> relevanceMap = new HashMap<String, Integer>();
    private static Map<Integer, Double> idealScoreMap = new HashMap<Integer, Double>();

    public static void main(String[] args) {
        evalSearch(new CoreSearchImpl());
    }

    private static String createKey(Integer queryId, Integer docId) {
        return queryId + "_" + docId;
    }

    public static void evalSearch(CoreSearch coreSearch) {

        coreSearch.init();
        for (Document document : ReadCranfieldData.readDocuments()) {
            coreSearch.addToIndex(document);
        }


        calculateIdeal();


        List<Double> ndcgs = new ArrayList<Double>();
        List<Query> queries = ReadCranfieldData.readQueries();
        for (Query query : queries) {
            double queryScore = 0.0;
            List<Integer> docs = coreSearch.search(query.getQuery());
            for (int i = 0; i < docs.size(); i++) {
                String key = createKey(query.getId(), docs.get(i));
                if (relevanceMap.containsKey(key)) {
                    queryScore = queryScore + (relevanceMap.get(key) / (Math.log(i + 2) / log2));
                }
            }

            if (idealScoreMap.containsKey(query.getId()) && queryScore != 0.0) {

                double ndcg = queryScore / idealScoreMap.get(query.getId());
                System.out.println(query.getId() + ")" + query.getQuery() + " dcg=" + queryScore + ", ideal=" + idealScoreMap.get(query.getId())
                        + ",ndcg= " + ndcg);
                ndcgs.add(ndcg);
            }
        }

        Double sum = 0.0;
        for (Double ndcg : ndcgs) {
            sum = sum + ndcg;
        }
        System.out.println("Total ndcg score=" + sum/(queries.size()-1) );
    }

    private static void calculateIdeal() {
        Map<Integer, List<Integer>> queryScores = new HashMap<Integer, List<Integer>>();
        for (Relevance relevance : ReadCranfieldData.readRelevance()) {
            relevanceMap.put(createKey(relevance.getQueryID(), relevance.getId()), (5 - relevance.getPosition()));
            if (queryScores.containsKey(relevance.getQueryID())) {
                List<Integer> scores = queryScores.get(relevance.getQueryID());
                scores.add(5 - relevance.getPosition());
                Comparator<Integer> comparator = Collections.reverseOrder();
                Collections.sort(scores, comparator);
            } else {
                List<Integer> scores = new ArrayList<Integer>();
                scores.add(5 - relevance.getPosition());
                queryScores.put(relevance.getQueryID(), scores);
            }
        }

        for (Integer queryId : queryScores.keySet()) {
            List<Integer> currentQueryScore = queryScores.get(queryId);
            double queryScore = 0.0;
            for (int i = 0; i < currentQueryScore.size(); i++) {
                queryScore = queryScore + currentQueryScore.get(i) / (Math.log(i + 2) / log2);
            }

            idealScoreMap.put(queryId, queryScore);
        }
    }

}
