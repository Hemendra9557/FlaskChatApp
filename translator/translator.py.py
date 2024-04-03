from deepl import Translator
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
deepl_api_key = (
    "e6f1d062-5229-463b-b11f-6945aa2b969f:fx"  # Replace with your actual DeepL API key
)
translator = Translator(deepl_api_key)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_response", methods=["POST"])
def generate_response():
    data = request.get_json()
    text = data.get("text")
    target_language = data.get(
        "target_language", "FR"
    )  # Default to English if target_language is not provided

    ai_text = generate_text(text)
    translated_text = translate_text(ai_text, target_language)

    return jsonify({"ai_text": ai_text, "translated_text": translated_text})


def generate_text(text):
    return text


def translate_text(text, target_language):
    translation = translator.translate_text(text, target_lang="fr")
    return translation.text


if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Change port number as needed
