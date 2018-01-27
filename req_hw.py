import requests
import os


def read_file(t_path):
    with open(t_path) as file:
        content = file.read()
    return content


def translate_it(source_path, source_lang, result_lang, result_path):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
     & key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [hint=<список вероятных языков текста>]
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param source_path: path to the file with the text for translation.
           source_lang: language of the text for translation.
           result_lang: language into which the text should be translated.
           result_path: path to the file with the translated text.
    :return: None.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'hint': source_lang,
        'lang': result_lang,
        'text': read_file(source_path)
    }
    response = requests.get(url, params=params).json()

    with open(result_path, "w+") as file:
        file.write(' '.join(response.get('text', [])))

    return

texts = ["DE.txt", "ES.txt", "FR.txt"]
result_texts = []

for text in texts:
    text_path = os.path.join(os.getcwd(), text)
    # print(text_path)
    result_path = os.path.join(os.getcwd(), "RU" + text)
    translate_it(text_path, ['de', 'es', 'fr'], 'ru', result_path)
    result_texts.append(result_path)

del_files = input("Print 'yes' if you want to delete files with translated texts: ")

if del_files == "yes":
    for result_text in result_texts:
        os.remove(result_text)
