from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter # Split based on specific character as embeddings have fixed size
from langchain.vectorstores import FAISS # Vector Database
from langchain.chains.question_answering import load_qa_chain
import os
from dotenv import load_dotenv
from pathlib import Path
import openai
from pdf2image import convert_from_path
import re
import shutil
import sys
import io
import imgkit
import subprocess
import easyocr
from functools import lru_cache
import time