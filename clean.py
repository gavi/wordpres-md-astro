import re
import os
import requests

def replace_hero_image(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex to find the first image URL, ensuring it only matches images
    images = re.findall(r'!\[.*?\]\((.*?)\s*(?:["\'].*?["\'])?\)', content)
    if images:
        first_image_url = images[0]
        print(f"Checking image URL: {first_image_url}")  # Debug output

        try:
            # Make a HEAD request to check if the image URL works
            response = requests.head(first_image_url, allow_redirects=True)
            if response.status_code == 200:
                print(f"Image URL is valid: {first_image_url}")

                # Replace the heroImage in the YAML front matter
                new_content = re.sub(r'(heroImage:\s*["\'])(.*?)(["\'])', r'\1' + first_image_url + r'\3', content, count=1)
                print(f"New heroImage line: {re.search(r'heroImage:.*', new_content).group()}")  # Debug output

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated heroImage in {file_path}")
            else:
                print(f"Image URL returned {response.status_code}, not updating heroImage.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve image URL {first_image_url}: {e}")

    else:
        print(f"No images found in {file_path}")

# Iterate through all markdown files in the directory
for filename in os.listdir('.'):
    if filename.endswith('.md'):
        replace_hero_image(filename)
