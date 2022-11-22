import sys
import requests

SERVER_API_URL='http://192.168.1.109:5000/predict'

def call_predict_endpoint(question):
  payload_form = { "question": question }
  response = requests.post(SERVER_API_URL, data=payload_form)
  req_time = response.elapsed.total_seconds()
  r = response.json()
  if r['status'] == 0:
    print(f'In {req_time}s - Response for question "{question}" is {r["data"]}')
  else:
    print('No question')

if __name__ == "__main__":
  question = sys.argv[1]
  if question is None:
    print('Dont have question. Exit!')
    exit(0)

  call_predict_endpoint(question)
