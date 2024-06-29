# TurkishUpper-And-TurkishLower

Pythondaki upper() ve lower() metodları bazı türkçe karakterlerde çalışmaz

```
#lower test
text="İstanbul".lower()
if "istanbul" == text:
  print("lower metodu çalıştı mı? ",True)   
else:
  print("lower metodu çalıştı mı? ",False)

#output: false
```
---


Aynı problem casefold() metodunda da geçerli:

```
#casefold test
text="İstanbul".casefold()
if "istanbul" == text:
  print("casefold metodu çalıştı mı? ",True)   
else:
  print("casefold metodu çalıştı mı? ",False)
  
#output: false
```
---


Ben bu sorunu Turkish Upper Lower'ı geliştirerek çözdüm:

```
#Turkish upper lower test
text= TUL.tr_lower("İstanbul")
if "istanbul" == text:
  print("Turkish upper lower çalıştı mı? ",True)   
else:
  print("Turkish upper lower çalıştı mı? ",False)
  
#output: True
```