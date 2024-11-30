from transformers import pipeline
class TextSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        """
        Initialize summarization pipeline
        
        Args:
            model_name (str): Hugging Face model for summarization
        """
        try:
            self.summarizer = pipeline("summarization", model=model_name)
        except Exception as e:
            raise RuntimeError(f"Failed to load summarization model: {e}")
    
    def generate_summary(self, text, max_length=400, min_length=100):
        """
        Generate summary for given text
        
        Args:
            text (str): Input text to summarize
            max_length (int): Maximum length of summary
            min_length (int): Minimum length of summary
        
        Returns:
            str: Generated summary
        """
        try:
            # Validate input text
            if not text or len(text.strip()) == 0:
                return "No text provided for summarization."
            
            # Ensure min_length is less than max_length
            min_length = min(min_length, max_length)
            
            # Generate summary
            summary = self.summarizer(
                text, 
                max_length=max_length, 
                min_length=min_length, 
                do_sample=False
            )[0]['summary_text']
            
            return summary
        
        except Exception as e:
            return f"Error during summarization: {e}"
