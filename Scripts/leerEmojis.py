# -*- coding: utf-8 -*-

import emoji

"""
La función recibe una cadena de texto y la devuelve después de haberle quitado los emoticonos que aparecen en ella
"""

def eliminarEmojis(cadena):
    fraseSinEmojis = []
    for i in cadena:
        if i not in emoji.UNICODE_EMOJI['en']:
            fraseSinEmojis.append(i)
    return ''.join(fraseSinEmojis)