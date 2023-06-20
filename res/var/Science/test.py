_str = '''
'''

def returnNum(_var):
    if _var == 'a':
        return 1
    if _var == 'b':
        return 2
    if _var == 'c':
        return 3
    if _var == 'd':
        return 4

from googletrans import Translator

translator = Translator()

newVar = ""
cou = 0
for line in _str.splitlines():
    cou+=1
    if cou == 1:
        newVar+=f'h++\nwindow["h-e-q-ma"+h] = "{(translator.translate(line, src="en", dest="ml").text)}";\nwindow["h-e-q-en"+h] = "{line}";\n'
    if cou == 2:
        newVar+=f'window["h-e-A"+h] = "{line}";\n'.replace("a) ","")
    if cou == 3:
        newVar+=f'window["h-e-B"+h] = "{line}";\n'.replace("b) ","")
    if cou == 4:
        newVar+=f'window["h-e-C"+h] = "{line}";\n'.replace("c) ","")
    if cou == 5:
        newVar+=f'window["h-e-D"+h] = "{line}";\n'.replace("d) ","")
    if cou == 6:
        newVar+= f'window["h-e-ans"+h] = {line};\n'.replace("Answer: ",'')
    if cou == 7:
        cou = 0
        newVar+="\n"
print(newVar)




# translated_text = translator.translate('안녕하세요.')
# print(translated_text.text)

# translated_text = translator.translate('안녕하세요.', dest='ml')
# print(translated_text.text)

# translated_text = translator.translate('veritas lux mea', src='la', dest='ml')
# print(translated_text.text)
