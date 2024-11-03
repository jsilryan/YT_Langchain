from imports import *

@lru_cache(maxsize=1)
def llm_setup():
    load_dotenv()
    api_key = os.environ.get("KEY_2")

    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 800, # 800
        chunk_overlap = 200, # 200
        length_function = len # Inbuilt function
    ) 

    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    chain = load_qa_chain(OpenAI(openai_api_key=api_key), chain_type = "stuff")

    reader = easyocr.Reader(["en"])
    return text_splitter, embeddings, chain, reader