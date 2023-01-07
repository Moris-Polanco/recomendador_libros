import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")



st.title("Recomendador de libros")

intereses = st.text_input("¿Qué tipo de libros te gustan?", "")

if st.button("Recomendar libro"):
  model_engine = "text-davinci-003"

  prompt = (f"Recomendar libros en español sobre {intereses}")

  completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
  )

  recommendation = completions.choices[0].text
  st.write(recommendation)
