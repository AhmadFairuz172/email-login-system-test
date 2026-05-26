import re

def email_valid(emel):
    
    #1.No spaces
    if " " in emel:
        print('Ralat!Emel tidak boleh ada jarak')
        return False

    #2.Not over 30 words
    if len(emel) > 30:
        print('Ralat!Emel tidak boleh melebihi 50 patah perkataan')
        return False

    #3.No bad words
    bad_words = ['ass','boobs','butt']
    for word in bad_words:
        if word in emel.lower():
            print('Ralat!Emel mengandungi nama buruk')
            return False
    
    #4.Not less than 6 words
    if len(emel) < 6:
        print('Ralat!Emel tidak boleh kurang dari 6 patah perkataan')
        return False

    #5.Follow pattern
    pattern = r"^[a-zA-Z0-9]gmail\.com$"

    if re.match(pattern, emel):
         return True
    else:
        print('Ralat!Bentuk emel tidak sah.')
        return False

    
    return True
    
