import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm

def dowload(kanda, sarga, total_slokas):
    slokas = []

    # Set up tqdm progress bar
    progress_bar = tqdm(total=total_slokas, desc=f'Downloading JSON {kanda}.{sarga}.json')

    for sloka in range(1, total_slokas + 1):
        url = f"https://www.valmiki.iitk.ac.in/content?language=dv&field_kanda_tid={kanda}&field_sarga_value={sarga}&field_sloka_value={sloka}"
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        
        # Select elements with the "field-content" class
        elements = soup.select('div.field-content')

        # Extract the content
        content = [element.decode_contents() for element in elements]

        # Create the JSON object
        text = content[0]
        meaning = content[1]
        translation = content[2]
        jsonObject = {
            'id': f"{kanda}.{sarga}.{sloka}",
            'script': 'devanagari',
            'kanda': kanda,
            'sarga': sarga,
            'sloka': sloka,
            'description': "",
            'text': text,
            'meaning': meaning,
            'translation': translation,
            'source': url
        }

        slokas.append(jsonObject)

        # Update the progress bar
        progress_bar.update(1)

    # Save JSON data to a file
    file_name = f"slokas/{kanda}.{sarga}.json"
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(slokas, file, ensure_ascii=False, indent=4)

    # Close the progress bar
    progress_bar.close()

    print(f"JSON data saved to {file_name}.")

# Example usage
# Sarga 1
# dowload(1, 1, 100)
# Sarga 1 Downloaded
# Sarga 1 (text) verified

# Sarga 2
# dowload(1, 2, 43)
# Sarga 2 Downloaded

# Sarga 3
# dowload(1, 3, 38)
# Sarga 3 Downloaded

# Sarga 4
# dowload(1, 4, 31)
# Sarga 4 Downloaded