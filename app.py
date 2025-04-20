from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()

    gather = Gather(num_digits=1, action="/handle-key", method="POST", language="ta-IN")
    gather.say("வணக்கம்! விவசாயி ஐ.வி.ஆர் சேவைக்கு வரவேற்கிறோம். Soil testingக்கு 1, பூச்சி கண்டறிதலுக்கு 2, கேள்விக்கு பதில் பெற 3, அரசு திட்டங்களை அறிய 4 ஐ அழுத்தவும்.", language="ta-IN")
    response.append(gather)
    response.redirect('/voice')
    return str(response)

@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    digit_pressed = request.values.get('Digits')
    response = VoiceResponse()

    if digit_pressed == "1":
        response.say("மண் பரிசோதனை: உங்கள் அருகிலுள்ள மண் பரிசோதனை மையம் - திருச்சி வேளாண் நிலையம்.", language="ta-IN")
    elif digit_pressed == "2":
        response.say("பூச்சி கண்டறிதல்: உங்கள் பயிரில் பழுப்பு பூச்சி இருக்கலாம். அருகிலுள்ள வேளாண்மை அதிகாரியை அணுகவும்.", language="ta-IN")
    elif digit_pressed == "3":
        response.say("தயவுசெய்து உங்கள் கேள்வியை கூறவும். பதிவு செய்யப்படுகிறது...", language="ta-IN")
        response.record(timeout=5, max_length=30, action="/ai-response")
    elif digit_pressed == "4":
        response.say("அரசு திட்டம்: பிஎம் கிசான் திட்டம் - வருடத்திற்கு ரூ.6000 வழங்கப்படும்.", language="ta-IN")
    else:
        response.say("தவறான தேர்வு. மீண்டும் முயற்சிக்கவும்.", language="ta-IN")
        response.redirect('/voice')
    
    return str(response)

@app.route("/ai-response", methods=['POST'])
def ai_response():
    recording_url = request.values.get("RecordingUrl")

    # Log or process the recording URL using Whisper/OpenAI later
    print("Received question audio at:", recording_url)

    response = VoiceResponse()
    response.say("உங்கள் கேள்விக்கு பதில் விரைவில் அளிக்கப்படும். நன்றி!", language="ta-IN")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
