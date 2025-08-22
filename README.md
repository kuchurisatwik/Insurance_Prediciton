# Insurance Prediction API

## My Journey into ML and FastAPI 

This project marks my exciting first steps into the world of Machine Learning and API development! I was genuinely curious about how to build a predictive model and connect it to real-world API endpoints that could give users personalized responses.

## What This Project Taught Me

Through building this insurance prediction microservice, I discovered the beauty of combining two powerful technologies:

- **Machine Learning**: Training models to predict insurance costs based on user data
- **FastAPI**: Creating lightning-fast API endpoints that serve predictions in real-time

The experience of watching ML and FastAPI work together seamlessly was incredibly rewarding. It opened my eyes to the multidisciplinary nature of modern software development - where data science meets web development!

## What It Does

This API predicts insurance premiums based on user characteristics like:
- Age
- BMI
- Number of dependents
- Smoking status
- Region
- And more!

Simply send a POST request with user data, and get back a personalized insurance cost prediction.

## Tech Stack

- **Python** - The backbone of everything
- **FastAPI** - For blazingly fast API endpoints
- **Machine Learning** - Predictive modeling (likely scikit-learn)
- **Pandas & NumPy** - Data processing and manipulation

## Why I Built This

As someone curious about both ML and API development, I wanted to bridge the gap between training a model and actually serving it to users. This project taught me valuable skills in:

- Data preprocessing and feature engineering
- Model training and evaluation  
- API design and development
- Connecting ML models to web services
- Real-world application deployment

## What's Next?

This project has sparked my passion for exploring FastAPI to an even greater extent! I'm excited to:
- Build more complex ML-powered APIs
- Explore advanced FastAPI features
- Dive deeper into MLOps and model deployment
- Create more user-friendly interfaces

## Getting Started

```CMD
# Clone the repository
git clone https://github.com/kuchurisatwik/Insurance_Prediction.git

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` to explore the interactive API documentation!





