import pykakasi

def change_word(word:str) -> str:
    kks = pykakasi.kakasi()
    result = kks.convert(word)
    return result[0]['passport']