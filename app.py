from flask import Flask, request
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"

@app.route("/generate", methods=["POST"])
def generate_text():
    url = request.get_json()["image_url"]

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Provide feedback on the UI/UX design. Give an overall UI score and an UX score "
                                "including areas of strength and areas of improvement."
                    },
                    {
                        "type": "image_url",
                        "image_url": url
                    },
                ],
            }
        ],
        max_tokens=300
    )

    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    app.run(debug=True)
