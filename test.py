from ClassMaplestorysixV2 import *

six = CharacterV2(500,95)

six.skill_addname('오리진')
six.skill_adddamagepercent(0.0744)
six.skill_adddamagerise('오리진', 820800 , 27360)

six.mastery_addname('폭시')
six.mastery_adddamagepercent( 0.2067 )
six.mastery_adddamagerise('폭시' , 365 , 7)

print(six.skillinfo.damage_rise10['오리진'])
cnt = 1
new = 1
for i in range(29):
    new *= six.skillinfo.damage_rise['오리진'][i]
    cnt += 1
    if cnt == 10:
        print(new)
        cnt = 0
        new = 1
    
print(six.masteryinfo.damage_rise10['폭시'])
cnt = 1
new = 1
for i in range(29):
    new *= six.masteryinfo.damage_rise['폭시'][i]
    cnt += 1
    if cnt == 9 or cnt == 19 or cnt == 29 or cnt == 30:
        print(new)
        new = 1
    