import requests
import spacy
import pandas as pd
from textblob import TextBlob 

# Function to calculate a risk score for a company based on news articles
def calculate_risk_score(company_name):
    nlp = spacy.load("en_core_web_sm")
    try:
        # Replace 'YOUR_API_KEY' with your actual News API key
        api_key = 'b41e3858a432466b92810434d12bab48'
        
        # Define the News API URL
        base_url = 'https://newsapi.org/v2/everything'
        
        # Specify your query parameters
        params = {
            'q': company_name,
            'apiKey': api_key
        }
        
        # Make a GET request to the News API
        response = requests.get(base_url, params=params)
        data = response.json()
    
        if response.status_code == 200:
            articles = data.get('articles', [])
            risk_keywords = [    "Lawsuit"
            "Scandal",
            "Controversy",
            "Financial crisis",
            "Fraud",
            "Regulatory violation",
            "Investigation",
            "Litigation",
            "Default",
            "Bankruptcy",
            "Mismanagement",
            "Misconduct",
            "Corruption",
            "Fine",
            "Ethical breach",
            "Data breach",
            "Security breach",
            "Privacy violation",
            "Environmental violation",
            "Product recall",
            "Safety issue",
            "Labor strike",
            "Supply chain disruption",
            "Market decline",
            "Reputation damage",
            "Shareholder activism",
            "Insider trading",
            "Economic downturn",
            "Antitrust",
            "Bribery"]  # Define risk-related keywords
            
            risk_score = 0
            
            for article in articles:
                text = article['title'] + ' ' + article['description']
                doc = nlp(text)
                
                # Perform sentiment analysis using TextBlob
                sentiment = TextBlob(text).sentiment.polarity
                
                # Check for risk-related keywords
                contains_risk_keyword = any(keyword in text.lower() for keyword in risk_keywords)
                
                # Calculate risk score for the article based on sentiment and keywords
                article_risk_score = sentiment + (1 if contains_risk_keyword else 0)
                
                risk_score += article_risk_score
            
            return risk_score

        else:
            print(f"Error fetching news: {data.get('message', 'Unknown error')}")
            return "Oops Data Not Found !!!"
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Oops Error Occurred !!!"
    
    