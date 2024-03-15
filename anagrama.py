#¿Es un anagrama?
"""
Escribe una funcion que reciba dos palabras(String) y retorne
verdadero o falso (Bool) segun sean anagramas o no.
- Un anagrama consiste en formar una palabra redondeando TODAS
  las letras de otra pabra inicial.
- No hace falta comprobar que las palabras existan.
- Dos palabras exactamente iguales no son anagramas.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Amor","Roma"))