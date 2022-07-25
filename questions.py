from api_calls import *
import json
from random import randint


def get_one_question(num ,token):
    payload={}
    headers = {
    'Authorization': 'Bearer ' + token
}
    questions = requests.get( url + endpoint_question_all, headers=headers, data=payload)
    data = questions.json()
    question_dict ={
    "questions" : data['questions'][num]['question'],
    "id" : data['questions'][num]["id"],
    "answer" : data['questions'][num]['answer']
    }
    return f'Question: {question_dict["questions"]}'


def get_answer(num ,token):
    payload={}
    headers = {
    'Authorization': 'Bearer ' + token
}
    questions = requests.get( url + endpoint_question_all, headers=headers, data=payload)
    data = questions.json()
    question_dict ={
    "questions" : data['questions'][num]['question'],
    "id" : data['questions'][num]["id"],
    "answer" : data['questions'][num]['answer']
    }
    return question_dict["answer"]

#####################################################################################################
#########################GET ALL QUESTIONS#################################################
def all_questions(token):
  
    payload={}
    headers = {
        'Authorization': 'Bearer ' + token
}
    questions = requests.get( url + endpoint_question_all, headers=headers, data=payload)
    return questions.json()['questions']

######################################CREATE A QUESTION###################################################################################
def create_question(token ,payload):

    payload = json.dumps(payload)
    headers = {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    }

    response = requests.post(url+ endpoint_question, headers=headers, data=payload)
    return response.text
###########################################EDIT QUESTION############################################################3
def edit_question(token ,payload):
    q_id = input("what is the question id?")

    payload = json.dumps(payload)
    headers = {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    }

    response = requests.put(url+ endpoint_edit_question+str(q_id), headers=headers, data=payload)
    return response.text








def delete_user(token):
    headers = {
        'Authorization':"Bearer " + token
    }
    
    response = requests.delete(
        url+endpoint_user,
        headers=headers
    )
    return response.text
