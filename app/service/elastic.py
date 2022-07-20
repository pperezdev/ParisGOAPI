from elasticsearch import Elasticsearch
es = Elasticsearch("http://elasticsearch:9200")

def get_autocompletion(text: str):

    elastic_query = {
        "_source": ["Geometry X Y", "Geometry", "L_ADR"],
        "query": {
            "match": {
            "L_ADR": str(text)
            }
        }
    }
    print(elastic_query)
    reponse = es.search(
        index="adresse", 
        body=elastic_query
    )
    
    return reponse["hits"]["hits"]