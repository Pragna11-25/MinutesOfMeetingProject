from transformers import pipeline

def get_text_summarization(text):
  print("summarization_pipeline started ")
  summarization_pipeline = pipeline("summarization")
  summary = summarization_pipeline(text,min_length=5,
                                   do_sample=False, truncation=True)
  print("summarization_pipeline : ended ")
  print("summarization_pipeline : " +  summary[0]['summary_text'])
  return summary[0]['summary_text']