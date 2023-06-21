
API = "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"

import openai
from dotenv import load_dotenv

# Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()


def ReplyBrain(question, chat_log=None):
    FileLog = open("chat_log.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nLiNa : '
    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nLiNa : {answer}"
    FileLog = open("chat_log.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer
#
# reply = ReplyBrain("who are you")
# print(reply)