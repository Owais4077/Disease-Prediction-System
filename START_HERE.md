# 🚀 Disease Prediction System - Quick Start Guide

## ⚡ Fastest Way to Run

### Option 1: One-Click Start (Recommended)
```bash
python run_server.py
```

### Option 2: Manual Start
```bash
python manage.py runserver
```

### Option 3: Windows Users
Double-click: `start_server.bat`

## 🌐 Access the Application

After starting the server, open your browser and go to:
**http://127.0.0.1:8000/**

## 🎯 How to Use

1. **Select Symptoms**: Check the symptoms you're experiencing
2. **Choose Model**: Select from 7 AI models (Gradient Boosting recommended)
3. **Get Prediction**: Click "Predict Disease"
4. **View Results**: See the predicted disease with confidence score

## 🔧 If You Get Errors

### Quick Fix Commands:
```bash
# Install missing packages
pip install Django scikit-learn pandas numpy joblib matplotlib django-crispy-forms crispy-bootstrap5

# If models are missing
python ml_models/train_models.py

# If database issues
python manage.py migrate

# Check system status
python diagnose_system.py
```

## 📱 What You Should See

✅ **Home Page**: Symptom selection form with 82+ symptoms  
✅ **Model Selection**: 7 different AI algorithms to choose from  
✅ **Results Page**: Disease prediction with confidence scores  
✅ **About Page**: Information about all 7 models  

## 🆘 Need Help?

1. **Run Diagnostic**: `python diagnose_system.py`
2. **Check Troubleshooting Guide**: Open `TROUBLESHOOTING_GUIDE.md`
3. **Verify Installation**: All packages should be installed

## 🎉 Success Indicators

- Server starts without errors
- Browser loads http://127.0.0.1:8000/
- You see "Disease Prediction System" with symptom checkboxes
- All 7 models appear in the dropdown menu

**That's it! You're ready to predict diseases with AI! 🤖**
