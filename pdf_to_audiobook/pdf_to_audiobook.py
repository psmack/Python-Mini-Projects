""" Convert PDF to audio
This script uses pyMuPDF (fitz) to get text from PDF and uses gTTS
to convert text to audio file.

Dependencies:
    pip install gtts
    pip install pyMuPDF
"""
from gtts import gTTS
import os
import sys
import fitz


def pdf_to_text(filename):
    """
    Convert PDF to text string.

    Args:
        filename: PDF filepath

    Returns:
        text: Text content of PDF file
    """

    text = ""

    try:
        print("[Status] Converting PDF to text ...")
        doc = fitz.open(filename)
        for page in doc:
            text += page.get_text()

    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)

    return text


def text_to_audio(text_content, pdf_file):
    """
    Convert text string to audio using gTTS and save as .mp3.

    Args:
        text_content: String content of PDF file
        pdf_file: Filename 

    """

    out_file, ext = os.path.splitext(pdf_file)

    try:
        print("[Status] Converting text to audio ...")
        audio = gTTS(text=text_content, lang="en", slow=False)
        print(f"[Status] Saving {out_file}.mp3 ...")
        audio.save(f"{out_file}.mp3")
    except (OSError, UnicodeDecodeError, ConnectionError) as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    pdf_file = input("Enter the file path of PDF (Ex: 'sample_pdf\sample.pdf'): ")
    text = pdf_to_text(pdf_file)
    text_to_audio(text, pdf_file)
    print("Completed!")


if __name__ == "__main__":
    main()
