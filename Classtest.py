from ClassMaplestorysixV2 import *

six = CharacterV2(500,95)
# six = Sixskill()

six.enhance_addname('잔시' , '퀴버' , '레인' , '미라주')
six.enhance_adddamagepercent( 0.1392 , 0.1342 , 0.1079 , 0.032)

six.mastery_addname('폭시')
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
six.skill_addname('오리진')
six.skill_adddamagepercent(0.0744)
six.skill_adddamagerise('오리진', 820800 , 27360)

# six.calculate()
six.printresult()
# six.printresult_withnumber()