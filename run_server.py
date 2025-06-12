#!/usr/bin/env python
"""
Startup script for Disease Prediction System
"""
import os
import sys
import subprocess

def check_requirements():
    """Check if all requirements are installed"""
    try:
        import django
        import sklearn
        import pandas
        import numpy
        import joblib
        import crispy_forms
        print("✓ All required packages are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_models():
    """Check if ML models are trained and available"""
    model_files = [
        'ml_models/saved_models/random_forest_model.pkl',
        'ml_models/saved_models/knn_model.pkl',
        'ml_models/saved_models/label_encoder.pkl',
        'ml_models/saved_models/symptoms_list.pkl'
    ]
    
    for model_file in model_files:
        if not os.path.exists(model_file):
            print(f"✗ Missing model file: {model_file}")
            print("Please run: python ml_models/train_models.py")
            return False
    
    print("✓ All ML models are available")
    return True

def run_migrations():
    """Run Django migrations"""
    try:
        print("Running Django migrations...")
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
        print("✓ Migrations completed")
        return True
    except subprocess.CalledProcessError:
        print("✗ Migration failed")
        return False

def start_server():
    """Start the Django development server"""
    print("\n" + "="*50)
    print("Starting Disease Prediction System")
    print("="*50)
    print("Server will be available at: http://127.0.0.1:8000/")
    print("Press Ctrl+C to stop the server")
    print("="*50 + "\n")
    
    try:
        subprocess.run([sys.executable, 'manage.py', 'runserver'])
    except KeyboardInterrupt:
        print("\n\nServer stopped by user")

def main():
    """Main startup function"""
    print("Disease Prediction System - Startup")
    print("="*40)
    
    # Check requirements
    if not check_requirements():
        return False
    
    # Check models
    if not check_models():
        return False
    
    # Run migrations
    if not run_migrations():
        return False
    
    # Start server
    start_server()
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
