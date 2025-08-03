from flask import Flask, render_template, request, redirect
from libretranslate_api import get_supported_languages, translate_text
from db import init_db, insert_translation, get_last_translations

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    languages = get_supported_languages()
    history = get_last_translations()

    if request.method == "POST":
        src = request.form["source_lang"]
        tgt = request.form["target_lang"]
        text = request.form["text"]

        try:
            translated = translate_text(text, src, tgt)
            insert_translation(src, tgt, text, translated)
        except Exception as e:
            translated = f"Translation error: {e}"

        history = get_last_translations()
        return render_template("index.html", languages=languages, result=translated, history=history)

    return render_template("index.html", languages=languages, result=None, history=history)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
