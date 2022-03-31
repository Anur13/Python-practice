def wave(people: str) -> list[str]:
    result = []
    for (count, test) in enumerate(people):
        if test.isspace():
            continue
        p = list(people)
        p[count] = test.upper()
        result.append(''.join(p))
    return result


print(wave("test"))
