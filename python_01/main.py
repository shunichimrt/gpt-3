import openai

openai.api_key = ""

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

def crean_text(text):
    text= text.replace('　',' ')
    return text

text = '''
Wikipedia is a multilingual free online encyclopedia written and 
maintained by a community of volunteers through open collaboration 
and a wiki-based editing system. Its editors are known as Wikipedians. 
Wikipedia is the largest and most-read reference work in history. 
It is consistently one of the 10 most popular websites ranked by the 
Similarweb and formerly Alexa; as of 2022, Wikipedia was ranked the 7th most popular site.
It is hosted by the Wikimedia Foundation, an American non-profit organization funded mainly 
through donations.
'''

prompt ='''
つまり、
'''

prompt = crean_text(text) +  prompt

print(text_summary(prompt))