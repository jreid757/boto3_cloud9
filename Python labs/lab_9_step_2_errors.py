# Standard Imports
import argparse
import json

# 3rd Party Imports
import boto3

# Arguments
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True
    )

args = parser.parse_args()
import argparse
import json
import boto3

parser = argparse.ArgumentParser(description="Provides translation between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid JSON.",
    required=True
)

args = parser.parse_args()

def open_input():
    try:
        with open(args.filename) as file_object:
            contents = json.load(file_object)
            return contents['Input']
    except Exception as e:
        print(f"Error opening the input file: {e}")
        return None

def translate_text(**kwargs):
    try:
        client = boto3.client('translate')
        response = client.translate_text(**kwargs)
        print(response['TranslatedText'])
    except Exception as e:
        print(f"Error translating the text: {e}")

def translate_loop():
    input_text = open_input()
    if input_text is not None:
        for item in input_text:
            if input_validation(item):
                try:
                    translate_text(**item)
                except SystemError:
                    print("Error during translation")
            else:
                print("Invalid input item")

def input_validation(item):
    languages = ["af", "sq", "am", "ar", "az", "bn", "bs", "bg", "zh", "zh-TW", "hr", "cs", "da", "fa-AF",
                 "nl", "en", "et", "fi", "fr", "fr-CA", "ka", "de", "el", "ha", "he", "hi", "hu", "id", "it",
                 "ja", "ko", "lv", "ms", "no", "fa", "ps", "pl", "pt", "ro", "ru", "sr", "sk", "sl", "so", "es",
                 "sw", "sv", "tl", "ta", "th", "tr", "uk", "ur", "vi"
                 ]
    try:
        json_input = item
        SourceLanguageCode = json_input['SourceLanguageCode']
        TargetLanguageCode = json_input['TargetLanguageCode']

        if SourceLanguageCode == TargetLanguageCode:
            print("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
            return False
        elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
            print("Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
            return False
        elif SourceLanguageCode not in languages:
            print("The SourceLanguageCode is not valid - stopping")
            return False
        elif TargetLanguageCode not in languages:
            print("The TargetLanguageCode is not valid - stopping")
            return False
        elif SourceLanguageCode in languages and TargetLanguageCode in languages:
            print("The SourceLanguageCode and TargetLanguageCode are valid - proceeding")
            return True
        else:
            print("There is an issue")
            return False
    except Exception as e:
        print(f"Error during input validation: {e}")
        return False

def main():
    try:
        translate_loop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
