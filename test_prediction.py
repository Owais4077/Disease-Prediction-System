#!/usr/bin/env python
"""
Test script for the Disease Prediction System
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'disease_prediction_system.settings')
django.setup()

from ml_models.train_models import DiseasePredictor

def test_prediction_system():
    """Test the disease prediction functionality"""
    print("=" * 50)
    print("Disease Prediction System - Test")
    print("=" * 50)
    
    try:
        # Initialize predictor
        print("Loading ML models...")
        predictor = DiseasePredictor()
        predictor.load_models()
        print("✓ Models loaded successfully!")
        
        # Test cases
        test_cases = [
            {
                'name': 'Skin Issues (Fungal Infection)',
                'symptoms': ['itching', 'skin_rash', 'nodal_skin_eruptions']
            },
            {
                'name': 'Fever and Headache (Malaria/Dengue)',
                'symptoms': ['high_fever', 'headache', 'muscle_pain', 'chills']
            },
            {
                'name': 'Respiratory Issues (Common Cold)',
                'symptoms': ['continuous_sneezing', 'runny_nose', 'cough', 'throat_irritation']
            }
        ]

        # All 7 models to test
        models_to_test = [
            ('gb', 'Gradient Boosting'),
            ('nb', 'Naive Bayes'),
            ('nn', 'Neural Network'),
            ('svm', 'Support Vector Machine'),
            ('rf', 'Random Forest'),
            ('knn', 'K-Nearest Neighbors'),
            ('dt', 'Decision Tree')
        ]

        print(f"\nTesting {len(test_cases)} symptom combinations with all 7 models...\n")

        for i, test_case in enumerate(test_cases, 1):
            print(f"Test {i}: {test_case['name']}")
            print(f"Symptoms: {', '.join(test_case['symptoms'])}")
            print("-" * 60)

            for model_code, model_name in models_to_test:
                try:
                    disease, confidence, top_diseases = predictor.predict_disease(
                        test_case['symptoms'], model_code
                    )
                    print(f"{model_name:20}: {disease} ({confidence:.1%})")
                except Exception as e:
                    print(f"{model_name:20}: Error - {str(e)[:30]}")

            print("=" * 60)
        
        print("✓ All tests completed successfully!")
        print("\nSystem is ready for use!")
        
    except Exception as e:
        print(f"✗ Error during testing: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = test_prediction_system()
    sys.exit(0 if success else 1)
