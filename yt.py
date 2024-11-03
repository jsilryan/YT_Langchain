from imports import *
from directory import *
from llm_details import *
from pdf_to_text import *

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
text_splitter, embeddings, chain, reader = llm_setup()

def get_pdf_details(
    file,
    text_splitter,
    embeddings,
    chain,
    query
):
    raw_text = convert_PDF_to_text(reader, file)
    texts = text_splitter.split_text(raw_text)
    print(f"Done with splitting.\n")
    document_search = FAISS.from_texts(texts, embeddings)
    print(f"Done with search.\n")
    
    # Query the text
    docs = document_search.similarity_search(query)
    answer = chain.run(input_documents=docs, question=query)
    print(f"Done with answer.\n")
    print(answer)

if __name__ == "__main__":
    file = r"C:\Users\ryan\Desktop\Projects\Projects\Docs\A-Brief-Introduction-to-Singapore.pdf"
    query = r"Please provide a summary of the pdf with important points as key value pairs."
    get_pdf_details(file, text_splitter, embeddings, chain, query)

