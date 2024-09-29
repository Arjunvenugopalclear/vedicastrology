from datetime import datetime
from chat_request import send_openai_request
from chart_generator import generate_chart

def generate_horoscope(birth_datetime: datetime, place_of_birth: str) -> str:
    rasi_chart = generate_chart("rasi", birth_datetime, birth_datetime, place_of_birth)
    navamsa_chart = generate_chart("navamsa", birth_datetime, birth_datetime, place_of_birth)
    dasha_chart = generate_chart("dasha", birth_datetime, birth_datetime, place_of_birth)
    natal_chart = generate_chart("natal", birth_datetime, birth_datetime, place_of_birth)

    prompt = f"""
    Generate a Vedic astrology horoscope for a person born on {birth_datetime.strftime('%Y-%m-%d')} at {birth_datetime.strftime('%H:%M')} in {place_of_birth}. 
    Include the following aspects:
    1. Sun sign and Moon sign
    2. Rising sign (Ascendant)
    3. Planetary positions in houses
    4. Major life aspects (career, relationships, health)
    5. Current planetary transits and their effects
    6. Any specific influences based on the place of birth

    Consider the following chart information:
    Rasi Chart: {rasi_chart}
    Navamsa Chart: {navamsa_chart}
    Dasha Chart: {dasha_chart}
    Natal Chart: {natal_chart}
    
    Provide a detailed and insightful horoscope based on Vedic astrology principles, taking into account the location of birth and the generated charts.
    """
    
    horoscope = send_openai_request(prompt)
    return horoscope
