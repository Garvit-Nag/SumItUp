import os
# Set environment variables before importing transformers
os.environ['TRANSFORMERS_OFFLINE'] = '1'
os.environ['HF_HUB_DISABLE_TELEMETRY'] = '1'

import torch
from transformers import pipeline

class TextSummarizer:
    def __init__(self, model_name="google/pegasus-xsum"):
        """
        Initialize summarization pipeline with robust error handling
        """
        try:
            # Explicitly use CPU
            self.summarizer = pipeline(
                "summarization", 
                model=model_name, 
                device=-1  # Force CPU usage
            )
        except Exception as e:
            print(f"Model Loading Error: {e}")
            raise RuntimeError(f"Failed to load summarization model: {e}")
    
    def generate_summary(self, text, max_length=150, min_length=50):
        try:
            # More robust input validation
            if not text or len(text.strip()) == 0:
                return "No text provided for summarization."
            
            # Truncate very long texts to prevent memory issues
            text = text[:1024]
            
            # Generate summary
            summary = self.summarizer(
                text, 
                max_length=max_length, 
                min_length=min_length, 
                do_sample=False
            )[0]['summary_text']
            
            return summary
        
        except Exception as e:
            print(f"Summarization Error: {e}")
            return f"Error during summarization: {e}"
