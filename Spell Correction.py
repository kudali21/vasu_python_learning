from spellchecker import SpellChecker

def correct_spelling(text):
    spell = SpellChecker()
    words = text.split()
    corrected_text = []
    for word in words:
        corrected_word = spell.correction(word)
        corrected_text.append(corrected_word)
    return ' '.join(corrected_text)

# Example usage
text = "wht is uour nama"
corrected_text = correct_spelling(text)
print(corrected_text)