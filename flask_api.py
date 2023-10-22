import json
from flask import Flask, jsonify, request
from doc_vec import convert_vec
import pinecone

app = Flask(__name__)

# @app.route('/scorer_endpoint')
def scorer_endpoint():
    f = open("test1.json")
    data = json.load(f)

    query = data["Query"]
    data.pop("Query")
    content = []

    for profile_num in data:
        str__ = ""
        str__ = str__ +"description"
        print(profile_num)
        str__ = str__ + data[profile_num]["Agent`s description"]

        str__ = str__ +"Case History"
        str__ = str__ + data[profile_num]["This agent has the following case histories"]["Case History 1 Title"]

        str__ = str__ +"Case History 1 Description"
        str__ = str__ + data[profile_num]["This agent has the following case histories"]["Case History 1 Description"]
    
        content.append(str__)

    pinecone_key = "42c8108f-1798-4fc2-b43b-320d619c9207"
    pinecone.init(api_key=pinecone_key, environment="northamerica-northeast1-gcp")
    
    
    index = pinecone.Index(index_name = "docscorer")
    print(index.describe_index_stats())
    # for i, st in enumerate(content):
    #     input = convert_vec(st[:511])
    #     print(input[0])
    #     items = [{"id": str(i), "values": input[0].tolist()}]
    #     index.upsert(vectors = items)

    # query = "I am looking for a real estate agent who experience in selling detached home and has listed at least 2 homes in the past 2 years"

    query_embedding = convert_vec(query)[0].tolist()

    results = index.query(
        top_k = 6,
        include_values = True,
        vector = query_embedding
    )
    
    scores = []

    for i in range(6):
        scores.append(results["matches"][i]["score"])

    return scores

if __name__ == "__main__":
    scorer_endpoint()
    # app.run()
    print("running flask_api...")