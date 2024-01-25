
import streamlit as st
import os
import langchain
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
from langchain import HuggingFaceHub,LLMChain
from langchain.prompts import PromptTemplate
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])


def get_llm_response(question):
    llm_chain = LLMChain(prompt=prompt,llm=HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",model_kwargs={"temperature":0.6,"max_length":10000}))
    response=llm_chain.run(question)
    return response

st.set_page_config(page_title="GPT4L")

st.header("GPTransformer")

input=st.text_input("Type here:",key="input")
response=get_llm_response(input)

submit=st.button("Ask the question")

if submit:
    st.subheader("The Response is:")
    st.write(response)
