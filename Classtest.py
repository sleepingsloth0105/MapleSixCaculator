from ClassMaplestorysixV2 import *
from ClassMaplestorysixV1 import *

six = CharacterV1(500,95)
# six = Sixskill()

six.enhance_addname_and_level('잔시',2)
six.enhance_addname_and_level('퀴버',5)
six.enhance_addname_and_level('레인',1)
six.enhance_addname_and_level('미라주',1)
six.enhance_adddamagepercent( 0.1392 )
six.enhance_adddamagepercent( 0.1342 ) 
six.enhance_adddamagepercent( 0.1079 ) 
six.enhance_adddamagepercent( 0.032 )

six.mastery_addname_and_level('폭시',5)
six.mastery_adddamagepercent( 0.2067 )
six.mastery_adddamagerise('폭시' , 365 , 7)
'''
check = 1
for i in range(29):
    check *= six.masteryinfo.damage_rise['폭시'][i]
check10 = 1
for i in range(4):
    check10 *= six.masteryinfo.damage_rise10['폭시'][i]
print (575/372 , check , check10)
'''
six.skill_addname_and_level('오리진',8)
six.skill_adddamagepercent(0.0744)
six.skill_adddamagerise('오리진', 820800 , 27360)

# six.calculate()
six.printresult()
# six.printresult_withnumber()
''''''
six1 = CharacterV2(500,95)
# six = Sixskill()

six1.enhance_addname_and_level('잔시',2)
six1.enhance_addname_and_level('퀴버',5)
six1.enhance_addname_and_level('레인',1)
six1.enhance_addname_and_level('미라주',1)
six1.enhance_adddamagepercent( 0.1392 )
six1.enhance_adddamagepercent( 0.1342 ) 
six1.enhance_adddamagepercent( 0.1079 ) 
six1.enhance_adddamagepercent( 0.032 )

six1.mastery_addname_and_level('폭시',5)
six1.mastery_adddamagepercent( 0.2067 )
six1.mastery_adddamagerise('폭시' , 365 , 7)
'''
check = 1
for i in range(29):
    check *= six.masteryinfo.damage_rise['폭시'][i]
check10 = 1
for i in range(4):
    check10 *= six.masteryinfo.damage_rise10['폭시'][i]
print (575/372 , check , check10)
'''
six1.skill_addname_and_level('오리진',8)
six1.skill_adddamagepercent(0.0744)
six1.skill_adddamagerise('오리진', 820800 , 27360)

# six.calculate()
six1.printresult()
# six.printresult_withnumber()