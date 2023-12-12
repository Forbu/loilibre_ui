"""
Main script that show the main UI

The UI is composed of :

- The actual chatbot (RAG currently)

- Metrics around the use of LoiLibre (number of generated tokens etc)

- Description of the method

"""
import streamlit as st

# the UI have a side panel with 3 components :
# - the chatbot
# - the metrics
# - the description of the method

st.sidebar.markdown(
    """
    LoiLibre est un chatbot qui génère des textes juridiques à partir d'une base de données de codes juridiques.
    
    Il s'agit uniquement d'un prototype, et les textes générés ne sont pas à utiliser en l'état.

    Le project est open source, et le code et les datasets sont utilisés pour faire l'applications sont disponibles sur 
    huggingface : https://huggingface.co/datasets/Forbu14/LoiLibre

    Le code de l'UI est disponible sur github :
    https://github.com/Forbu/loilibre_ui

    """)


# add the images and center it from images/logo_v3.png and center it
st.markdown(
    """
    <div style="text-align:center">
    <img src="/workspaces/loilibre_ui/loilibre_ui/images/logo_v3.png" alt="LoiLibre logo" width="200"/>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """

    LoiLibre est un chatbot qui génère des textes juridiques à partir d'une base de données de codes juridiques.
    
    Le project est en phase de construction et n'est pas encore utilisable en production.

    Le project est open source, et le code et les datasets sont utilisés pour faire l'applications sont disponibles sur
    
    Il s'agit aussi de rendre accessible le droit à tous, et de permettre à chacun de comprendre les lois qui régissent notre société.

    "Nul n'est censé ignorer la loi" est un principe fondamental de notre société, et pourtant, il est très difficile de comprendre les lois qui régissent notre société.
    
    Cette initiative a pour but de rendre le droit accessible à tous, et de permettre à chacun de comprendre les lois qui régissent notre société.
    
    Le principal outil de LoiLibre est un chatbot qui permet de répondre à des questions juridiques en se basant sur une base de données de codes juridiques.


    """
)