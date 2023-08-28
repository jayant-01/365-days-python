#language detection

from langdetect import detect

def detect_language(text):
    return detect(text)

if __name__ == "__main__":
    text = input("Enter text: ")
    print(detect_language(text))
