import sys
import openai
import datetime
from openaienv import OpenAiEnv

dt_now = datetime.datetime.now()
openai.api_key = OpenAiEnv.OPENAI_API_KEY

def main():
    text_data = open("./target.txt", "r")
    contents = text_data.read().replace('　',' ')
    text_data.close()
    prompt = f'{contents}\nこれを要約する。'
    result = text_summary(prompt)
    return result

def fileOutput(summary):
    f = open('./result'+str(dt_now.strftime('%Y%m%d_%H%M%S'))+'.txt', 'w')
    f.write(summary)
    f.close()

def text_summary(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response["choices"][0]["text"].replace('\n','')

if __name__ == '__main__':
    args = sys.argv
    summary = main()
    fileOutput(summary)