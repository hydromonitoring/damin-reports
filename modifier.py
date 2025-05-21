import os

from PIL import Image



def convert_png_to_webp(root_folder):

    for foldername, subfolders, filenames in os.walk(root_folder):

        for filename in filenames:

            if filename.lower().endswith('.png'):

                full_path = os.path.join(foldername, filename)

                webp_path = os.path.splitext(full_path)[0] + '.webp'

                try:

                    img = Image.open(full_path).convert("RGBA")

                    img.save(webp_path, 'webp')

                    os.remove(full_path)

                    print(f"Converted and removed: {full_path}")

                except Exception as e:

                    print(f"Error converting {full_path}: {e}")



def update_html_references(root_folder):

    for foldername, subfolders, filenames in os.walk(root_folder):

        for filename in filenames:

            if filename.lower().endswith('.html'):

                html_path = os.path.join(foldername, filename)

                with open(html_path, 'r', encoding='utf-8') as file:

                    content = file.read()

                updated_content = content.replace('.png', '.webp')

                if content != updated_content:

                    with open(html_path, 'w', encoding='utf-8') as file:

                        file.write(updated_content)

                    print(f"Updated image references in: {html_path}")



if __name__ == "__main__":

    root_folder = input("Enter the root folder path: ").strip()

    convert_png_to_webp(root_folder)

    update_html_references(root_folder)


