import pykakasi

def change_word(word:str) -> str:
    """漢字からローマ字に変換するライブラリを使用
    """
    kks = pykakasi.kakasi()
    result = kks.convert(word)
    return result[0]['passport']