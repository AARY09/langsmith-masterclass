
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

# Initialize the OpenRouter model
model = ChatOpenRouter(
    model="openai/gpt-4o-mini",
    temperature=0
)

parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({
    "question": "What is the capital of india?"
})

print(result)
