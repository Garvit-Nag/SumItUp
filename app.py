import streamlit as st
from src.document_processor import process_document
from src.summarizer import TextSummarizer
import logging
from textblob import TextBlob  # Ensure this library is installed

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def main():
    # Streamlit app configuration
    st.set_page_config(
        page_title="SumItUp | Document Summarizer",
        page_icon="✍️",  # Or another icon that represents summarization
        layout="wide"
    )

    st.title("✍️ SumItUp")
    st.subheader("Intelligent Document Summarization Made Easy")

    # Sidebar for configuration
    st.sidebar.header("Summarization Settings")
    summary_length = st.sidebar.slider(
        "Summary Length",
        min_value=100,
        max_value=400,
        value=250
    )

    # Tabs for different input methods
    tab1, tab2 = st.tabs(["Paste Text", "Upload Document"])

    # Initialize summarizer
    summarizer = TextSummarizer()

    # Function to classify sentiment
    def classify_sentiment(polarity):
        if polarity > 0:
            return "Positive 😊"
        elif polarity < 0:
            return "Negative 😟"
        else:
            return "Neutral 😐"

    # Tab 1: Direct Text Input
    with tab1:
        st.header("Direct Text Input")
        text_input = st.text_area(
            "Paste your text here:",
            height=300,
            help="Enter the text you want to summarize"
        )

        if st.button("Summarize Text", key="text_summarize"):
            if text_input:
                with st.spinner('Generating summary and sentiment analysis...'):
                    try:
                        # Generate summary
                        summary = summarizer.generate_summary(
                            text_input,
                            max_length=summary_length,
                            min_length=summary_length // 2  # Optional: set min_length proportionally
                        )
                        st.subheader("Summary")
                        st.write(summary)

                        # Perform sentiment analysis
                        if text_input.strip():
                            sentiment = TextBlob(text_input).sentiment
                            sentiment_class = classify_sentiment(sentiment.polarity)
                            st.subheader("Sentiment Analysis")
                            st.write(f"Sentiment: {sentiment_class}")
                            st.write(f"Polarity: {sentiment.polarity:.2f} (Range: -1 to 1)")
                            st.write(f"Subjectivity: {sentiment.subjectivity:.2f} (Range: 0 to 1)")
                        else:
                            st.warning("No valid text for sentiment analysis.")

                    except Exception as e:
                        st.error(f"Summarization failed: {e}")
            else:
                st.warning("Please enter some text to summarize.")

    # Tab 2: Document Upload
    with tab2:
        st.header("Document Upload")
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['txt', 'pdf', 'docx'],
            help="Upload a text, PDF, or Word document"
        )

        if uploaded_file is not None:
            if st.button("Summarize Document", key="doc_summarize"):
                with st.spinner('Processing, summarizing, and analyzing sentiment...'):
                    try:
                        # Process document
                        document_text = process_document(uploaded_file)

                        # Generate summary
                        summary = summarizer.generate_summary(
                            document_text,
                            max_length=summary_length,
                            min_length=summary_length // 2  # Optional: set min_length proportionally
                        )
                        st.subheader("Summary")
                        st.write(summary)

                        # Perform sentiment analysis
                        if document_text.strip():
                            sentiment = TextBlob(document_text).sentiment
                            sentiment_class = classify_sentiment(sentiment.polarity)
                            st.subheader("Sentiment Analysis")
                            st.write(f"Sentiment: {sentiment_class}")
                            st.write(f"Polarity: {sentiment.polarity:.2f} (Range: -1 to 1)")
                            st.write(f"Subjectivity: {sentiment.subjectivity:.2f} (Range: 0 to 1)")
                        else:
                            st.warning("No valid text for sentiment analysis.")

                    except Exception as e:
                        st.error(f"Error processing document: {e}")


if __name__ == "__main__":
    main()
