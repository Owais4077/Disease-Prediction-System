#!/usr/bin/env python
"""
Disease Prediction System - Diagnostic Script
Run this to identify and fix common issues
"""
import os
import sys
import subprocess
import importlib

def print_header(title):
    print("\n" + "="*50)
    print(f" {title}")
    print("="*50)

def print_status(message, status):
    status_symbol = "✅" if status else "❌"
    print(f"{status_symbol} {message}")

def check_python_version():
    print_header("Python Version Check")
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print_status("Python version is compatible", True)
        return True
    else:
        print_status("Python version is too old (need 3.7+)", False)
        return False

def check_packages():
    print_header("Package Installation Check")
    
    required_packages = [
        'django',
        'sklearn',
        'pandas', 
        'numpy',
        'joblib',
        'matplotlib',
        'crispy_forms'
    ]
    
    all_installed = True
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print_status(f"{package} is installed", True)
        except ImportError:
            print_status(f"{package} is NOT installed", False)
            all_installed = False
    
    return all_installed

def check_file_structure():
    print_header("File Structure Check")
    
    required_files = [
        'manage.py',
        'requirements.txt',
        'ml_models/train_models.py',
        'data/disease_symptom_dataset.csv',
        'predictor/models.py',
        'predictor/views.py',
        'predictor/forms.py'
    ]
    
    all_present = True
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print_status(f"{file_path} exists", True)
        else:
            print_status(f"{file_path} is MISSING", False)
            all_present = False
    
    return all_present

def check_ml_models():
    print_header("ML Models Check")
    
    model_files = [
        'ml_models/saved_models/random_forest_model.pkl',
        'ml_models/saved_models/knn_model.pkl',
        'ml_models/saved_models/gradient_boosting_model.pkl',
        'ml_models/saved_models/naive_bayes_model.pkl',
        'ml_models/saved_models/neural_network_model.pkl',
        'ml_models/saved_models/svm_model.pkl',
        'ml_models/saved_models/decision_tree_model.pkl',
        'ml_models/saved_models/label_encoder.pkl',
        'ml_models/saved_models/symptoms_list.pkl'
    ]
    
    models_exist = True
    
    for model_file in model_files:
        if os.path.exists(model_file):
            print_status(f"{os.path.basename(model_file)} exists", True)
        else:
            print_status(f"{os.path.basename(model_file)} is MISSING", False)
            models_exist = False
    
    return models_exist

def check_database():
    print_header("Database Check")
    
    try:
        # Set Django settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'disease_prediction_system.settings')
        
        import django
        django.setup()
        
        from django.core.management import execute_from_command_line
        
        # Check if migrations are needed
        result = subprocess.run([sys.executable, 'manage.py', 'showmigrations'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print_status("Database configuration is valid", True)
            return True
        else:
            print_status("Database has issues", False)
            return False
            
    except Exception as e:
        print_status(f"Database check failed: {e}", False)
        return False

def provide_solutions():
    print_header("Recommended Solutions")
    
    print("🔧 To fix missing packages:")
    print("   pip install -r requirements.txt")
    print("   or")
    print("   pip install Django scikit-learn pandas numpy joblib matplotlib django-crispy-forms crispy-bootstrap5")
    
    print("\n🤖 To train ML models:")
    print("   python ml_models/train_models.py")
    
    print("\n🗄️ To setup database:")
    print("   python manage.py makemigrations")
    print("   python manage.py migrate")
    
    print("\n🚀 To start the server:")
    print("   python manage.py runserver")
    print("   or")
    print("   python run_server.py")

def main():
    print_header("Disease Prediction System - Diagnostic Tool")
    print("This tool will check your system and identify any issues.")
    
    # Run all checks
    python_ok = check_python_version()
    packages_ok = check_packages()
    files_ok = check_file_structure()
    models_ok = check_ml_models()
    db_ok = check_database()
    
    # Summary
    print_header("Diagnostic Summary")
    
    all_good = python_ok and packages_ok and files_ok and models_ok and db_ok
    
    if all_good:
        print("🎉 All checks passed! Your system should work correctly.")
        print("\nTo start the server, run:")
        print("   python manage.py runserver")
        print("\nThen open: http://127.0.0.1:8000/")
    else:
        print("⚠️  Some issues were found. Please fix them using the solutions below.")
        provide_solutions()
    
    return all_good

if __name__ == "__main__":
    success = main()
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
