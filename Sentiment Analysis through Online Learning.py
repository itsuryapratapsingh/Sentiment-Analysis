
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

class OnlineSentimentAnalysis:
    def __init__(self):
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        compound_score = self.sentiment_analyzer.polarity_scores(text)['compound']

        if compound_score >= 0.05:
            return 'Positive'
        elif compound_score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    def online_learning(self, user_feedback, current_sentiment):
        # Update the sentiment analyzer based on user feedback
        if user_feedback == 'positive' and current_sentiment != 'Positive':
            self.sentiment_analyzer.lexicon['good'] += 1
        elif user_feedback == 'negative' and current_sentiment != 'Negative':
            self.sentiment_analyzer.lexicon['bad'] += 1

# Example usage
if __name__ == "__main__":
    online_sentiment_analysis = OnlineSentimentAnalysis()

    # Online learning loop
    for _ in range(5):
        user_input = input("Enter a sentence for sentiment analysis: ")
        current_sentiment = online_sentiment_analysis.analyze_sentiment(user_input)
        print(f"Predicted Sentiment: {current_sentiment}")

        user_feedback = input("Provide feedback (positive/negative/neutral): ").lower()
        online_sentiment_analysis.online_learning(user_feedback, current_sentiment)

    # Example of using the updated model
    new_user_input = input("Enter a new sentence for sentiment analysis: ")
    new_sentiment = online_sentiment_analysis.analyze_sentiment(new_user_input)
    print(f"Predicted Sentiment (after online learning): {new_sentiment}")

