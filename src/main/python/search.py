from readers import read_queries, read_documents
import math


# ToDo
# 1. Stemming (Porter)
# 2. Stop Words
# 3. Rewrite IDF and Cos

inverted_index = {}


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

# def tf(freq):
#     return 1 + math.log(float(freq))
#
# def idf(freq):
#     return math.log((max-1) / float(freq))

# def rank_postings(query):
#     query_word_count = {}
#     query_word_count[query[0]] = 1
#     query_word_unique = [query[0]]
#
#     for i in range(1, len(query)):
#         if query[i] in query_word_count:
#             query_word_count[query[i]] += 1
#         else:
#             query_word_count[query[i]] = 1
#             query_word_unique.append(query[i])
#
#     scores = [0] * max
#     length = [0] * max
#     query_length = 0
#
#     for i in range(len(query_word_unique)):
#         token = query_word_unique[i]
#         id_list = inverted_index[token]
#         list_length = len(id_list)
#
#         idf_val = idf(list_length)
#         vec_query = tf(query_word_count[token]) * idf_val
#         query_length += vec_query**2
#
#         for tup in id_list:
#             doc_id = tup[0]
            # doc_freq = tup[1]
            # # Print this
            # vec_doc = tf(doc_freq)
#
#             length[doc_id] += vec_doc**2
#             scores[doc_id] += vec_doc * vec_query
#
#     ranking = []
#     for i in range(0, len(scores)):
#         if scores[i] > 0:
#             cos_score = scores[i] / ((query_length*0.5) * (length[i]**0.5))
#         else:
#             cos_score = scores[i]
#         ranking.append((i, cos_score))
#     ranking.sort(key=lambda tup: tup[1], reverse=True)
#
#     return [pos[0] for pos in ranking]

def merge_postings(indexed_tokens):
    first_list = inverted_index[indexed_tokens[0]]
    second_list = []
    for each in range(1, len(indexed_tokens)):
        second_list = inverted_index[indexed_tokens[each]]
        first_list = merge_two_postings(first_list, second_list)
    return first_list


def search_query(query):
    tokens = tokenize(str(query['query']))
    indexed_tokens = remove_not_indexed_toknes(tokens)
    if len(indexed_tokens) == 0:
        return []
    elif len(indexed_tokens) == 1:
        return inverted_index[indexed_tokens[0]]
    else:
        # return rank_postings(indexed_tokens)
        return merge_postings(indexed_tokens)


def tokenize(text):
    return text.split(" ")


def add_token_to_index(token, doc_id):
    if token in inverted_index:
        current_postings = inverted_index[token]

    #     insert = False
    #     for i in range(0, len(current_postings)):
    #         if doc_id == current_postings[i][0]:
    #             current_postings[i][1] += 1
    #             insert = True
    #     if insert == False:
    #         current_postings.append([doc_id, 1])
    #         current_postings.sort(key=lambda tup: tup[1])
    # else:
    #     inverted_index[token] = [[doc_id, 1]]

        current_postings.append(doc_id)
        inverted_index[token] = current_postings
    else:
        inverted_index[token] = [doc_id]


def add_to_index(document):

    # Extending the search to the body.
    docId = document['id']
    documentText = document['title']
    tokens = tokenize(documentText)

    body = tokenize(document['body'])

    tokens.extend(body)

    global max
    max += 1
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
        print "Query:{} and Results:{}".format(query, documents)
