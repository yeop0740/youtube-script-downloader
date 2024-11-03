from youtube_transcript_api import YouTubeTranscriptApi

video_id = '0_jfH6qijVY'
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

sentences = []
for sentence in transcript:
    text= sentence['text'].replace('\n', ' ')
    sentences.append(text)
result = ' '.join(sentences)
print('senteces:', result.replace('. ', '.\n'))
