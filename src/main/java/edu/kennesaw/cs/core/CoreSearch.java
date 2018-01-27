package edu.kennesaw.cs.core;

import edu.kennesaw.cs.readers.Document;
import java.util.List;


/**
 * Created by Ferosh Jacob
 * Date: 01/27/18
 * KSU: CS 7263 Text Mining
 */
public interface CoreSearch {


    /*
    Core method to implement search
     */
    void init();

    /*
     Add to Index method
     */
    void addToIndex(Document document);

    /*
      The search implementation

     */
    List<Integer> search(String query);

}
