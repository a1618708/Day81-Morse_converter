alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

morse_a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

number=["0","1","2","3","4","5","6","7","8","9"]

morse_num=["-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]

Is_Run=True
while Is_Run:
  call=input("If translating string to Morse code: T \nConverting Morse code to string : C\n").upper()
  if call=="T":
    translator=""
    strings=list(input("please enter strings that want to convert to morse code? \n").lower())
    for string in strings:
      if string in alphabet:
        translator += morse_a[alphabet.index(string)] + "   "
      elif string in number:
        translator += morse_num[number.index(string)] + "   "
      elif string == " ":
        translator += "       "
      else:
        translator += string
    print(translator)
  elif call=="C":
    converter=""
    codes=input("please enter Morse codes that want to convert to morse code? \n").split("   ")
    for code in codes:
      code = code.strip()
      print(code)
      if code in morse_a:
        converter += alphabet[morse_a.index(code)]
      elif code in number:
        converter += number[morse_num.index(code)]
      else:
        converter += " "
    print(converter)
  else:
    Is_Run=False