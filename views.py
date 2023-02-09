from django.shortcuts import render
import openai,os
from dotenv import load_dotenv
load_dotenv()
api_key =os.getenv("OPENAI_KEY",None)

def chatbot(request):
    chatbot_response = None
    if request.method == 'POST':
        openai.api_key=api_key
        user_input = request.POST.get('user_input')
        prompt=user_input

        response=openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=150,
            #stop="."
            temperature=0.9,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
            
        )
        print(response)
        chatbot_response= response["choices"][0]["text"]
    return render(request,'main.html',{"response":chatbot_response})


    