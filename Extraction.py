
import googleapiclient.discovery
from googleapiclient.errors import HttpError

api_key = 'AIzaSyDTt8htsSBXUU9V_xEWlF-ansYfr13Y1bw'

def raw_comments(video_ids):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    comments = []
    for video_id in video_ids:
        try:
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                maxResults=1
            ).execute()

            if not response['items']:
                print(f"Comments are disabled for video with ID: {video_id}. Skipping...")
                continue

            next_page_token = None
            while True:
                response = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    textFormat='plainText',
                    pageToken=next_page_token,
                    maxResults=100
                ).execute()

                for item in response['items']:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    comments.append(comment)

                next_page_token = response.get('nextPageToken')
                if not next_page_token:
                    break
        except HttpError as e:
            if e.resp.status == 403 and "commentsDisabled" in str(e):
                print(f"Comments are disabled for video with ID: {video_id}. Skipping...")
            else:
                print(f"An error occurred while fetching comments for video with ID: {video_id}")
                print(f"Error details: {str(e)}")

    return comments


#video_ids = ['ohc7o8sZFxs', 'WPmW5FiEQHw', '-h8Swyz8Ovs', 'WOk7LgzJjVo', 'h64QUZTM9hc']
#all_comments = extract_comments(video_ids)
#print(all_comments)





