from celery import current_app as celery
import time
import text_summariser as ts
import whisper

@celery.task(bind=True)
def process_audio(self, file_path, filename):

    audio_path = filename
    self.update_state(state='STARTED', meta={'info': 'Processing the File.', 'audio_path': filename, 'audio_filename': filename})
    time.sleep(10)

    model = whisper.load_model("base")
    print("File path : " + file_path)
    result = model.transcribe(file_path)
    text = result['text']
    print("text from transcription : "+text )
    print("filename: "+filename)

    try:

        self.update_state(state='PROGRESS', meta={'info': 'Text extracted, Summarizing now.', 'audio_path': audio_path, 'audio_filename': filename})
        time.sleep(10)

        minutes_of_meeting = meeting_minutes(text)

        self.update_state(state='SUCCESS', meta={'info': 'Summary Ready.', 'summary': minutes_of_meeting, 'audio_path': audio_path, 'audio_filename': filename})
        time.sleep(10000)
        return minutes_of_meeting
    except Exception as e:
        print("Exception: ", e)

def meeting_minutes(transcription):
    abstract_summary = ts.get_text_summarization(transcription)
    return abstract_summary