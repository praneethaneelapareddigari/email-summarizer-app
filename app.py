from flask import Flask, request, jsonify, render_template
from ollama_utils import summarize_email
from email import policy
from email.parser import BytesParser
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize_file', methods=['POST'])
def summarize_file():
    uploaded_file = request.files.get('file')
    if not uploaded_file:
        return jsonify({'error': 'No file uploaded'}), 400

    filename = uploaded_file.filename
    ext = os.path.splitext(filename)[1].lower()

    # Extract email body
    if ext == ".eml":
        eml_bytes = uploaded_file.read()
        msg = BytesParser(policy=policy.default).parsebytes(eml_bytes)

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_content()
                    break
        else:
            body = msg.get_content()

    elif ext == ".txt":
        body = uploaded_file.read().decode("utf-8")

    else:
        return jsonify({'error': 'Unsupported file type. Only .eml and .txt allowed.'}), 400

    if not body:
        return jsonify({'error': 'Could not extract email content.'}), 400

    summary = summarize_email(body)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

