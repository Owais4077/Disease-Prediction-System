# Disease Prediction System

A Django-based machine learning web application that predicts diseases based on user-input symptoms using advanced ML algorithms.

**Developed by: OWAIS AHMAD**
**Field: Data Science**
**Expertise: Machine Learning & AI Solutions**

## Features

- **7 AI-Powered Models**: Choose from Random Forest, Gradient Boosting, SVM, Neural Network, Naive Bayes, KNN, and Decision Tree
- **Interactive Web Interface**: User-friendly symptom selection with Bootstrap 5
- **High Accuracy**: Best models achieve 100% accuracy on test data
- **Confidence Scores**: Get prediction confidence levels and top 3 disease predictions
- **Prediction History**: Track your previous predictions
- **Responsive Design**: Works on desktop and mobile devices
- **Admin Interface**: Manage symptoms, diseases, and view prediction analytics
- **Model Comparison**: Compare predictions across different algorithms

## Technology Stack

### Backend
- **Django 5.2**: Web framework
- **Python 3.13**: Programming language
- **Scikit-learn**: Machine learning library
- **Pandas & NumPy**: Data manipulation and analysis
- **Joblib**: Model serialization

### Frontend
- **Bootstrap 5**: CSS framework
- **Font Awesome**: Icons
- **Django Crispy Forms**: Enhanced form rendering
- **JavaScript**: Interactive features

### Machine Learning
- **7 Advanced Models**: Gradient Boosting (100%), Neural Network (100%), Naive Bayes (100%), SVM (92.9%), Random Forest (85.7%), KNN (42.9%), Decision Tree (7.1%)
- **Best Performance**: Multiple models achieving 100% accuracy
- **82+ Symptoms**: Comprehensive symptom database
- **24+ Diseases**: Wide range of disease predictions
- **Model Comparison**: Test different algorithms for the same symptoms

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd disease-prediction-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Train ML models** (if not already trained)
   ```bash
   python ml_models/train_models.py
   ```

5. **Create superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main app: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

1. **Select Symptoms**: Choose from the comprehensive list of symptoms you're experiencing
2. **Choose ML Model**: Select from 7 different algorithms (Gradient Boosting recommended)
3. **Get Prediction**: Click "Predict Disease" to get AI-powered results
4. **View Results**: See the predicted disease with confidence score and top 3 predictions
5. **Compare Models**: Try different algorithms to compare predictions
6. **Check History**: View your previous predictions in the history section

## Project Structure

```
disease_prediction_system/
├── data/                          # Dataset files
│   └── disease_symptom_dataset.csv
├── ml_models/                     # Machine learning components
│   ├── saved_models/             # Trained model files
│   └── train_models.py           # Model training script
├── predictor/                     # Main Django app
│   ├── templates/                # HTML templates
│   ├── models.py                 # Database models
│   ├── views.py                  # View logic
│   ├── forms.py                  # Form definitions
│   ├── urls.py                   # URL patterns
│   └── admin.py                  # Admin configuration
├── disease_prediction_system/     # Django project settings
├── manage.py                     # Django management script
└── requirements.txt              # Python dependencies
```

## Dataset Information

- **24+ Diseases**: Including Diabetes, Hypertension, Malaria, Dengue, Tuberculosis, etc.
- **82+ Symptoms**: Comprehensive symptom coverage
- **66+ Training Samples**: Balanced dataset for accurate predictions
- **Binary Encoding**: Symptoms encoded as binary features for ML processing

## Model Performance

- **Gradient Boosting**: 100% accuracy (Best performing model)
- **Naive Bayes**: 100% accuracy (Excellent for probabilistic classification)
- **Neural Network**: 100% accuracy (Deep learning approach)
- **Support Vector Machine**: 92.9% accuracy (Effective in high dimensions)
- **Random Forest**: 85.7% accuracy (Robust ensemble method)
- **K-Nearest Neighbors**: 42.9% accuracy (Simple pattern recognition)
- **Decision Tree**: 7.1% accuracy (Basic tree-based approach)
- **Cross-validation**: Models evaluated using train-test split
- **Confidence Scores**: Probability-based confidence metrics

## API Endpoints

- `/` - Home page with symptom selection form
- `/predict/` - Disease prediction endpoint
- `/history/` - Prediction history
- `/about/` - System information
- `/admin/` - Django admin interface

## Important Disclaimer

⚠️ **Medical Disclaimer**: This system is for educational and research purposes only. The predictions should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is for educational purposes. Please ensure proper attribution when using or modifying the code.

## Support

For issues or questions, please create an issue in the repository or contact the development team.

---

**Built with ❤️ using Django and Machine Learning**
