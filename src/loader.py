from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from urllib.parse import urlparse, parse_qs

def extract_video_id(url:str)->str:
    """
    Extract the video ID from a YouTube URL.
    """

    parsed_url = urlparse(url)

    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path.lstrip("/").split("?")[0]
    
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        qs = parse_qs(parsed_url.query)
        if "v" in qs:
            return qs["v"][0]
        
    raise ValueError("Invalid YouTube URL")


def get_transcript(url:str)->str:
    """
    Fetches the full transcript of a YouTube video as a single string.
    Raises a clear error if transcript is unavailable.
    """
    video_id = extract_video_id(url)

    try:
        yt_api = YouTubeTranscriptApi()
        transcriptList = yt_api.fetch(video_id)

        # full_transcript = " ".join(entry["text"] for entry in transcriptList)
        full_transcript = " ".join(entry.text for entry in transcriptList)
        return full_transcript
    
    except TranscriptsDisabled:
        raise RuntimeError("Transcripts are disabled for this video.")

    except NoTranscriptFound:
        raise RuntimeError("No transcript found. The video may not have captions.")

    except Exception as e:
        raise RuntimeError(f"Unexpected error fetching transcript: {e}")
