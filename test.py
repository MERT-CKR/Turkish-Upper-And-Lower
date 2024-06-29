import TurkishUpperLower as TUL

#normal lower test
text="İstanbul".lower()
if "istanbul" == text:
  print("lower metodu çalıştı mı? ",True)   
else:
  print("lower metodu çalıştı mı? ",False)
#output: false


text="İstanbul".casefold()
if "istanbul" == text:
  print("casefold metodu çalıştı mı? ",True)   
else:
  print("casefold metodu çalıştı mı? ",False)
  
#output: false

text= TUL.tr_lower("İstanbul")
if "istanbul" == text:
  print("Turkish upper lower çalıştı mı? ",True)   
else:
  print("Turkish upper lower çalıştı mı? ",False)
  
#output: True