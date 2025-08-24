from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
# Sample labeled training data: queries and their intents
def train_classifier():
    data = [
        ("find papers on machine learning?", "search"),
        ("search for recent AI articles?", "search"),
        ("lookup research about neural networks?", "search"),
        ("summarize the paper on reinforcement learning", "summarize"),
        ("give me a summary of the latest NLP research", "summarize"),
        ("can you summarize this article?", "summarize"),
        ("what is the main idea of this paper?", "answer"),
        ("how does this algorithm work?", "answer"),
        ("who wrote the paper on transformers?", "answer"),
        ("Can you find me papers on GNNS?", "search"),
        ("Can you help me find papers on blue whales?", "search"),
        ("Show me papers on prompt engineering", "search"),
        ("look up papers on graph summarization", "search"),
        ("find recent papers on deep learning", "search"),
        ("search for articles about quantum computing", "search"),
        ("lookup research papers on gene editing", "search"),
        ("show me papers about climate change", "search"),
        ("I want to find studies on vaccine efficacy", "search"),
        ("summarize the latest paper on natural language processing", "summarize"),
        ("give me a summary of the research on battery technology", "summarize"),
        ("can you summarize this document?", "summarize"),
        ("please provide a brief summary of that article", "summarize"),
        ("summarize the findings of the recent AI paper", "summarize"),
        ("what are the key points of that study?", "answer"),
        ("who wrote the article about blockchain?", "answer"),
        ("how does the proposed algorithm work?", "answer"),
        ("what methods were used in this research?", "answer"),
        ("why is this paper important for machine learning?", "answer"),
    ]

    # Split into inputs and labels
    texts, labels = zip(*data)

    # Split dataset into train/test for evaluation (optional)
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=42)

    # Create a pipeline: TF-IDF vectorizer + Logistic Regression classifier
    model = make_pipeline(TfidfVectorizer(), LogisticRegression())

    # Train the model
    model.fit(X_train, y_train)

    # Test the model
    y_pred = model.predict(X_test)

    # Print classification report
    print(classification_report(y_test, y_pred))

    save_model(model)

    test_classifier()
    # Example usage: classify new queries



def save_model(model):
    joblib.dump(model, 'intent_classifier.joblib')
    print("Model saved to intent_classifier.joblib")

def load_model():
    # Load the saved model
    model = joblib.load('Intent_classifier\\intent_classifier.joblib')
    print("Model loaded")
    return model





def test_classifier():
    model = load_model()

    # Try some queries
    queries = [
        "find latest papers on GPT models",
        "please summarize the AI article",
        "what is transfer learning?",
        "search for RoboCup papers"
    ]

    for q in queries:
        print(f"Query: {q}\nPredicted intent: {classify_intent_with_uncertainty(model, q)}\n")

def query_intent_classifier(user_input):
    model = load_model()
    
    return classify_intent_with_uncertainty(model, user_input)


def classify_intent_with_uncertainty(model, query, threshold=0.4):
    probas = model.predict_proba([query])[0]       # Probabilities for each class
    max_proba = max(probas)
    if max_proba < threshold:
        return "unknown"
    else:
        return model.classes_[probas.argmax()]

if __name__ == "__main__":
    train_classifier()