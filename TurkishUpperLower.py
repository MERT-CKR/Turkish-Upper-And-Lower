def tr_lower(text):
    tr_dict = {'I':'ı', 'İ':'i', 'Ç':'ç', 'Ş':'ş', 'Ö':'ö', 'Ü':'ü', 'Ğ':'ğ'}
    for key, value in tr_dict.items():
        text = text.replace(key, value)
    return text.lower()

def tr_upper(text):
    tr_dict = {'ı':'I', 'i':'İ', 'ç':'Ç', 'ş':'Ş', 'ö':'Ö', 'ü':'Ü', 'ğ':'Ğ'}
    for key, value in tr_dict.items():
        text = text.replace(key, value)
    return text.upper()



text= "BUNU KÜÇÜK HARFLERLE YAZABİLİRMİSİN : ÇŞĞİÖÜI"

text2="bunu küçük harflerle yazabilirmisin : çşğiöüı"

print("küçük harflerle yazılması gereken cümle: ",text)
text_lower= text.lower()
print("normal lower:",text_lower)

text_trLower= tr_lower(text)



print("tr lower:",text_trLower)

print("normal lower çalıştı mı?",text_lower==text2)
print("tr lower çalıştı mı?",text_trLower==text2)
