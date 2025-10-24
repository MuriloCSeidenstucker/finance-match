import Levenshtein
from unidecode import unidecode

def remove_accents_and_spaces(input_str: str) -> str:
    return (
        unidecode(input_str.replace(" ", "").lower())
        if isinstance(input_str, str)
        else input_str
    )

def compare(a: str, b:str) -> bool:
    processed_a = remove_accents_and_spaces(a)
    processed_b = remove_accents_and_spaces(b)
    distance = Levenshtein.ratio(processed_a, processed_b)
    return distance >= 0.5
