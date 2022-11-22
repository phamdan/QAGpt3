import warnings
import openai
import os
import settings
import json

from tqdm import tqdm
from flask import Flask, jsonify, abort, request
from werkzeug.exceptions import HTTPException, default_exceptions
from logger import AppLogger

app = Flask(__name__)
warnings.filterwarnings("ignore")

def init(path_to_document, key_api):
  openai.api_key =key_api
  documents=[]
  for root, dirs, files in tqdm(os.walk(path_to_document)):
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

@app.route('/predict', methods=['POST', 'GET'])
def predict():
  if request.method == 'GET':
    abort(404)

  json_response = {}
  question = request.form.get('question')
  if question is None:
    abort(400)

  res_answers = openai.Answer.create(
    search_model="ada",
    model="curie",
    question=question,
    documents=[gpt3_model],
    examples_context="In 2017, U.S. life expectancy was 78.6 years.",
    examples=[["What is human life expectancy in the United States?", "78 years."]],
    max_tokens=30,
    stop=["\n", "<|endoftext|>"]
  )

  if 'answers' in res_answers:
    json_response['status'] = 0
    json_response['data'] = res_answers.answers[0]
    return_code = 200
  else:
    json_response['status'] = 1
    return_code = 404

  result = json.dumps(json_response, ensure_ascii=False).encode("utf8")
  logger.info(f'{request.remote_addr} - Response for question "{question}" is {result}')
  return result, return_code

@app.errorhandler(Exception)
def handle_exception(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    error_str = jsonify(message=str(e), code=code, success=False)
    logger.error("EXCEPTION: %s" % error_str.data.decode("utf-8"))
    return error_str

# register error handler
for ex in default_exceptions:
    app.register_error_handler(ex, handle_exception)

if __name__ == "__main__":
  logger = AppLogger()

  gpt3_model = init(settings.OPENAI_DOCUMENTS_PATH, settings.OPENAI_API_KEY)

  app.run(host="0.0.0.0", port=5000)
