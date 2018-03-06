from readers import read_queries, read_documents
import math
# from nltk.corpus import stopwords             Decreases the ndcg score.
# from nltk.stem import SnowballStemmer



# ToDo
# 1. Stemming (Porter)
# 2. Stop Words
# 3. Rewrite IDF and Cos

inverted_index = {}
doc_length = {}

# Find the # of documents in the corpus.
max = len(read_documents()) + 1

# Creating a master dictionary to store the docId and IDF value.
masterDictionary = {}

def remove_not_indexed_toknes(tokens):
    return [token for token in tokens if token in inverted_index]


# def merge_two_postings(first, second):
#     first_index = 0
#     second_index = 0
#     merged_list = []
#     while first_index < len(first) and second_index < len(second):
#         if first[first_index] == second[second_index]:
#             merged_list.append(first[first_index])
#             first_index = first_index + 1
#             second_index = second_index + 1
#         elif first[first_index] < second[second_index]:
#             first_index = first_index + 1
#         else:
#             second_index = second_index + 1
#     return merged_list


def ranking(scores, Qlength, length):
    ranking = []
    cos_score = 0
    for i in range(0, len(scores)):
        if scores[i] > 0:
            cos_score = scores[i] / ((Qlength * 0.5) * (length[i] ** 0.5))
        else:
            cos_score = scores[i]
        ranking.append((i, cos_score))

    return ranking

def tf(freq):
    return 1 + math.log(float(freq))

def idf(freq):
    return math.log((max-1) / float(freq))

def calculate_tf_idf(query):
    wordCount = {}
    wordCount[query[0]] = 1
    uniqueWords =  [query[0]]

    for token in query:
        if token in wordCount:
            wordCount[token] += 1
        else:
            wordCount[token] = 1
            uniqueWords.append(token)

    scores = [0] * max
    length = [0] * max
    Qlength = 0

    for token in uniqueWords:
        documents = inverted_index[token]
        noOfDocuments = len(documents)

        vectorQuery = tf(wordCount[token]) * idf(noOfDocuments)
        Qlength += vectorQuery**2

        for document in documents:
            docId = document[0]
            # print(docId)
            freq = document[1]
            # print(freq)
            vectorDocument = tf(freq)
            # vectorDocument = tf(freq) * idf(freq)
            length[docId] += vectorDocument**2
            scores[docId] += vectorDocument * vectorQuery

    rankings = []
    rankings = ranking(scores, Qlength, length)

    rankings.sort(key=lambda tup: tup[1], reverse=True)
    return [i[0] for i in rankings]

# def merge_postings(indexed_tokens):
#     first_list = inverted_index[indexed_tokens[0]]
#     second_list = []
#     for each in range(1, len(indexed_tokens)):
#         second_list = inverted_index[indexed_tokens[each]]
#         first_list = merge_two_postings(first_list, second_list)
#     return first_list


def search_query(query):
    tokens = tokenize(str(query['query']))
    indexed_tokens = remove_not_indexed_toknes(tokens)
    if len(indexed_tokens) == 0:
        return []
    elif len(indexed_tokens) == 1:
        return inverted_index[indexed_tokens[0]]
    else:
        # return rank_postings(indexed_tokens)
        return calculate_tf_idf(indexed_tokens)

# Takes the ncdg score from 0.59 to 0.61
def specialChars(tokens):
    str = []
    for token in tokens:
        str.append(''.join(e for e in token if e.isalnum()))        # https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
    return str

# Takes the ndcg score from 0.61 to 0.63
# def stop(tokens):
#     stop_words = set(stopwords.words('english'))
#     str = []
#     for token in tokens:
#         if token not in stop_words:
#             str.append(token)
#     return str

# def stemming(tokens):
#     str= []
#     stemmer = SnowballStemmer("english", ignore_stopwords=True)                #www.nltk.org/howto/stem.html
#     for token in tokens:
#         str.append(stemmer.stem(token))
#     return str

def tokenize(text):
    str = []
    str = text.split(" ")
    str = specialChars(str)
    # str =  stop(str)
    # str = stemming(str)
    return str


def add_token_to_index(token, doc_id):
    if token in inverted_index:
        current_postings = inverted_index[token]
        insert = False
        for i in range(0, len(current_postings)):
            if doc_id == current_postings[i][0]:
                current_postings[i][1] += 1
                insert = True
        if (insert == False):
            current_postings.append([doc_id, 1])
            current_postings.sort(key=lambda tup: tup[1])
    else:
        inverted_index[token] = [[doc_id, 1]]


def add_to_index(document):
    # Extending the search to the body.
    docId = document['id']
    tokens = tokenize(document['title'])
    body = tokenize(document['body'])
    tokens.extend(body)

    for token in tokens:
        add_token_to_index(token, docId)

def create_index():
    for document in read_documents():
        add_to_index(document)

    # print "Created index with size {}".format(len(inverted_index))


create_index()

if __name__ == '__main__':
    all_queries = [query for query in read_queries() if query['query number'] != 0]
    for query in all_queries:
        documents = search_query(query)
        # print ("Query:{} and Results:{}", format(query, documents))
