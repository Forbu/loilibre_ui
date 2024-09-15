"""
Main script that shows the main UI

The UI is composed of:
- The actual chatbot (RAG currently)
- Metrics around the use of LoiLibre (number of generated tokens etc)
- Description of the method
"""

import streamlit as st

# Sidebar components
st.sidebar.image("loilibre_ui/images/logo_v3.png", width=300)

st.sidebar.markdown("""
    LoiLibre est un chatbot qui génère des textes juridiques à partir d'une base de données de codes juridiques.

    Il s'agit uniquement d'un prototype, et les textes générés ne sont pas à utiliser en l'état.

    Le projet est open source, et le code et les datasets utilisés pour faire l'application sont disponibles sur
    huggingface : https://huggingface.co/datasets/Forbu14/LoiLibre

    Le code de l'UI est disponible sur github :
    https://github.com/Forbu/loilibre_ui
""")

# Main content
st.markdown("""
    LoiLibre est un chatbot qui génère des textes juridiques à partir d'une base de données de codes juridiques.

    Le projet est en phase de construction et n'est pas encore utilisable en production.

    Il s'agit aussi de rendre accessible le droit à tous, et de permettre à chacun de comprendre les lois qui régissent notre société.

    "Nul n'est censé ignorer la loi" est un principe fondamental de notre société, et pourtant, il est très difficile de comprendre les lois qui régissent notre société.

    Cette initiative a pour but de rendre le droit accessible à tous, et de permettre à chacun de comprendre les lois qui régissent notre société.

    Le principal outil de LoiLibre est un chatbot qui permet de répondre à des questions juridiques en se basant sur une base de données de codes juridiques.
""")
