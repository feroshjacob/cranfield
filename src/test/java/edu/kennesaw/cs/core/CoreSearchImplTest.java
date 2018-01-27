package edu.kennesaw.cs.core;

import edu.kennesaw.cs.readers.Document;
import edu.kennesaw.cs.readers.Query;
import edu.kennesaw.cs.readers.ReadCranfieldData;

import java.util.List;

public class CoreSearchImplTest {

    public static void main(String[] args) {
        CoreSearch coreSearch = new CoreSearchImpl();
        coreSearch.init();
        for(Document document:ReadCranfieldData.readDocuments()){
            coreSearch.addToIndex(document);
        }
        for(Query query: ReadCranfieldData.readQueries()) {
           List<Integer> docs=  coreSearch.search(query.getQuery());
           if(docs.size() >0) {
               System.out.print(query.getId()+") "+ query.getQuery() +"-> ");
               for(Integer doc: docs) {
                   System.out.print(doc+" ");
               }
               System.out.println();
           }
        }
    }
}
