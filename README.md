# Text Sentiment Annotator

This Python project provides a graphical user interface (GUI) for annotating research paper sentences based on multiple sentiment layers. It allows the user to classify sentences from a text document into categories like sentiment polarity, section aspects, subjective polarity, and major comments.

## Features
- **Sentence Tokenization**: The program tokenizes the input text into sentences for classification.
- **Four Sentiment Layers**:
  1. **Sentiment Layer**: Classifies sentences as Positive, Introspective, Summary, or Yes.
  2. **Section Aspect**: Identifies the section of the research paper (e.g., Introduction, Related Work, Experiments, etc.).
  3. **Subjective Polarity**: Classifies sentences into Summary, Suggestion, Deficit, Appreciation, Discussion, or Question.
  4. **Major Comment**: Allows users to mark comments as Major or Not.
- **User Interface**: A GUI built with `wxPython` for intuitive sentence classification.
- **Annotations**: After classification, the sentences are annotated with the user's choices and saved into a new text file.

## Requirements
- Python 3.x
- `wxPython` (for GUI)
- `nltk` (for text tokenization)
