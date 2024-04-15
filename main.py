import os
import argparse
import google.generativeai as genai
import PIL.Image
from src.prompt.srs_prompt import SRS_PROMPT

def parse_args(): 
    parser = argparse.ArgumentParser(
        description="Generate SRS document from image"
    );
    parser.add_argument("image", type=str, help="Path of the image")
    return parser.parse_args()

def main():
    args = parse_args()

    img = PIL.Image.open(args.image)

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro-vision')

    response = model.generate_content([SRS_PROMPT, img])

    response.resolve()

    print(response.text)

    with open("output.md", "w") as f:
        f.write(response.text)
        print('------- Written output')


if __name__ == "__main__":
    main()