# IPA Phonemizer: https://github.com/bootphon/phonemizer

import os
import string

_pad = "$"
_punctuation = '«»“”;:,.!?¡¿—…" '
_letters = '()1234567*\u0361\u0306\u0303MNOPQRSTUVWXYăabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘̩'ᵻ"



# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

letters = list(_letters) + list(_letters_ipa)

dicts = {}
for i in range(len((symbols))):
    dicts[symbols[i]] = i

class TextCleaner:
    def __init__(self, dummy=None):
        self.word_index_dictionary = dicts
        print(len(dicts))
    def __call__(self, text):
        indexes = []
        for char in text:
            try:
                indexes.append(self.word_index_dictionary[char])
            except KeyError:
                indexes.append(self.word_index_dictionary['U']) # unknown token
#                 print(char)
        return indexes

if __name__ == '__main__':
    phonems ="kak5 man2_ham2 kuə4 dɯk5 bi6 tɤ̆j4_căj1 taj6 ɛɲ1 va2 fap5 , va2 nestlé*é ŋiəm1_ɲiən1 hɯəŋ4 lɤj6 ."
    for i in phonems:
        if i not in dicts:
            print(i)