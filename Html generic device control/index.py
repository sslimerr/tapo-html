from flask import Flask, render_template, request, jsonify
import asyncio
from tapo import ApiClient

app = Flask(__name__)

tapo_username = "email" # Set your Tapo email
tapo_password = "password" # Set your Tapo password
device_ip = "192.168.1.---" # Set your device IP

@app.route('/')
def index():
    return render_template('index.html')

async def control_light(action):
    client = ApiClient(tapo_username, tapo_password)
    device = await client.l510(device_ip)
    if action == 'on':
        await device.on()
    elif action == 'off':
        await device.off()

@app.route('/control', methods=['POST'])
def control():
    action = request.form.get('action')
    asyncio.run(control_light(action))
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='192.168.1.---', port=8080, debug=True) # Set your IP and port
