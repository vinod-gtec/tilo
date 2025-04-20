from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/ivr", methods=["POST", "GET"])
def ivr_menu():
    response_xml = """
    <Response>
        <GetInput action="/handle-key" method="POST" timeout="10" numDigits="1">
            <Say language="ta-IN">வணக்கம்! மண் பரிசோதனைக்கு 1 ஐ, பூச்சி கண்டறிதலுக்கு 2 ஐ, கேள்விக்கான பதிலுக்கு 3 ஐ, அரசு திட்டங்களுக்கு 4 ஐ அழுத்தவும்.</Say>
        </GetInput>
    </Response>
    """
    return Response(response_xml, mimetype='text/xml')


@app.route("/handle-key", methods=["POST", "GET"])
def handle_key():
    digits = request.values.get("Digits", "")
    
    if digits == "1":
        say_text = "மண் பரிசோதனை மையம் உங்கள் அருகில் உள்ளது."
    elif digits == "2":
        say_text = "பூச்சி கண்டறிதல்: பழுப்பு பூச்சி இருக்கலாம்."
    elif digits == "3":
        say_text = "உங்கள் கேள்வியை விரைவில் பதிலளிக்கப்படும்."
    elif digits == "4":
        say_text = "பிஎம் கிசான் அரசு திட்டம்: வருடத்திற்கு ரூ.6000 உதவித் தொகை."
    else:
        say_text = "தவறான தேர்வு. மீண்டும் முயற்சிக்கவும்."

    response_xml = f"""
    <Response>
        <Say language="ta-IN">{say_text}</Say>
    </Response>
    """
    return Response(response_xml, mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
