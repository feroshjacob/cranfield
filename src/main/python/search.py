from readers import read_queries, read_documents

inverted_index = {}


def remove_not_indexed_toknes(tokens):
    return [token for token in tokens if token in inverted_index]


def merge_two_postings(first, second):
    first_index = 0
    second_index = 0
    merged_list = []
    while first_index < len(first) and second_index < len(second):
        if first[first_index] == second[second_index]:
            merged_list.append(first[first_index])
            first_index = first_index + 1
            second_index = second_index + 1
        elif first[first_index] < second[second_index]:
            first_index = first_index + 1
        else:
            second_index = second_index + 1
    return merged_list


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
        return merge_postings(indexed_tokens)


def tokenize(text):
    return text.split(" ")


def add_token_to_index(token, doc_id):
    if token in inverted_index:
        current_postings = inverted_index[token]
        current_postings.append(doc_id)
        inverted_index[token] = current_postings
    else:
        inverted_index[token] = [doc_id]


def add_to_index(document):
    for token in tokenize(document['title']):
        add_token_to_index(token, document['id'])


def create_index():
    for document in read_documents():
        add_to_index(document)
    print "Created index with size {}".format(len(inverted_index))


create_index()

if __name__ == '__main__':
    all_queries = [query for query in read_queries() if query['query number'] != 0]
    for query in all_queries:
        documents = search_query(query)
        print "Query:{} and Results:{}".format(query, documents)
