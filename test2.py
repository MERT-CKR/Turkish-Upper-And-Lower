import TurkishUpperLower as TL


text= "BUNU KÜÇÜK HARFLERLE YAZABİLİRMİSİN : ÇŞĞİÖÜI"

text2="bunu küçük harflerle yazabilirmisin : çşğiöüı"

print("küçük harflerle yazılması gereken cümle: ",text)
text_lower= text.lower()
print("normal lower:",text_lower)

text_trLower= TL.tr_lower(text)



print("tr lower:",text_trLower)

print("normal lower çalıştı mı?",text_lower==text2)
print("tr lower çalıştı mı?",text_trLower==text2)