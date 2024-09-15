import streamlit as st

# ici on peut décrire l'idée du project : faire un prototype de chatbot qui assiste les juristes et citoyens dans la compréhension du droit
# on peut aussi décrire les datasets utilisés, et les modèles utilisés
# on parle de l'auteur (Adrien Bufort) et on donne son contact

st.title("LoiLibre chat")

# markdown pour décrire le projet
st.markdown(
    """
    Le dataset utilisé (avec les textes de lois) est disponible sur huggingface : https://huggingface.co/datasets/Forbu14/LoiLibre  
    Le code de l'UI est disponible sur github :
        https://github.com/Forbu/loilibre_ui/tree/main

    En ce qui concerne le modèle, il s'agit d'un modèle RAG (Retrieve and Generate) qui permet de générer des textes à partir d'une base de données de textes.
    Le "base modèle" est Mixtral.

    En ce qui concerne l'auteur, il s'agit d'Adrien Bufort (https://www.linkedin.com/in/adrien-bufort-a65901a1/), qui est un simple citoyen dev qui s'intéresse au droit.    

    """)

