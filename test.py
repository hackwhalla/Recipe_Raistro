import requests
import prompt
import tool
from agent import agent
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.base import MIMEBase
from email import encoders
import os

def mail(response,reciver_email):
    try:  
        body = f"""Hello Food Lover 👋,

        Thank you for choosing Recipe Raistro ❤️
        We’re excited to serve you recipes crafted specially according to your taste and preferences.

        {response}

        ✨Happy Cooking & Happy Eating! 😄

        Warm regards,
        Team Recipe Raistro

        🥗 “Good food is the foundation of genuine happiness."""

        sender_email = "hackwhalla@gmail.com"
        sender_password = "dvup tfns thgk wifx"
        reciver_email = reciver_email

        subject = "Your Personalized Food Recipe from Recipe Rastro 🏪👨🏻‍🍳🍽🍝🍜👩🏻‍🍳🥘🥂✨😋😋😋😍😍😍"
        message =  MIMEMultipart()
        message["From"] = sender_email
        message["To"] = reciver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))
        folder_path = "/content/generated_files"
        # ✅ Only check folder
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(".pdf"):
                    file_path = os.path.join(folder_path, file_name)

                    with open(file_path, "rb") as f:
                        part = MIMEBase("application", "pdf")
                        part.set_payload(f.read())

                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f'attachment; filename="{file_name}"'
                    )
                    message.attach(part)

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login(user=sender_email, password=sender_password)
            server.send_message(message)
            server.quit()
        return "mail sent successfully!!"

    except Exception as e:
        return f"Mail Error: {e} Mail not sent"

    


def protein():
    protein_prompt = prompt.protein_prompt
    min_p = int(input("min_p")) 
    max_p = int(input("max_p")) 
    page = int(input("page"))
    user_prefrence = input("dishes you dont want(optional): ").strip() or "None"
    if user_prefrence != "None":
        user_prefrence = user_prefrence.split(" ")
    user_query = f"Give a high protein dish with protein range min_protein: {min_p}, max_protein: {max_p}, page: {page}. \n\n user_prefrence: user want do not suggest these dishes({user_prefrence})."
    response = agent(protein_prompt,user_query)
    return response

def energy():
    energy_prompt = prompt.energy_prompt
    min_e = int(input("min_e")) 
    max_e = int(input("max_e")) 
    page = int(input("page")) 
    user_prefrence = input("dishes you dont want(optional): ").strip() or "None"
    if user_prefrence != "None":
        user_prefrence = user_prefrence.split(" ") 
    user_query = f"Give a high energy dish with energy range min_energy: {min_e}, max_energy: {max_e}, page: {page}. \n\n user_prefrence: user want do not suggest these dishes({user_prefrence})."
    response = agent(energy_prompt,user_query)
    return response

def carbs():
    carbs_prompt = prompt.carbs_prompt
    min_c = int(input("min_c")) 
    max_c = int(input("max_c")) 
    page = int(input("page")) 
    user_prefrence = input("dishes you dont want(optional): ").strip() or "None"
    if user_prefrence != "None":
        user_prefrence = user_prefrence.split(" ") 
    user_query = f"Give a high carbs dish with carbs range min_carbs: {min_c}, max_carbs: {max_c}, page: {page}. \n\n user_prefrence: user want do not suggest these dishes({user_prefrence})."
    response = agent(carbs_prompt,user_query)
    return response

def diet_by_region():
    diet_by_region_prompt = prompt.diet_by_region_prompt
    region = input("region") 
    diet = input("diet") 
    user_prefrence = input("dishes you dont want(optional): ").strip() or "None"
    if user_prefrence != "None":
        user_prefrence = user_prefrence.split(" ") 
    user_query = f"Give a best in nutrition dish with region name: {region}, diet type: {diet}. \n\n user_prefrence: user want do not suggest these dishes({user_prefrence})."
    response = agent(diet_by_region_prompt,user_query)
    return response

def recipe_with_title():
    recipe_title = input("recipe_title") 
    recipe_with_title_prompt = prompt.recipe_with_title_prompt
    user_prefrence = input("dishes you dont want(optional): ").strip() or "None"
    if user_prefrence != "None":
        user_prefrence = user_prefrence.split(" ")
    user_query = f"Give a recipe instruction and ingredient information with recipe name: {recipe_title}. \n\n user_prefrence: user want do not suggest these dishes({user_prefrence})."
    response = agent(recipe_with_title_prompt,user_query)
    return response

def including_and_excluding_ingredients_categories_and_title():
    including_and_excluding_ingredients_categories_and_title_prompt = prompt.including_and_excluding_ingredients_categories_and_title_prompt
    includeIngredients = input("includeIngredients").split(" ")
    excludeIngredients = input("excludeIngredients").split(" ")
    includeCategories = input("includeCategories").split(" ")
    excludeCategories = input("excludeCategories").split(" ")
    page = int(input("page")) 
    title = str(input("title")) 
    user_prefrence = input("dishes you dont want(optional): ").strip() or "None"
    if user_prefrence != "None":
        user_prefrence = user_prefrence.split(" ") 
    user_query = f"Give a recipe instruction and ingredient information of dish. dish name: {title}. with includeIngredients: {includeIngredients}, excludeIngredients: {excludeIngredients}, includeCategories: {includeCategories}, excludeCategories: {excludeCategories}, page: {page}. \n\n user_prefrence: user want do not suggest these dishes({user_prefrence})."
    response = agent(including_and_excluding_ingredients_categories_and_title_prompt,user_query)
    return response

if __name__ == "__main__":
    print("""protein = 1
    Energy = 2
    Carbs = 3
    diet_by_region = 4
    recipe_with_title = 5
    including_and_excluding_ingredients_categories_and_title = 6""")

    options = {
    1: protein,
    2: energy,
    3: carbs,
    4: diet_by_region,
    5: recipe_with_title,
    6: including_and_excluding_ingredients_categories_and_title
       }
    
    what_you_want = int(input("what you want: ")) 
    response = options[what_you_want]()
    print(response)
    mail = mail(response,"sagarmandil01@gmail.com")
    print(mail)



"""    what_you_want = int(input("what you want: ")) 
    match what_you_want:
        case 1:  #protein()
            response = protein()
            print(response)
        case 2:  #Energy()
            response = energy()
            print(response)
        case 3:  #Carbs()
            response = carbs()
            print(response)
        case 4:  #diet_by_region()
            response = diet_by_region()
            print(response)
        case 5:  #recipe_with_title()
            response = recipe_with_title()
            print(response)
        case 6:  #including_and_excluding_ingredients_categories_and_title()
            response = including_and_excluding_ingredients_categories_and_title()
            print(response)"""


"""    mail = mail(response,"goyaladarsh49@gmail.com")
    print(mail)
"""