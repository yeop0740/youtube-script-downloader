from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qsl

def handler(event, context):
    url = event['url']
    parts = urlparse(url)
    query_string = dict(parse_qsl(parts.query))
    video_id = query_string['v']

    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    sentences = []
    for sentence in transcript:
        text= sentence['text'].replace('\n', ' ')
        sentences.append(text)
    result = ' '.join(sentences)
    return result.replace('. ', '.\n')
