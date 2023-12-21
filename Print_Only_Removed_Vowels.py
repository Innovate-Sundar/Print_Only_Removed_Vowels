text=str(input('Enter the String:'))
Vowels=['a','e','i','o','u','A','E','I','O','U']
textlen=len(text)
newtext=""
for i in range(textlen):
    if text[i] not in Vowels:
        newtext=newtext+text[i]
print('After Removing the Vowels of a Particular Word below,')
print(newtext)