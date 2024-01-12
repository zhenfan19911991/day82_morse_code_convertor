import requests

morse_trans = requests.get("https://api.npoint.io/388fc09ed21e9c759c38")
morse_trans = morse_trans.json()

guess = True

while guess:
    give_input = input('What is the text to translate?')

    text_to_translate = give_input.upper()
    text_to_translate_list = text_to_translate.split()

    morse_translation_all = ""
    for index1, word in enumerate(text_to_translate_list):
        morse_translation_word = ""
        for index, letter in enumerate(word):
            morse_code = morse_trans[letter]
            if index < len(word) - 1:
                morse_code = morse_code + ' '
            morse_translation_word = morse_translation_word+morse_code
        if index1 < len(text_to_translate_list)-1:
            morse_translation_word = morse_translation_word + ' / '
        morse_translation_all = morse_translation_all + morse_translation_word


    print(f'The translated morse code of "{give_input}" is: "{morse_translation_all}"')
    ask = input('Do you want to translate another word? [y/n]')
    if ask.lower() == 'y':
        guess = True
    else:
        print('Thank you for using our translation tool! See you next time.')
        guess = False




