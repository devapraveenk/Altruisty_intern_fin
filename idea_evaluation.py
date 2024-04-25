from html import entities
import streamlit as st
from pydoc import text
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
from collections import Counter
import numpy as np
import en_core_web_sm

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# Initialize spaCy model (choose a suitable model for your needs)
nlp = en_core_web_sm.load()

# Initialize NLTK sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Initialize NLTK lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to preprocess text
def preprocess_text(text):
    # Tokenization and normalization
    tokens = nltk.word_tokenize(text.lower())
    # Lemmatization
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    # Stop word removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

# Function to evaluate research depth
def evaluate_research(analysis_result):
    research_parameters = [
        analysis_result["problem"],
        analysis_result["target_audience"],
        analysis_result["solution_type"],
        analysis_result["technical_feasibility"],
        analysis_result["market_research"],
        analysis_result["monetization_strategy"],
        analysis_result["scalability_potential"],
        analysis_result["user_passion"]
    ]
    total_parameters = len(research_parameters)
    met_parameters = sum(param is not None for param in research_parameters)
    research_percentage = (met_parameters / total_parameters) * 100

    if research_percentage <= 30:
        return "Minimal Research"
    elif research_percentage <= 60:
        return "Intermediate Research"
    else:
        return "Strategized Research"

# Function to analyze user idea
def analyze_idea(text):
    # Preprocess text
    preprocessed_text = preprocess_text(text)
    
    # Use spaCy for entity recognition
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Identify themes
    theme_counter = Counter(preprocessed_text)
    most_common_themes = theme_counter.most_common(10)
    themes = [term for term, _ in most_common_themes]

    # Initialize parameters
    problem = None
    target_audience = None
    solution_type = None
    technical_feasibility = None
    monetization_strategy = None
    scalability_potential = None
    user_passion = None
    market_research = None
    competitor_analysis = None


    # Define keywords and phrases for parameters
    problem_keywords = ["problem", "issue", "challenge", "pain point", "opportunity"]
    target_audience_keywords = ["target audience","user", "customer", "audience","consumer","demographic","community"]
    solution_type_keywords = ["app", "website", "service", "product", "platform", "solution", "technology", "platform"]
    technical_feasibility_keywords = ["existing technology", "feasible", "implementable","not feasible","high expenditure","high cost"]
    monetization_keywords = ["subscription", "advertising", "in-app purchase", "monetization"]
    scalability_keywords = ["scalable", "growth", "expand", "potential"]
    competitor_keywords = ["competitor", "rival", "existing solution"]
    market_analysis_keywords = ["market size", "market research", "target market", "demographic"]
    user_passion_keywords = ["Excited","Committed","Passionate","Vision","Dream","Motivated","Optimistic" ]

    # Analyze entities and text for parameters
    for ent in entities:
        if ent[0] in ("problem", "issue", "challenge"):
            problem = ent[0]
        elif ent[0] in ("user", "customer", "audience"):
            target_audience = ent[0]
        elif ent[0] in ("app", "website", "service"):
            solution_type = ent[0]
        elif ent[0] in ("existing technology", "feasible", "implementable","not feasible","high expenditure","high cost"):
            technical_feasibility = ent[0]
        elif ent[0] in ("subscription", "advertising", "in-app purchase", "monetization"):
            monetization_strategy = ent[0]
        elif ent[0] in ("scalable", "growth", "expand", "potential"):
            scalability_potential = ent[0]
        elif ent[0] in ("competitor", "rival", "existing solution"):
            competitor_analysis = ent[0]
        elif ent[0] in ("market size", "market research", "target market", "demographic"):
            market_research = ent[0]
        elif ent[0] in ("Excited","Committed","Passionate","Vision","Dream","Motivated","Optimistic"):
            user_passion = ent[0]    
        
    for token in preprocessed_text:
        if token in problem_keywords:
            problem = "Problem Identified"
        elif token in target_audience_keywords:
            target_audience = "Have Researched On Target Audience"
        elif token in solution_type_keywords:
            solution_type = "Solution Type Identified"
        elif token in technical_feasibility_keywords:
            technical_feasibility = "Feasibility Mentioned"    
        elif token in monetization_keywords:
            monetization_strategy = "Potential"
        elif token in scalability_keywords:
            scalability_potential = "Potential"
        elif any(keyword in token for keyword in competitor_keywords):
            competitor_analysis = "Researched"
        elif any(keyword in token for keyword in market_analysis_keywords):
            market_research = "Analyzed"


    technical_feasibility_keywords = ["existing technology", "feasible", "implementable"]
    for token in preprocessed_text:
        if token in technical_feasibility_keywords:
            technical_feasibility = "Possible"

    technical_feasibility_keywords = ["not feasible", "high expenditure", "high cost"]
    for token in preprocessed_text:
        if token in technical_feasibility_keywords:
            technical_feasibility = "Should think about an alternative"

    # Perform sentiment analysis using NLTK VADER
    sentiment_scores = sentiment_analyzer.polarity_scores(text)
    sentiment_score = sentiment_scores['compound']

    # Analyze sentiment score for potential indication of user passion
    if sentiment_score > 0.5:  # Adjust threshold as needed
        user_passion = "High"
    else:
        user_passion = "Moderate"

    # Further inputs
    further_inputs = []
    if problem is None:
        further_inputs.append("Clearly define the problem your idea addresses.")
    if solution_type is None:
        further_inputs.append("Clearly define the solution type for your idea.")    
    if target_audience is None:
        further_inputs.append("Identify your target audience and their needs.")
    if technical_feasibility is None:
        further_inputs.append("Clarify the technical feasibility of your idea.")
    if monetization_strategy is None:
        further_inputs.append("Determine a potential monetization strategy.")
    if scalability_potential is None:
        further_inputs.append("Consider the scalability potential of your idea.")
    if market_research is None:
        further_inputs.append("Conduct market research to validate your idea.")
    if competitor_analysis is None:
        further_inputs.append("Analyze competitors in the market.")
    
    # Evaluate research depth
    research_evaluation = evaluate_research({
        "problem": problem,
        "solution_type": solution_type,
        "target_audience": target_audience,
        "technical_feasibility": technical_feasibility,
        "market_research": market_research,
        "monetization_strategy": monetization_strategy,
        "scalability_potential": scalability_potential,
        "user_passion": user_passion
    })

    # Return analysis results
    return {
        "research_depth": research_evaluation,
        "further_inputs": further_inputs,
        "problem": problem,
        "target_audience": target_audience,
        "solution_type": solution_type,
        "technical_feasibility": technical_feasibility,
        "monetization_strategy": monetization_strategy,
        "scalability_potential": scalability_potential,
        "competitor_analysis": competitor_analysis,
        "market_research": market_research,
        "user_passion": user_passion,
        "sentiment_score": sentiment_score,
        "identified_entities": entities,
        "potential_themes": themes
    }
# Analyze the user's idea
# analysis_result = analyze_idea(user_idea)

# # Display research depth
# print(f"Research Depth: {analysis_result['research_depth']}")

# # Display further inputs required
# print(f"Further Inputs:")
# for input_text in analysis_result["further_inputs"]:
#     print(f"- {input_text}")

# # Display other analysis results
# print("Analysis Results:")
# print(f"Problem: {analysis_result['problem']}")
# print(f"Target Audience: {analysis_result['target_audience']}")
# print(f"Solution Type: {analysis_result['solution_type']}")
# print(f"Technical Feasibility: {analysis_result['technical_feasibility']}")
# print(f"Monetization Strategy: {analysis_result['monetization_strategy']}")
# print(f"Scalability Potential: {analysis_result['scalability_potential']}")
# print(f"Competitor Analysis: {analysis_result['competitor_analysis']}")
# print(f"Market Research: {analysis_result['market_research']}")
# print(f"User Passion: {analysis_result['user_passion']}")
# print(f"Sentiment Score: {analysis_result['sentiment_score']}")
# print(f"Identified Entities: {analysis_result['identified_entities']}")
# print(f"Potential Themes: {analysis_result['potential_themes']}")



def idea():
    st.title("Altruisty Idea Evaluation Tool")
    st.write("Click the button below to start interacting with the tool.")
    
    if st.button("Start Evaluation"):
        # Use a unique key for the text_input widget
        user_idea = st.text_input("Please explain your startup idea in a maximum of 300 words:", key="user_idea_input")

        if user_idea:
            analysis_result = analyze_idea(user_idea)

            st.write(f"Research Depth: {analysis_result['research_depth']}")

            st.write("Analysis Results:")
            st.write(f"Problem: {analysis_result['problem']}")
            st.write(f"Target Audience: {analysis_result['target_audience']}")
            st.write(f"Solution Type: {analysis_result['solution_type']}")
            st.write(f"Technical Feasibility: {analysis_result['technical_feasibility']}")
            st.write(f"Monetization Strategy: {analysis_result['monetization_strategy']}")
            st.write(f"Scalability Potential: {analysis_result['scalability_potential']}")
            st.write(f"Competitor Analysis: {analysis_result['competitor_analysis']}")
            st.write(f"Market Research: {analysis_result['market_research']}")
            st.write(f"User Passion: {analysis_result['user_passion']}")
            st.write(f"Sentiment Score: {analysis_result['sentiment_score']}")
            st.write(f"Identified Entities: {analysis_result['identified_entities']}")
            st.write(f"Potential Themes: {analysis_result['potential_themes']}")
