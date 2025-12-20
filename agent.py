import tool
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

def agent(prompt,user_query):
    #tools
    protein = tool.protein
    Energy = tool.Energy
    Carbs = tool.Carbs
    diet_by_region = tool.diet_by_region
    recipe_instruction = tool.recipe_instruction
    ingrendints = tool.ingrendints
    recipe_with_title = tool.recipe_with_title

    #load key
    load_dotenv()
    api_key = os.getenv("API_KEY")

    client = genai.Client(api_key=api_key)
    config = types.GenerateContentConfig(tools=[protein, recipe_instruction, Energy, Carbs, diet_by_region, ingrendints, recipe_with_title])

    # Combine system and user content into a single user message for generate_content
    combined_user_content = f"user query-- {user_query}"

    # Create the correctly formatted contents list
    contents_for_generation = [
        types.Content(role="model", parts=[types.Part(text=prompt)]),
        types.Content(role="user", parts=[types.Part(text=combined_user_content)])
    ]

    # Send request with function declarations
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents_for_generation,
        config=config,
    )
    try:
        return(response.text)
    except:
        return(f"model response error {response}")