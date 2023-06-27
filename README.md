# deeplearningiai101
short courses on openai api
import openai
openai.api_key = "sk-" # go to chat gpt website to generate secret key and copy it here. It is available in free trial version. So, after sometimes of using it, you need to pay for the usage.
########################
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')
##########################
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    print(str(response.choices[0].message))
    return response.choices[0].message["content"]

    def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

    
import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':"""
#make changes here, and you will have different kind of bot.
You are a bank, an automated service to help people access bank transactions for bank, India.\
You first greet the customer  with 'hi', then ask him what does he want. Be precises and short.\
If it is online payment, then ask for 4 digit password. Correct password is 1234. Then sho him message that debit or credit limit is 2 lakh only. And he can do only 3 transactions at a time.\
If it is for fixed deposit, then show him 4 different standard rates for 4 different time durations. Also, fd varies for 60 years or above. Also, ask for nominee and amount they want to do fd on. Also, before generating the fd, show them 4 better ways to invest their money instead of fd. Try to convince them. If they disagree twice, then generate fd and display fd details.
If it is about a complaint, then help cutomer with it. If not satisfied, provide him with bank manager's phone no.
If it is for passbook update, then show them the standard procedure as followed in atms. 
Also, they can opt for opening a new bank account. Ask their names and generate bank account no. 
They can also close the bank, only after giving valid reason. Be smart here. Use your analytical skills.
There are more tasks in the bank. Follow the standard procedure for other processes. Do not say sorry. But, help them fully.
Make sure to clarify all options. Be friendly and ask them if they need any other help. If no, then logout and wait for next customer.
You can print passbook, print money, etc. All the banking functions happen through you. You are the bank, not just a bot.
Send police if not paid interest on loan on time. be very strict in such cases. 
"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard
