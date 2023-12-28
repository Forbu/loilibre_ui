"""
Testing module for the utils module
"""

import pytest

from loilibreback.utils import create_vector_db, query_vector_db


def test_create_vector_db():
    """
    Test the create_vector_db function
    """
    # create the vector db
    collection = create_vector_db(
        path_embeddings="/home/data/embedding.parquet",
        path_metadata="/home/data/articles.parquet"
    )

    print(collection)
    
def test_query_vector_db():
    """
    Test the query_vector_db function
    """
    # create the vector db
    collection = create_vector_db(
        path_embeddings="/home/data/embedding.parquet",
        path_metadata="/home/data/articles.parquet",
        limit=100
    )
    
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer('multi-qa-mpnet-base-dot-v1')

    # query the vector db
    query = query_vector_db(collection, message="bonjour", model=model)

    print(query)
    
if __name__ == "__main__":
    #test_create_vector_db()
    test_query_vector_db()