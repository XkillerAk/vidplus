from static.images.YTsearch import youtube_search
from Extraction import raw_comments
from DataAnalyse import clean_comments, get_sentiment_scores
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def collected_list():
    query = request.form.get('query', '')
    videos = youtube_search(query)

    raw_list = []
    def hello():
        for video in videos:
            raw_list.append(video)
            print(video['video_id'])

        return raw_list
    
    raw_list = hello()

    video_ids = [video['video_id'] for video in raw_list]
    print(f"Video IDs: {video_ids}")

    comments = raw_comments(video_ids)
    print(f"Total comments: {len(comments)}")

    cleaned_comments = clean_comments(comments)
    positive_scores, negative_scores = get_sentiment_scores(cleaned_comments)

  
    videos_data = list(zip(video_ids, comments, positive_scores, negative_scores))

    
    videos_data = [video for video in videos_data if video[1]]  

    
    sorted_videos = sorted(videos_data, key=lambda x: x[2], reverse=True)

    for video in sorted_videos:
        print(f"Video ID: {video[0]}")
        print(f"Positive Score: {video[2]}")
        print(f"Negative Score: {video[3]}")
        print("---------")
    
    
    last_selected_videos = [video[0] for video in sorted_videos]

    return render_template('index.html', results=last_selected_videos)

    print(f"Last Selected Video IDs: {last_selected_videos}")

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
