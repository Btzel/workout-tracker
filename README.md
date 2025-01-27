# Natural Language Workout Tracker
A Python application that converts natural language exercise descriptions into structured workout data using Nutritionix API and stores it in a Google Sheet.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![API](https://img.shields.io/badge/Nutritionix-API-red)
![Sheets](https://img.shields.io/badge/Google-Sheets-green)
![Tracking](https://img.shields.io/badge/Workout-Tracking-orange)

## 🎯 Overview
This project creates an intuitive workout tracking system that:
1. Accepts natural language input
2. Processes exercise descriptions
3. Calculates calories burned
4. Records workout duration
5. Logs data automatically

## 🏃 Application Features
### Input Processing
- Natural language understanding
- Exercise type detection
- Duration calculation
- Calorie estimation
- Real-time logging

### Data Management
- Google Sheets integration
- Timestamp tracking
- Secure authentication
- Structured data storage
- Exercise categorization

## 🔧 Technical Components
### Exercise Processing System
```python
exercise_parameters = {
    'query': exercise_query,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}
```

### Key Features
1. **Natural Language Processing**
   - Exercise identification
   - Duration extraction
   - Distance calculation
   - Calorie computation

2. **Data Security**
   - Base64 authentication
   - Secure API calls
   - Environment variables
   - Protected endpoints

3. **Data Organization**
   - Structured JSON
   - Timestamped entries
   - Exercise categorization
   - Calorie tracking

## 💻 Implementation Details
### API Integration
- Nutritionix API for exercise processing
- Google Sheets API for data storage
- HTTP request handling
- Response validation

### Data Storage
- Date and time tracking
- Exercise details
- Duration metrics
- Calorie calculations

## 🚀 Usage
1. Install required packages:
```bash
pip install requests
```

2. Set up environment variables:
```bash
export APP_ID="your_nutritionix_app_id"
export API_KEY="your_nutritionix_api_key"
export SHEET_ENDPOINT="your_google_sheet_endpoint"
export SHEET_AUTH_USERNAME="your_basic_auth_username"
export SHEET_AUTH_PASSWORD="your_basic_auth_password"
```

3. Run the tracker:
```bash
python main.py
```

## 🎯 Tracking Rules
1. Enter exercise in natural language
2. Include duration or distance
3. Wait for processing
4. Check sheet for entry
5. Verify calorie calculations

## 🛠️ Project Structure
```
workout-tracker/
├── main.py           # Application core
└── .env             # Environment variables
```

## 📊 Features
### Input Processing
- Natural text input
- Exercise recognition
- Duration parsing
- Distance calculation

### Output Management
- Google Sheets logging
- Calorie tracking
- Exercise categorization
- Time stamping

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL