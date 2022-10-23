import sys
import openai
from openaienv import OpenAiEnv

openai.api_key = OpenAiEnv.OPENAI_API_KEY

def main(dots):
    
    text_data = open("./target.txt", "r")
    contents = text_data.read().replace('　',' ')
    text_data.close()
    
    prompt = f'{contents}\n以下の{dots}点でまとめる。'
    print(prompt)
    result = text_summary(prompt)

    return result

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
    dots = args[1]
    
    summary = main(dots)
    print(summary)