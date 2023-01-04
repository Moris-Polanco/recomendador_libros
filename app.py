import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def obtener_recomendaciones(genero, edad, sexo, autores_favoritos):
  model_engine = "text-davinci-003"
  prompt = (f"Recomendaciones de libros en español para un {sexo} de {edad} años que disfruta de {genero} y cuya autores favoritos son {autores_favoritos}")

  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  respuesta = completions.choices[0].text
  recomendaciones = respuesta.split("\n")[2:]
  return recomendaciones

st.title("Recomendador de libros personalizado")
st.markdown("Este es un recomendador de libros personalizado que utiliza GPT-3 para proporcionar recomendaciones en español basadas en tus intereses y preferencias.")

genero = st.text_input("¿Qué tipo de libros te gustaría leer?", "novela histórica")
edad = st.number_input("¿Cuál es tu edad?", min_value=0, max_value=100)
sexo = st.radio("¿Hombre o mujer?", ("Hombre", "Mujer"))
autores_favoritos = st.text_input("¿Cuáles son tus autores favoritos?", "Posteguillo, Delibes, García Márquez")

recomendaciones = obtener_recomendaciones(genero, edad, sexo, autores_favoritos)

st.header("Recomendaciones:")
for recomendacion in recomendaciones:
  st.markdown(f"- {recomendacion}")
