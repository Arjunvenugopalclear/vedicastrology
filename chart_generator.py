from datetime import datetime, date, time
from typing import Union

def generate_rasi_chart(birth_date: Union[datetime, date], birth_time: time, place_of_birth: str) -> str:
    print(f"Generating Rasi chart for {birth_date} {birth_time} at {place_of_birth}")  # Debug print
    date_str = birth_date.strftime('%Y-%m-%d') if isinstance(birth_date, datetime) else birth_date.isoformat()
    time_str = birth_time.strftime('%H:%M')
    result = f"Placeholder Rasi chart for {date_str} {time_str} at {place_of_birth}"
    print(f"Rasi chart result: {result}")  # Debug print
    return result

def generate_navamsa_chart(birth_date: Union[datetime, date], birth_time: time, place_of_birth: str) -> str:
    print(f"Generating Navamsa chart for {birth_date} {birth_time} at {place_of_birth}")  # Debug print
    date_str = birth_date.strftime('%Y-%m-%d') if isinstance(birth_date, datetime) else birth_date.isoformat()
    time_str = birth_time.strftime('%H:%M')
    result = f"Placeholder Navamsa chart for {date_str} {time_str} at {place_of_birth}"
    print(f"Navamsa chart result: {result}")  # Debug print
    return result

def generate_dasha_chart(birth_date: Union[datetime, date], birth_time: time, place_of_birth: str) -> str:
    print(f"Generating Dasha chart for {birth_date} {birth_time} at {place_of_birth}")  # Debug print
    date_str = birth_date.strftime('%Y-%m-%d') if isinstance(birth_date, datetime) else birth_date.isoformat()
    time_str = birth_time.strftime('%H:%M')
    result = f"Placeholder Dasha chart for {date_str} {time_str} at {place_of_birth}"
    print(f"Dasha chart result: {result}")  # Debug print
    return result

def generate_natal_chart(birth_date: Union[datetime, date], birth_time: time, place_of_birth: str) -> str:
    print(f"Generating Natal chart for {birth_date} {birth_time} at {place_of_birth}")  # Debug print
    date_str = birth_date.strftime('%Y-%m-%d') if isinstance(birth_date, datetime) else birth_date.isoformat()
    time_str = birth_time.strftime('%H:%M')
    result = f"Placeholder Natal chart for {date_str} {time_str} at {place_of_birth}"
    print(f"Natal chart result: {result}")  # Debug print
    return result

def generate_chart(chart_type: str, birth_date: Union[datetime, date], birth_time: time, place_of_birth: str) -> str:
    print(f"generate_chart called with: {chart_type}, {birth_date}, {birth_time}, {place_of_birth}")  # Debug print
    if chart_type.lower() == "rasi":
        return generate_rasi_chart(birth_date, birth_time, place_of_birth)
    elif chart_type.lower() == "navamsa":
        return generate_navamsa_chart(birth_date, birth_time, place_of_birth)
    elif chart_type.lower() == "dasha":
        return generate_dasha_chart(birth_date, birth_time, place_of_birth)
    elif chart_type.lower() == "natal":
        return generate_natal_chart(birth_date, birth_time, place_of_birth)
    else:
        result = f"Unsupported chart type: {chart_type}"
        print(f"Unsupported chart type: {result}")  # Debug print
        return result
