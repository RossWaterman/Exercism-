def translate(text):
    words = text.split()
    translated_words = []
    vowels = 'aeiou'
    # Check for words that start with vowels or specific consonant clusters
    for word in words:
        if word.startswith(('xr', 'yt')) or word.startswith(vowels):
            translated_words.append(word + 'ay')
    # Check for words that start with consonant clusters
        elif not word.startswith(vowels):
            consonant_cluster = ''
            for i, char in enumerate(word):
                if char not in (vowels):
                    consonant_cluster += char
                    if char == 'q' and word[i+1] == 'u':
                        consonant_cluster += 'u'
                        break
                    if i + 1 < len(word) and word[i+1] == 'y':
                        break
                else:
                    break
            translated_words.append(word[len(consonant_cluster):] + consonant_cluster + 'ay')
    return ' '.join(translated_words)





        
        