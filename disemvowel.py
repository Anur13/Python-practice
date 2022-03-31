def disemvowel(string_):
    string_.casefold()
    translation_table = {ord("a"): None,
                         ord("e"): None,
                         ord("u"): None,
                         ord("i"): None,
                         ord("o"): None,
                         ord("A"): None,
                         ord("E"): None,
                         ord("U"): None,
                         ord("I"): None,
                         ord("O"): None
                         }
    new_str = string_.translate()
    return new_str


disemvowel("es")
