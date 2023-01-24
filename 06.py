# Напишите программу, удаляющую из текста 
# все слова, содержащие ""абв""

from os import system
system ( "cls" )

my_text = 'Незадачливый Клабва иабв заяц коралабвлы был оабвзадачен озадачен \
Кларытабв новой поэтомуабв задачей абв съелабв абву коралабвлы Карабвла ихабв отобабврав'
separators = [ ",", "!", ".", "?" ]
string = " ".join( map( lambda s: s if "абв" not in s.lower() else s[-1] if s[-1] in separators else "", my_text.split() ) ).replace("  ", " ").strip()

print( "Программа удаляет из текста все слова, содержащие абв" )
print( f"{my_text = }" )
print( f"{string = }\n" )