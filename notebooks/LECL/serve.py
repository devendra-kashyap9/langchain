from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

## Initialize the model
model = ChatGroq(model="openai/gpt-oss-20b",
                    groq_api_key=groq_api_key)


## 1.Create Prompt Template
system_template = "Translate tyhe foloowing into {language} :"
prompt = ChatPromptTemplate.from_messages(
    [('system', system_template),
     ('user',"{text}")]
)

parser = StrOutputParser()

## create Chain
chain = prompt | model | parser

## app definition
app = FastAPI(title="langchain server",
              version="1.0",
              description="A simple API server using Langchain runnable interface")


## adding chainRoutes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)