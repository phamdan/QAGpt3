import openai
import os
from tqdm import tqdm
def init(path_to_document,key_api):
    openai.api_key =key_api
    documents=[]
    for root,dirs,files in tqdm(os.walk(path_to_document)):
        for name in files:
            if(name.endswith("txt")):
                path_text=os.path.join(root, name)
                with open(path_text,"r") as f:
                    for line in f.readlines():
                        documents.append(line)
    text=""
    for value in documents:
        text+=(value+"\n")
    return text

def predict(question,document):
    response = openai.Answer.create(
        search_model="ada", 
        model="curie", 
        question=question, 
        documents=[document], 
        examples_context="In 2017, U.S. life expectancy was 78.6 years.", 
        examples=[["What is human life expectancy in the United States?", "78 years."]], 
        max_tokens=30,
        stop=["\n", "<|endoftext|>"]
    )
    return response["answers"][0]

if __name__ == "__main__":
    path_to_documents="data_gpt3" 
    question= "A quip from doc after he gets angry from dying ?"
    key_api=""
    
    text= init(path_to_documents,key_api)
    answer= predict(question,text)
    print(answer)

    
