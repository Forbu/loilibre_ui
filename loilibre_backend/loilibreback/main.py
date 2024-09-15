"""
In this module we will define the main endpoints of the API
1. /api/v1/loilibre_rag/THEMESSAGE -> GET -> Return the closest code to the message
and also the chatbot response
Here we will also save the message in the database
And we will also save the response in the database
And we will also count the number of tokens chatbot has used
2. /api/v1/loilibre_token -> GET -> Return the number of tokens chatbot has used
"""

# import the libraries
import pandas as pd
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
import os
from openai import OpenAI

from loilibreback.utils import create_vector_db, query_vector_db

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# first endpoint
# instantiate the app
app = FastAPI()

collection = create_vector_db(
    path_embeddings="/home/data/embedding.parquet",
    path_metadata="/home/data/articles.parquet",
    limit=100
)

model = SentenceTransformer('multi-qa-mpnet-base-dot-v1')

# first endpoint creation
@app.get("/api/v1/loilibre_rag/{message}")
def loilibre_rag(message: str):
    """
    Return the closest code to the message
    and also the chatbot response
    """
    # query the vector db
    document = query_vector_db(collection, message=message, model=model)

    # Prepare the prompt for OpenAI
    prompt = f"""Given the following context and user message, provide a helpful response:

Context: {document}

User message: {message}

Response:"""

    # Call OpenAI API to generate the response
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides information about French law based on the given context."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )

    response = completion.choices[0].message.content.strip()
    
    return {"message": message, "document": document, "response": response}

# second endpoint to get the number of tokens
@app.get("/api/v1/loilibre_token")
def loilibre_token():
    """
    Return the number of tokens chatbot has used
    """
    return {"token": 0}

