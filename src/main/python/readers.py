import json


def read_documents():
    return json.load(open('../resources/cranfield_data.json'))


def read_queries():
    return json.load(open('../resources/cran.qry.json'))


def read_relevance():
    return json.load(open('../resources/cranqrel.json'))
