# Disease Prediction System - Troubleshooting Guide

## 🚀 Quick Start (Recommended Method)

### Method 1: Using the Startup Script
```bash
# Navigate to project directory
cd "Disease Prediction System"

# Run the startup script
python run_server.py
```

### Method 2: Manual Setup
```bash
# 1. Install required packages
pip install Django scikit-learn pandas numpy joblib matplotlib django-crispy-forms crispy-bootstrap5

# 2. Run migrations
python manage.py migrate

# 3. Start server
python manage.py runserver
```

### Method 3: Windows Batch File
```bash
# Double-click the file or run in command prompt
start_server.bat
```

## 🔧 Common Errors and Solutions

### Error 1: "ModuleNotFoundError: No module named 'django'"
**Solution:**
```bash
pip install Django
# or
pip install -r requirements.txt
```

### Error 2: "ModuleNotFoundError: No module named 'sklearn'"
**Solution:**
```bash
pip install scikit-learn
```

### Error 3: "ModuleNotFoundError: No module named 'crispy_forms'"
**Solution:**
```bash
pip install django-crispy-forms crispy-bootstrap5
```

### Error 4: "FileNotFoundError: [Errno 2] No such file or directory: 'ml_models/saved_models/...'"
**Solution:**
```bash
# Train the models first
python ml_models/train_models.py
```

### Error 5: "Port already in use" or "Address already in use"
**Solution:**
```bash
# Use a different port
python manage.py runserver 8001

# Or kill existing processes (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F

# Or kill existing processes (Mac/Linux)
lsof -ti:8000 | xargs kill -9
```

### Error 6: "ImportError: cannot import name 'DiseasePredictor'"
**Solution:**
```bash
# Make sure you're in the correct directory
cd "Disease Prediction System"

# Check if the file exists
dir ml_models\train_models.py  # Windows
ls ml_models/train_models.py   # Mac/Linux
```

### Error 7: Database Migration Errors
**Solution:**
```bash
# Delete existing migrations and database
del db.sqlite3  # Windows
rm db.sqlite3   # Mac/Linux

# Create fresh migrations
python manage.py makemigrations
python manage.py migrate
```

## 📋 Step-by-Step Setup Instructions

### Step 1: Verify Python Installation
```bash
python --version
# Should show Python 3.7 or higher
```

### Step 2: Install Dependencies
```bash
# Install all required packages
pip install Django>=4.2.0 scikit-learn>=1.2.0 pandas>=1.5.0 numpy>=1.21.0 joblib>=1.2.0 matplotlib>=3.5.0 django-crispy-forms>=1.14.0 crispy-bootstrap5>=0.6
```

### Step 3: Verify Installation
```bash
python -c "import django, sklearn, pandas, numpy, joblib, matplotlib, crispy_forms; print('All packages installed successfully!')"
```

### Step 4: Train ML Models
```bash
python ml_models/train_models.py
```

### Step 5: Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Start Server
```bash
python manage.py runserver
```

### Step 7: Access Application
Open browser and go to: http://127.0.0.1:8000/

## 🐛 Advanced Troubleshooting

### Check Current Directory
```bash
# Make sure you're in the right directory
pwd  # Mac/Linux
cd   # Windows

# Should show: .../Disease Prediction System
```

### Verify File Structure
```bash
# Check if all files exist
dir  # Windows
ls   # Mac/Linux

# Should see:
# - manage.py
# - requirements.txt
# - ml_models/
# - predictor/
# - data/
```

### Test ML Models
```bash
python test_prediction.py
```

### Check Django Installation
```bash
python -c "import django; print(django.get_version())"
```

### Reset Everything (Nuclear Option)
```bash
# 1. Delete database
del db.sqlite3  # Windows
rm db.sqlite3   # Mac/Linux

# 2. Delete migrations
del predictor\migrations\0*.py  # Windows
rm predictor/migrations/0*.py   # Mac/Linux

# 3. Reinstall packages
pip uninstall Django scikit-learn pandas numpy joblib matplotlib django-crispy-forms crispy-bootstrap5 -y
pip install Django scikit-learn pandas numpy joblib matplotlib django-crispy-forms crispy-bootstrap5

# 4. Retrain models
python ml_models/train_models.py

# 5. Fresh migrations
python manage.py makemigrations
python manage.py migrate

# 6. Start server
python manage.py runserver
```

## 📞 Getting Help

### Check Server Status
```bash
# Test if server is running
curl http://127.0.0.1:8000/
# or open http://127.0.0.1:8000/ in browser
```

### View Server Logs
The server will show logs in the terminal. Look for:
- ✅ "System check identified no issues"
- ✅ "Starting development server at http://127.0.0.1:8000/"
- ❌ Any error messages in red

### Common Success Indicators
- Server starts without errors
- You can access http://127.0.0.1:8000/
- Form loads with 82+ symptoms
- All 7 ML models are available in dropdown

## 🎯 Quick Test

After starting the server, test these URLs:
- http://127.0.0.1:8000/ (Main page)
- http://127.0.0.1:8000/about/ (About page)
- http://127.0.0.1:8000/admin/ (Admin interface)

If all load successfully, the system is working correctly!
