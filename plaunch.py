# Example: Product Launch Campaign (Product Description, USP, Target Audience, Marketing Channels, Ad Copy, Landing Page, Email Campaign, Social Media Posts, Press Release, and Performance Metrics)
from llama_cpp_agent import AgentChainElement, AgentChain
from llama_cpp_agent import LlamaCppAgent
from llama_cpp_agent import MessagesFormatterType
from llama_cpp_agent.providers import LlamaCppServerProvider

import warnings
warnings.filterwarnings(action='ignore')
import datetime
from rich.console import Console
console = Console(width=90)
import datetime
from time import sleep

def writehistory(filename,text):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')
    f.close()

#SetFilename
tstamp = datetime.datetime.now()
tstamp = str(tstamp).replace(' ','_')
tstamp = str(tstamp).replace(':','_')
logfile = f'{tstamp[:-7]}_log.txt'
sleep(2)
#Write in the history the first 2 sessions
writehistory(logfile,f'Created with 🌀 Qwen2-0.5b-chat\n---\n')    

model = LlamaCppServerProvider("http://127.0.0.1:8080") #default port llamafile server is 8080
agent = LlamaCppAgent(
    model,
    system_prompt="",
    #predefined_messages_formatter_type=MessagesFormatterType.MISTRAL
)

product_description = AgentChainElement(
    output_identifier="out_0",
    system_prompt="You are a product description writer",
    prompt="Write a detailed product description for {product_name}, including its features and benefits."
)

product_usp = AgentChainElement(
    output_identifier="out_1",
    system_prompt="You are a unique selling proposition (USP) creator",
    prompt="Create a compelling USP for {product_name} based on the following product description:\n--\n{out_0}"
)

target_audience = AgentChainElement(
    output_identifier="out_2",
    system_prompt="You are a target audience identifier",
    prompt="Identify the target audience for {product_name} based on the following product description and USP:\n--\nProduct Description:\n{out_0}\nUSP:\n{out_1}"
)

marketing_channels = AgentChainElement(
    output_identifier="out_3",
    system_prompt="You are a marketing channel strategist",
    prompt="Suggest the most effective marketing channels to promote {product_name} based on the following target audience:\n--\n{out_2}"
)

ad_copy = AgentChainElement(
    output_identifier="out_4",
    system_prompt="You are an advertising copywriter",
    prompt="Write engaging ad copy for {product_name} based on the following product description, USP, and target audience:\n--\nProduct Description:\n{out_0}\nUSP:\n{out_1}\nTarget Audience:\n{out_2}"
)

landing_page = AgentChainElement(
    output_identifier="out_5",
    system_prompt="You are a landing page designer",
    prompt="Create a high-converting landing page structure for {product_name} based on the following product description, USP, target audience, and ad copy:\n--\nProduct Description:\n{out_0}\nUSP:\n{out_1}\nTarget Audience:\n{out_2}\nAd Copy:\n{out_4}"
)

email_campaign = AgentChainElement(
    output_identifier="out_6",
    system_prompt="You are an email marketing specialist",
    prompt="Develop an email campaign for {product_name} based on the following product description, USP, target audience, and landing page structure:\n--\nProduct Description:\n{out_0}\nUSP:\n{out_1}\nTarget Audience:\n{out_2}\nLanding Page Structure:\n{out_5}"
)

social_media_posts = AgentChainElement(
    output_identifier="out_7",
    system_prompt="You are a social media content creator",
    prompt="Create a series of engaging social media posts for {product_name} based on the following product description, USP, target audience, and ad copy:\n--\nProduct Description:\n{out_0}\nUSP:\n{out_1}\nTarget Audience:\n{out_2}\nAd Copy:\n{out_4}"
)

press_release = AgentChainElement(
    output_identifier="out_8",
    system_prompt="You are a press release writer",
    prompt="Write a compelling press release announcing the launch of {product_name} based on the following product description, USP, and target audience:\n--\nProduct Description:\n{out_0}\nUSP:\n{out_1}\nTarget Audience:\n{out_2}"
)

performance_metrics = AgentChainElement(
    output_identifier="out_9",
    system_prompt="You are a marketing performance analyst",
    prompt="Identify the key performance metrics to track the success of the {product_name} launch campaign based on the following marketing channels, ad copy, landing page, email campaign, social media posts, and press release:\n--\nMarketing Channels:\n{out_3}\nAd Copy:\n{out_4}\nLanding Page Structure:\n{out_5}\nEmail Campaign:\n{out_6}\nSocial Media Posts:\n{out_7}\nPress Release:\n{out_8}"
)

chain = [product_description, product_usp, target_audience, marketing_channels, ad_copy, landing_page, email_campaign,
         social_media_posts, press_release, performance_metrics]
agent_chain = AgentChain(agent, chain)

productname = console.input(f'[bold green1]What do you want to launch> ') #ecxample "Smart Fitness Tracker"
start = datetime.datetime.now()
with console.status("🌟 AI Assistant is working on it...",spinner='pong'):
    res = agent_chain.run_chain(additional_fields={"product_name": productname})
delta =  datetime.datetime.now() - start

# LOGGING OUT AN ON FILE THE RESULTS
step00 = f"--------------PRODUCT NAME--------------------\n{res[1]['product_name']}"
console.print(step00)
writehistory(logfile,step00) 
step0 = f"--------------PRODUCT DESCRIPTION--------------------\n{res[1]['out_0']}"
console.print(step0)
writehistory(logfile,step0) 
step1 = f"--------------unique selling proposition--------------------\n{res[1]['out_1']}"
console.print(step1)
writehistory(logfile,step1)    
step2 = f"--------------TARGET AUDIENCE--------------------\n{res[1]['out_2']}"
console.print(step2)
writehistory(logfile,step2)     
step3 = f"--------------EFFECTIVE MARKETING CHANNEL--------------------\n{res[1]['out_3']}"
console.print(step3)
writehistory(logfile,step3)        
step4 = f"--------------ENGAGING ADVERTISE ANNOUCEMENT--------------------\n{res[1]['out_4']}"
console.print(step4)
writehistory(logfile,step4)       
step5 = f"--------------high-converting landing page structure--------------------\n{res[1]['out_5']}"
console.print(step5)
writehistory(logfile,step5)
step6 = f"-----------------EMAIL CAMPAIGN--------------------\n{res[1]['out_6']}"
console.print(step6)
writehistory(logfile,step6)
step7 = f"-----------------SOCIAL MEDIA POST--------------------\n{res[1]['out_7']}"
console.print(step7)
writehistory(logfile,step7)
step8 = f"-------------------------PRESS RELEASE--------------------\n{res[1]['out_8']}"
console.print(step8)
writehistory(logfile,step8)
step9 = f"-------------------------key performance metrics to track the success--------------------\n{res[1]['out_9']}"
console.print(step9)
writehistory(logfile,step9)
console.print('_____________________________________________________________________')
console.print(f'[bold green1]Generated in {delta}')