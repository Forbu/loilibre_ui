"""
Module for utility functions

1. Create the vector db from the data
2. make a query to the vector db and return the closest code
"""
import chromadb
import pandas as pd
from tqdm import tqdm


def create_vector_db(path_embeddings, path_metadata, limit=None):
    """
    Create the vector db from the data
    """
    data_embeddings = pd.read_parquet(path_embeddings)
    data_metadata = pd.read_parquet(path_metadata)

    if limit is not None:
        data_embeddings = data_embeddings.iloc[:limit]
        data_metadata = data_metadata.iloc[:limit]

    # create the vector db
    vector_db = chromadb.Client()

    # we create the collection
    collection = vector_db.create_collection(
        name="loilibre", metadata={"hnsw:space": "cosine"}
    )

    # add the data to the vector db
    for i in tqdm(range(len(data_embeddings))):
        # embedding
        embedding = list(data_embeddings.iloc[i]["embedding"])

        # convert every element to float
        embedding = [float(x) for x in embedding]

        # text
        text = data_metadata.iloc[i]["text"]

        # metadata
        metadata = data_metadata.iloc[i][
            [
                "title_parent",
                "cid",
                "date",
                "etat",
                "id",
                "intOrdre",
                "modId",
                "modTitle",
                "num",
                "file_name",
            ]
        ]

        # add the embedding to the collection
        collection.add(
            embeddings=[embedding],
            metadatas=[{"source": metadata["file_name"]}],
            documents=[text],
            ids=[str(i)],
        )

    return collection


def query_vector_db(collection, message, n_results=10, model=None):
    """
    make a query to the vector db and return the closest code
    """
    # get the embedding of the message
    embedding = list(model.encode(message))

    # convert every element to float
    embedding = [float(x) for x in embedding]

    # query the vector db
    query = collection.query(query_embeddings=[embedding], n_results=n_results)

    return query
