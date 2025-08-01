import subprocess

def summarize_email(email_text):
    prompt = f"""
Read the following email and extract the following fields:
1. Title (if no subject, infer a title)
2. Summary (2-3 lines)
3. Action Items (if any)
4. Urgency Level (High / Medium / Low)
5. Tone (e.g., formal, friendly, urgent, reminder)

Respond in the following format:
Title: ...
Summary: ...
Action Items: ...
Urgency: ...
Tone: ...

Email:
{email_text.strip()}
    """

    result = subprocess.run(
        ["ollama", "run", "gemma:2b"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode().strip()
