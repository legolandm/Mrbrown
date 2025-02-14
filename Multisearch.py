import os
import requests
from duckduckgo_search import ddg_images

def download_images(keywords, num_images, output_dir):
    for keyword in keywords:
        print(f"Searching images for: {keyword}")
        results = ddg_images(keyword, max_results=num_images)

        folder = os.path.join(output_dir, keyword)
        os.makedirs(folder, exist_ok=True)

        count = 0
        for result in results:
            try:
                image_url = result['image']
                response = requests.get(image_url, stream=True)

                if response.status_code == 200:
                    image_path = os.path.join(folder, f"{keyword}_{count + 1}.jpg")
                    with open(image_path, 'wb') as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    print(f"Downloaded: {image_path}")
                    count += 1

                    if count >= num_images:
                        break
            except Exception as e:
                print(f"Failed to download image: {e}")

if __name__ == "__main__":
    # Input from user
    keywords = input("Enter keywords separated by commas (e.g., cat, dog, car): ").split(',')
    keywords = [kw.strip() for kw in keywords]
    num_images = 5
    output_dir = "Downloaded_Images"

    download_images(keywords, num_images, output_dir)
    print("All images downloaded successfully!")
