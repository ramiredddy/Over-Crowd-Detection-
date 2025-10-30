from flask import Flask, request, jsonify, render_template
from models import crowd_model
import json
import time
import cv2
import numpy as np
import os

app = Flask(__name__)

# In-memory storage for demo purposes
crowd_data = []
alerts = []

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    # Expected data: {'density': float, 'time': float, 'location': str, 'lat': float, 'lon': float}
    density = data.get('density', 0)
    time_of_day = data.get('time', time.time() % 86400 / 3600)  # Hours since midnight
    location_factor = hash(data.get('location', 'default')) % 100 / 100.0  # Simple hash for demo

    risk = crowd_model.predict_risk(density, time_of_day, location_factor)

    entry = {
        'density': density,
        'time': time_of_day,
        'location': data.get('location', 'unknown'),
        'lat': data.get('lat', 0),
        'lon': data.get('lon', 0),
        'risk': risk,
        'timestamp': time.time()
    }
    crowd_data.append(entry)

    # Generate alert if high risk
    if risk == 'High':
        alert = {
            'message': f'High risk detected at {data.get("location", "unknown")} with density {density}',
            'timestamp': time.time(),
            'location': data.get('location', 'unknown')
        }
        alerts.append(alert)

    return jsonify({'status': 'Data received', 'risk': risk})

@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts[-10:])  # Last 10 alerts

@app.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    # Aggregate data for dashboard
    zones = {}
    for entry in crowd_data[-100:]:  # Last 100 entries
        loc = entry['location']
        if loc not in zones:
            zones[loc] = {'density': [], 'risks': []}
        zones[loc]['density'].append(entry['density'])
        zones[loc]['risks'].append(entry['risk'])

    # Compute averages
    for loc in zones:
        zones[loc]['avg_density'] = sum(zones[loc]['density']) / len(zones[loc]['density'])
        zones[loc]['high_risk_count'] = zones[loc]['risks'].count('High')

    return jsonify(zones)

def estimate_density_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    total_density = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Simple density estimation: count non-zero pixels after thresholding
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        density = np.sum(thresh > 0) / (thresh.shape[0] * thresh.shape[1]) * 100
        total_density += density

        if frame_count >= 10:  # Process first 10 frames for demo
            break

    cap.release()
    avg_density = total_density / frame_count if frame_count > 0 else 0
    return avg_density

@app.route('/video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400

    video_file = request.files['video']
    location = request.form.get('location', 'unknown')
    lat = float(request.form.get('lat', 0))
    lon = float(request.form.get('lon', 0))

    if video_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save video temporarily
    video_path = f"temp_{time.time()}.mp4"
    video_file.save(video_path)

    try:
        density = estimate_density_from_video(video_path)
        time_of_day = time.time() % 86400 / 3600
        location_factor = hash(location) % 100 / 100.0

        risk = crowd_model.predict_risk(density, time_of_day, location_factor)

        entry = {
            'density': density,
            'time': time_of_day,
            'location': location,
            'lat': lat,
            'lon': lon,
            'risk': risk,
            'timestamp': time.time()
        }
        crowd_data.append(entry)

        if risk == 'High':
            alert = {
                'message': f'High risk detected from video at {location} with density {density:.2f}',
                'timestamp': time.time(),
                'location': location
            }
            alerts.append(alert)

        os.remove(video_path)  # Clean up
        return jsonify({'status': 'Video processed', 'density': density, 'risk': risk})

    except Exception as e:
        os.remove(video_path)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
