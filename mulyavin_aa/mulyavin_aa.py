from transformers import pipeline

LANGS = ['ru', 'en']


def print_hi() -> None:
    print('''Hello User! Let's go to translate!!!''')

    from_lang = input('Введите исходный язык (en, ru): ').lower()
    to_lang = input('Введите требуемый язык (en, ru): ').lower()

    if not from_lang:
        print('Исходный язык не указан!')
        return

    if not to_lang:
        print('Требуемый язык не указан!')
        return

    if from_lang not in LANGS:
        print(f'Язык {from_lang} не поддерживается')
        return

    if to_lang not in LANGS:
        print(f'Язык {to_lang} не поддерживается')
        return

    if from_lang == to_lang:
        print('Меня не обманищЪ!')
        return

    pipe = pipeline("translation", model=f'Helsinki-NLP/opus-mt-{from_lang}-{to_lang}')

    while True:
        print('*' * 20)
        input_str = input(f'Введите текст на языке {from_lang}: ')
        if not input_str:
            break
        output_str_list = pipe(input_str)
        if not output_str_list:
            print('Не удалось перевести')
            break

        print('--> Результат перевода:')
        for out in output_str_list:
            print('\t', out['translation_text'])


if __name__ == '__main__':
    print_hi()
