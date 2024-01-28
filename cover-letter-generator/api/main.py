from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def generate(user_name, user_edu, user_exp, user_job):
    system_message = f"My name is {user_name}. My education is {user_edu}. My work experience: {user_exp}. For this job, {user_job} generate a cover letter template for me."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
        ],
    )

    return completion.choices[0].message.content


def save_cover_letter_to_text(cover_letter_content):
    with open("cover_letter.txt", "w") as text_file:
        text_file.write(cover_letter_content)


if __name__ == "__main__":
    user_input1 = input("Enter your name ")
    user_input2 = input("Enter your education ")
    user_input3 = input("Enter your work experience ")
    user_input4 = input("Enter the job description ")

    # Generate cover letter content
    cover_letter_content = generate(user_input1, user_input2, user_input3, user_input4)

    # Save cover letter content to text file
    save_cover_letter_to_text(cover_letter_content)

    print("Cover letter generated and saved to cover_letter.txt.")
