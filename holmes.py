import logging
import sys
import os
import numexpr as ne
import openai


from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

os.environ['NUMEXPR_MAX_THREADS'] = '4'
os.environ['NUMEXPR_NUM_THREADS'] = '2'

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.log = "debug"

from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

try:
    storage_context = StorageContext.from_defaults(persist_dir='./storage/cache/holmes/books')
    index = load_index_from_storage(storage_context)
    print('loading from disk')
except:
    documents = SimpleDirectoryReader('corpus/books').load_data()
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    index.storage_context.persist(persist_dir='./storage/cache/holmes/books/')
    print('persisting to disk')
    
from llama_index.prompts import PromptTemplate

text_qa_template_str = (
    "You are a Sherlock Holmes assistant that can read the Sherlock Holmes Stories.\n"
    "Always answer the query only using the provided context information, "
    "and not prior knowledge.\n"
    "Some rules to follow:\n"
    "1. Never directly reference the given context in your answer.\n"
    "2. Avoid statements like 'Based on the context, ...' or "
    "'The context information ...' or anything along "
    "those lines."
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Answer the question: {query_str}\n"
)

text_qa_template = PromptTemplate(text_qa_template_str)

response = index.as_query_engine(
    text_qa_template = text_qa_template 
).query("How does Sherlock Holmes solve crimes")

from llama_index.response.pprint_utils import pprint_response
pprint_response(response, show_source=True)
