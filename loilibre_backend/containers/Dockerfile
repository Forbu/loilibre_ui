# in this dockerfile we will install the necessary dependencies for the backend
# here we just want to create a fast API server with a RAG functionality :
# basicly the server will take a question and will return an answer
# it will also register the number of times the question was asked and the number of tokens generated
# the server will also be able to return the number of tokens generated
# the server will also be able to return the number of times a question was asked

# we will use the python image as a base image
FROM python:3.8

# we need 
# fastAPI to create the server
# uvicorn to run the server
# transformers to use the RAG model
# torch to use the RAG model
RUN pip install fastapi uvicorn transformers torch chromadb pandas pyarrow sentence_transformers
