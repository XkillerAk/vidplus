from textblob import TextBlob

def clean_comments(comments):
    
    cleaned_comments = []
    for comment in comments:
       
        cleaned_comments.append(comment)

    return cleaned_comments

def get_sentiment_scores(comments):
    positive_scores = []
    negative_scores = []
    for comment in comments:
        blob = TextBlob(comment)
        sentiment_score = blob.sentiment.polarity

        if sentiment_score > 0:
            positive_scores.append(sentiment_score)
        elif sentiment_score < 0:
            negative_scores.append(sentiment_score)

    return positive_scores, negative_scores


