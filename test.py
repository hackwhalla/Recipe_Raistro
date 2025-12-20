import requests
import prompt
import tool
from agent import agent
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

print("""protein = 1
Energy = 2
Carbs = 3
diet_by_region = 4
recipe_with_title = 5""")

#prompts
protein_prompt = prompt.protein_prompt

what_you_want = int(input("what you want: ")) 
match what_you_want:
    case 1:
        minp = int(input("minp")) 
        maxp = int(input("maxp")) 
        page = int(input("page")) 
        user_query = f"Give a high protein dish with protein range min_protein: {minp}, max_protein: {maxp}, page: {page}."
        response = agent(protein_prompt,user_query)
        print(response)
        print(1)
        #protein()
    case 2:
        print(2)
        #Energy()
    case 3:
        print(3)
        #Carbs()
    case 4:
        print(4)
        #diet_by_region()
    case 5:
        print(5)
        #recipe_with_title()
