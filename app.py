import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document
from google.generativeai import configure


api_key = "AIzaSyC8GwlU4BL4cc0TyWtidoXz9g18NJJB7Tk"

def configure_genai():
    configure(api_key=api_key)

configure_genai()

def get_conversational_chain():
    prompt_template = """
    You are a recipe bot. You know all types of recipes. Suggest recipes with ingredients and preparation processes.
    If asked unrelated questions, respond with: "I don't know, I only handle recipe-related queries."

    Context: {context}
    Question: {question}

    Only return the helpful answer below and nothing else.
    Helpful answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    chain = get_conversational_chain()
    dummy_context = [Document(page_content="This is a placeholder context for the recipe bot.")]
    response = chain({"input_documents": dummy_context, "question": user_question}, return_only_outputs=True)
    return response["output_text"]

st.title("Sumir Rannaghar 2.0")
st.subheader("Chat with the Recipe BOT")
user_message = st.text_input("Type your message here:")

if user_message:
    bot_response = user_input(user_message)
    st.write("*Assistant:*", bot_response)
