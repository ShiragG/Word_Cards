from googletrans import Translator
import keyboard
import clipboard

def translate():
    text = clipboard.paste()
    translator = Translator()
    print(f'Text: {text} \nTranslate..')
    translated = translator.translate(text, dest='ru')
    print(translated.text)

def main():
    keyboard.add_hotkey('ctrl+alt+x',translate)
    while True:
        pass

if __name__ == '__main__':
    main()
