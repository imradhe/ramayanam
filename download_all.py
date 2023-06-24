import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm

def download(kanda, sarga, total_slokas):
    slokas = []

    # Set up tqdm progress bar
    progress_bar = tqdm(total=total_slokas, desc=f'Downloading JSON {kanda}.{sarga}.json')

    try:
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
    except Exception as e:
        print(f"Error occurred: {e}")
        # Save the JSON data collected so far to a file
        file_name = f"test/{kanda}.{sarga}.json"
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(slokas, file, ensure_ascii=False, indent=4)
        print(f"Partial JSON data saved to {file_name}.")

    # Save JSON data to a file
    file_name = f"test/{kanda}.{sarga}.json"
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(slokas, file, ensure_ascii=False, indent=4)

    # Close the progress bar
    progress_bar.close()

    print(f"JSON data saved to {file_name}.")

# Load the stats from the JSON file
with open('stats.json', 'r') as f:
    stats = json.load(f)

# Set up tqdm progress bar for overall download progress
overall_progress_bar = tqdm(total=len(stats), desc='Downloading all sargas')

# Iterate through each element in the stats
for item in stats:
    kanda = item[0]
    sarga = item[1]
    total_slokas = item[2]

    # Print the kanda, sarga, and total_slokas
    download(kanda, sarga, total_slokas)

    # Update the overall progress bar
    overall_progress_bar.update(1)

# Close the overall progress bar
overall_progress_bar.close()