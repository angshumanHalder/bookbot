def get_num_words(content):
    return content.split()


def get_num_characters(content):
    charater_occurances = {}
    for c in content:
        if c.lower() not in charater_occurances:
            charater_occurances[c.lower()] = 0
        charater_occurances[c.lower()] += 1
    return charater_occurances

