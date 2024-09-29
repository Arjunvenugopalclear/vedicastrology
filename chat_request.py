import os
from openai import OpenAI, OpenAIError
from typing import List, Dict, Any

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def send_openai_request(messages: List[Dict[str, str]]):
    # Extract birth information from the conversation
    birth_info = extract_birth_info(messages)
    
    # Prepare the messages for OpenAI, including birth information
    openai_messages = prepare_messages(messages, birth_info)
    
    try:
        completion = openai_client.chat.completions.create(
            model="gpt-4o",  # Using GPT-4 for complex Vedic astrology tasks
            messages=[{"role": msg["role"], "content": msg["content"]} for msg in openai_messages],
            max_tokens=3000
        )
        content = completion.choices[0].message.content
        if not content:
            raise ValueError("OpenAI returned an empty response.")
        return content
    except OpenAIError as e:
        return f"Error in OpenAI request: {str(e)}. Please try again."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}. Please try again."

def extract_birth_info(messages: List[Dict[str, str]]) -> Dict[str, str]:
    birth_info = {}
    for message in messages:
        if message["role"] == "user":
            content = message["content"].lower()
            if "date of birth" in content:
                birth_info["date_of_birth"] = content.split("date of birth")[-1].strip()
            if "time of birth" in content:
                birth_info["time_of_birth"] = content.split("time of birth")[-1].strip()
            if "place of birth" in content:
                birth_info["place_of_birth"] = content.split("place of birth")[-1].strip()
    return birth_info

def prepare_messages(messages: List[Dict[str, str]], birth_info: Dict[str, str]) -> List[Dict[str, str]]:
    openai_messages = [
        {"role": "system", "content": """You are an expert Vedic astrologer with deep knowledge of Jyotish principles of Hindu culture. Your task is to provide insightful and personalized astrological guidance based on the user's birth information and questions. Use only Hindu principles for analysis. Follow these guidelines:

1. Interpret the user's birth chart (Rasi, Navamsa, Dasha, and Natal) using Vedic astrology principles. Start by informing the user of his Nakshatra and Rasi of both solar and lunar signs.
2. Consider the positions of planets in houses and signs, as well as their aspects and conjunctions.
3. Analyze the strengths and weaknesses of different planets and houses in the chart.
4. Provide insights on life areas such as career, relationships, health, spirituality, and personal growth.
5. Offer predictions based on current planetary transits and ongoing Dasha periods.
6. When appropriate, suggest remedies or practices aligned with Vedic astrology traditions.
7. Always maintain a respectful and supportive tone, focusing on empowering the user with knowledge.
8. If specific birth information is missing, provide general guidance based on available data.
9. Be prepared to explain Vedic astrology concepts if the user asks for clarification.
10. Mention the sanskrit names as well as Engligh names of the planets and houses while providing information.

Remember to tailor your responses to the user's specific questions and concerns while incorporating relevant astrological insights."""}
    ]
    
    if birth_info:
        birth_info_str = f"Birth Information: Date: {birth_info.get('date_of_birth', 'Unknown')}, Time: {birth_info.get('time_of_birth', 'Unknown')}, Place: {birth_info.get('place_of_birth', 'Unknown')}"
        openai_messages.append({"role": "system", "content": birth_info_str})
    
    for message in messages:
        if message["role"] != "system":
            openai_messages.append(message)
    
    return openai_messages
