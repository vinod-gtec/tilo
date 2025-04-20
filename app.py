# app.py
from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    
    gather = Gather(num_digits=1, action="/handle-key", method="POST", language="ta-IN")
    gather.say("வணக்கம்! soil testingக்கு 1, பூச்சி கண்டறிதலுக்கு 2, கேள்விக்கு பதில் பெற 3, அரசு திட்டங்கள் அறிய 4 ஐ அழுத்தவும்.", language="ta-IN")
    response.append(gather)
    response.redirect('/voice')
    return str(response)

@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    digit_pressed = request.values.get('Digits')
    response = VoiceResponse()
    
    if digit_pressed == "1":
        response.say("மண் பரிசோதனை தகவல்: உங்கள் அருகிலுள்ள பரிசோதனை மையம் - திருச்சி.", language="ta-IN")
    elif digit_pressed == "2":
        response.say("பூச்சி கண்டறிதல்: உங்கள் பயிரில் பழுப்பு பூச்சி இருக்கலாம். வேளாண்மை அதிகாரியை அணுகவும்.", language="ta-IN")
    elif digit_pressed == "3":
        response.say("தயவுசெய்து உங்கள் கேள்வியை கூறவும்...", language="ta-IN")
        response.record(timeout=5, max_length=30, action="/ai-response")
    elif digit_pressed == "4":
        response.say("அரசு திட்டம்: பிஎம்கிசான் திட்டம்: ரூ.6000 வருடத்திற்கு.", language="ta-IN")
    else:
        response.say("தவறான தேர்வு.", language="ta-IN")
        response.redirect('/voice')
    
    return str(response)

@app.route("/ai-response", methods=['POST'])
def ai_response():
    # Recorded voice URL from Twilio
    recording_url = request.values.get("RecordingUrl")
    
    # You can process audio via Whisper/OpenAI or display in logs
    print("Received question audio at:", recording_url)

    response = VoiceResponse()
    response.say("உங்கள் கேள்விக்கு பதில் விரைவில் அளிக்கப்படும்.", language="ta-IN")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
