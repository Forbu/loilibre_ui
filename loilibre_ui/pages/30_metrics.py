"""
In this UI we will plot the metrics of the chatbot

The number of tokens generated with it and the number of questions asked to it.
The number of proposed articles and the number of articles that were actually used.

This work is under developpement and is not yet usable in production.

"""

import streamlit as st

# markdown pour décrire le projet
st.markdown(
    """
    Le nombre de tokens générés avec le chatbot, et le nombre de questions posées au chatbot.
    Le nombre d'articles proposés et le nombre d'articles qui ont été effectivement utilisés.
    """)

# TODO : faire appel au server pour récupérer les données
# TODO : afficher les données sous forme de graphiques
