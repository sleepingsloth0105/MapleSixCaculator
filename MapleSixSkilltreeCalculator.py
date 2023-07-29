from tkinter import *
import tkinter.font as font
import tkinter.ttk as ttk
from ClassMaplestorysixV1 import *
from ClassMaplestorysixV1_1 import *
from ClassMaplestorysixV2 import *
from ClassMaplestorysixV2_1 import *

root = Tk()
'''기본 '''
root.title("6차 스킬트리 효율성 계산기 1.3.1 version")
root.geometry("1280x720+350+100")
titlefont = font.Font(size=15, family="Malgun Gothic")
generalfont = font.Font(size = 10, family="Malgun Gothic")
activefont = font.Font(size= 40 , family="Malgun Gothic")
'''제목 및 설명'''

frame_explane = LabelFrame(root, text="6차 스킬트리 계산기" ,bd = 0,font= titlefont , labelanchor="n" )
frame_explane.place(x=20 , y = 30, width = 260, height= 400)
explanation1 = Label(frame_explane , text = "\n사용방법",font=generalfont)
explanation1.pack()
explanation2 = Label(frame_explane , text = "1. 보총뎀과 방무를 입력하고 \n 하단의 드래그박스를 이용해 \n 효율 계산을 원하는 재화 선택",font=generalfont)
explanation2.pack()
explanation3 = Label(frame_explane , text = "2. 스킬 관련 정보를 각 칸에 입력 \n 주의 : 스킬 데미지는 \"0\"레벨 스킬 데미지 \n 상승량은 레벨당 데미지 상승량 \n ex) 폭시 기준 스킬 데미지 365 , 상승량 7", font=generalfont)
explanation3.pack()
explanation4 = Label(frame_explane , text = "3. 계산 버튼을 누르기",font=generalfont)
explanation4.pack()
explanation5 = Label(frame_explane , text = "4. 같은 폴더 안에 생성된 \n 스킬트리.txt에서 결과를 확인",font=generalfont )
explanation5.pack()
explanation6 = Label(frame_explane , text = "참고 : 딜지분, 방무는 xx.xx의 형태로 입력 \n ex) 13.92 \n 보총뎀과 방무는 6차 스킬(오리진)을 \n 사용할 때의 값으로 입력해야합니다. \n 레벨은 입력하지 않을 시 5차는 \'0\'레벨 \n 나머지는 \'1\'레벨로 입력됩니다." ,font=generalfont )
explanation6.pack()
'''보총뎀 , 방무 입력 및 버전 선택'''
bossdamage = Label(root , text="보총뎀 : " , font=generalfont)
bossdamage.place(x=40 , y = 420)
inputbossdamage = Entry(root , width = 5)
inputbossdamage.place(x = 100 , y = 420)
defignore = Label(root, text="방무 : " , font=generalfont)
defignore.place ( x = 160 , y = 420)
inputignoredef = Entry(root , width = 5)
inputignoredef.place(x = 210 , y = 420)
#version_value = [ "1. 조각의 효율성 계산" ,"1.1 조각의 효율성 계산(장기)" ,"2. 솔 에르다의 효율성 계산", "2.1 솔 에르다의 효율성 계산(장기)"]
version_value = [ "1. 조각의 효율성 계산"  ,"2. 솔 에르다의 효율성 계산"]
version = ttk.Combobox(root , values= version_value,state="readonly" , width = 28 , font=generalfont)
version.current(0)
version.place(x = 40 , y = 450)
'''5차 강화코어'''
frame_enhance = LabelFrame(root, text="5차 강화코어" ,relief="solid" ,bd = 1,font= titlefont , labelanchor="n" )
frame_enhance.place(x=300 , y = 30, width = 800, height= 165)

enhance_1 = Label(frame_enhance , text = "5차 강화코어 1 ", font=generalfont)
enhance_1.place(x=10 , y = 10)
enhance_2 = Label(frame_enhance , text = "5차 강화코어 2 ", font=generalfont)
enhance_2.place(x=10 , y = 40)
enhance_3 = Label(frame_enhance , text = "5차 강화코어 3 ", font=generalfont)
enhance_3.place(x=10 , y = 70)
enhance_4 = Label(frame_enhance , text = "5차 강화코어 4 ", font=generalfont)
enhance_4.place(x=10 , y = 100)

name1 = Label(frame_enhance , text = "이름 :", font=generalfont)
name2 = Label(frame_enhance , text = "이름 :", font=generalfont)
name3 = Label(frame_enhance , text = "이름 :", font=generalfont)
name4 = Label(frame_enhance , text = "이름 :", font=generalfont)
name1.place(x=110 , y = 10)
name2.place(x=110 , y = 40)
name3.place(x=110 , y = 70)
name4.place(x=110 , y = 100)
enhanceinputname1 = Entry(frame_enhance, width= 10)
enhanceinputname2 = Entry(frame_enhance, width= 10)
enhanceinputname3 = Entry(frame_enhance, width= 10)
enhanceinputname4 = Entry(frame_enhance, width= 10)
enhanceinputname1.place(x= 150 ,y = 10)
enhanceinputname2.place(x= 150 ,y = 40)
enhanceinputname3.place(x= 150 ,y = 70)
enhanceinputname4.place(x= 150 ,y = 100)

dmgper1 = Label(frame_enhance , text = "딜지분 :", font=generalfont)
dmgper2 = Label(frame_enhance , text = "딜지분 :", font=generalfont)
dmgper3 = Label(frame_enhance , text = "딜지분 :", font=generalfont)
dmgper4 = Label(frame_enhance , text = "딜지분 :", font=generalfont)
dmgper1.place(x=230 , y = 10)
dmgper2.place(x=230 , y = 40)
dmgper3.place(x=230 , y = 70)
dmgper4.place(x=230 , y = 100)
enhanceinputdmgper1 = Entry(frame_enhance, width= 5)
enhanceinputdmgper2 = Entry(frame_enhance, width= 5)
enhanceinputdmgper3 = Entry(frame_enhance, width= 5)
enhanceinputdmgper4 = Entry(frame_enhance, width= 5)
enhanceinputdmgper1.place(x= 290 ,y = 10)
enhanceinputdmgper2.place(x= 290 ,y = 40)
enhanceinputdmgper3.place(x= 290 ,y = 70)
enhanceinputdmgper4.place(x= 290 ,y = 100)

level1 = Label(frame_enhance , text = "레벨 :", font=generalfont)
level2 = Label(frame_enhance , text = "레벨 :", font=generalfont)
level3 = Label(frame_enhance , text = "레벨 :", font=generalfont)
level4 = Label(frame_enhance , text = "레벨 :", font=generalfont)
level1.place(x=340 , y = 10)
level2.place(x=340 , y = 40)
level3.place(x=340 , y = 70)
level4.place(x=340 , y = 100)
enhanceinputlevel1 = Entry(frame_enhance, width= 5)
enhanceinputlevel2 = Entry(frame_enhance, width= 5)
enhanceinputlevel3 = Entry(frame_enhance, width= 5)
enhanceinputlevel4 = Entry(frame_enhance, width= 5)
enhanceinputlevel1.place(x= 390 ,y = 10)
enhanceinputlevel2.place(x= 390 ,y = 40)
enhanceinputlevel3.place(x= 390 ,y = 70)
enhanceinputlevel4.place(x= 390 ,y = 100)



'''마스터리 코어'''
frame_mastery = LabelFrame(root, text="마스터리 코어" ,relief="solid" ,bd = 1,font= titlefont , labelanchor="n" )
frame_mastery.place(x=300 , y = 210, width = 800, height= 165)

mastery_1 = Label(frame_mastery , text = "마스터리 코어 1 ", font=generalfont)
mastery_1.place(x=10 , y = 10)
mastery_2 = Label(frame_mastery , text = "마스터리 코어 2 ", font=generalfont)
mastery_2.place(x=10 , y = 40)
mastery_3 = Label(frame_mastery , text = "마스터리 코어 3 ", font=generalfont)
mastery_3.place(x=10 , y = 70)
mastery_4 = Label(frame_mastery , text = "마스터리 코어 4 ", font=generalfont)
mastery_4.place(x=10 , y = 100)

name1 = Label(frame_mastery , text = "이름 :", font=generalfont)
name2 = Label(frame_mastery , text = "이름 :", font=generalfont)
name3 = Label(frame_mastery , text = "이름 :", font=generalfont)
name4 = Label(frame_mastery , text = "이름 :", font=generalfont)
name1.place(x=110 , y = 10)
name2.place(x=110 , y = 40)
name3.place(x=110 , y = 70)
name4.place(x=110 , y = 100)
masteryinputname1 = Entry(frame_mastery, width= 10)
masteryinputname2 = Entry(frame_mastery, width= 10)
masteryinputname3 = Entry(frame_mastery, width= 10)
masteryinputname4 = Entry(frame_mastery, width= 10)
masteryinputname1.place(x= 150 ,y = 10)
masteryinputname2.place(x= 150 ,y = 40)
masteryinputname3.place(x= 150 ,y = 70)
masteryinputname4.place(x= 150 ,y = 100)

dmgper1 = Label(frame_mastery , text = "딜지분 :", font=generalfont)
dmgper2 = Label(frame_mastery , text = "딜지분 :", font=generalfont)
dmgper3 = Label(frame_mastery , text = "딜지분 :", font=generalfont)
dmgper4 = Label(frame_mastery , text = "딜지분 :", font=generalfont)
dmgper1.place(x=230 , y = 10)
dmgper2.place(x=230 , y = 40)
dmgper3.place(x=230 , y = 70)
dmgper4.place(x=230 , y = 100)
masteryinputdmgper1 = Entry(frame_mastery, width= 5)
masteryinputdmgper2 = Entry(frame_mastery, width= 5)
masteryinputdmgper3 = Entry(frame_mastery, width= 5)
masteryinputdmgper4 = Entry(frame_mastery, width= 5)
masteryinputdmgper1.place(x= 290 ,y = 10)
masteryinputdmgper2.place(x= 290 ,y = 40)
masteryinputdmgper3.place(x= 290 ,y = 70)
masteryinputdmgper4.place(x= 290 ,y = 100)

level1dmg1 = Label(frame_mastery , text = "스킬 데미지 :", font=generalfont)
level1dmg2 = Label(frame_mastery , text = "스킬 데미지 :", font=generalfont)
level1dmg3 = Label(frame_mastery , text = "스킬 데미지 :", font=generalfont)
level1dmg4 = Label(frame_mastery , text = "스킬 데미지 :", font=generalfont)
level1dmg1.place(x=340 , y = 10)
level1dmg2.place(x=340 , y = 40)
level1dmg3.place(x=340 , y = 70)
level1dmg4.place(x=340 , y = 100)
masteryinputlevel1dmg1 = Entry(frame_mastery, width= 5)
masteryinputlevel1dmg2 = Entry(frame_mastery, width= 5)
masteryinputlevel1dmg3 = Entry(frame_mastery, width= 5)
masteryinputlevel1dmg4 = Entry(frame_mastery, width= 5)
masteryinputlevel1dmg1.place(x= 430 ,y = 10)
masteryinputlevel1dmg2.place(x= 430 ,y = 40)
masteryinputlevel1dmg3.place(x= 430 ,y = 70)
masteryinputlevel1dmg4.place(x= 430 ,y = 100)

levelupdmg1 = Label(frame_mastery , text = "상승량 :", font=generalfont)
levelupdmg2 = Label(frame_mastery , text = "상승량 :", font=generalfont)
levelupdmg3 = Label(frame_mastery , text = "상승량 :", font=generalfont)
levelupdmg4 = Label(frame_mastery , text = "상승량 :", font=generalfont)
levelupdmg1.place(x=480 , y = 10)
levelupdmg2.place(x=480 , y = 40)
levelupdmg3.place(x=480 , y = 70)
levelupdmg4.place(x=480 , y = 100)
masteryinputlevelupdmg1 = Entry(frame_mastery, width= 5)
masteryinputlevelupdmg2 = Entry(frame_mastery, width= 5)
masteryinputlevelupdmg3 = Entry(frame_mastery, width= 5)
masteryinputlevelupdmg4 = Entry(frame_mastery, width= 5)
masteryinputlevelupdmg1.place(x= 540 ,y = 10)
masteryinputlevelupdmg2.place(x= 540 ,y = 40)
masteryinputlevelupdmg3.place(x= 540 ,y = 70)
masteryinputlevelupdmg4.place(x= 540 ,y = 100)

level1 = Label(frame_mastery , text = "레벨 :", font=generalfont)
level2 = Label(frame_mastery , text = "레벨 :", font=generalfont)
level3 = Label(frame_mastery , text = "레벨 :", font=generalfont)
level4 = Label(frame_mastery , text = "레벨 :", font=generalfont)
level1.place(x=590 , y = 10)
level2.place(x=590 , y = 40)
level3.place(x=590 , y = 70)
level4.place(x=590 , y = 100)
masteryinputlevel1 = Entry(frame_mastery, width= 5)
masteryinputlevel2 = Entry(frame_mastery, width= 5)
masteryinputlevel3 = Entry(frame_mastery, width= 5)
masteryinputlevel4 = Entry(frame_mastery, width= 5)
masteryinputlevel1.place(x= 640 ,y = 10)
masteryinputlevel2.place(x= 640 ,y = 40)
masteryinputlevel3.place(x= 640 ,y = 70)
masteryinputlevel4.place(x= 640 ,y = 100)



'''6차 스킬 코어'''
frame_skill = LabelFrame(root, text="6차 스킬 코어" ,relief="solid" ,bd = 1,font= titlefont , labelanchor="n" )
frame_skill.place(x=300 , y = 390, width = 800, height= 225)

skill_1 = Label(frame_skill , text = "6차 스킬 코어 1 ", font=generalfont)
skill_1.place(x=10 , y = 10)
skill_2 = Label(frame_skill , text = "6차 스킬 코어 2 ", font=generalfont)
skill_2.place(x=10 , y = 40)
skill_3 = Label(frame_skill , text = "6차 스킬 코어 3 ", font=generalfont)
skill_3.place(x=10 , y = 70)
skill_4 = Label(frame_skill , text = "6차 스킬 코어 4 ", font=generalfont)
skill_4.place(x=10 , y = 100)
skill_5 = Label(frame_skill , text = "6차 스킬 코어 5 ", font=generalfont)
skill_5.place(x=10 , y = 130)
skill_6 = Label(frame_skill , text = "6차 스킬 코어 6 ", font=generalfont)
skill_6.place(x=10 , y = 160)


name1 = Label(frame_skill , text = "이름 :", font=generalfont)
name2 = Label(frame_skill , text = "이름 :", font=generalfont)
name3 = Label(frame_skill , text = "이름 :", font=generalfont)
name4 = Label(frame_skill , text = "이름 :", font=generalfont)
name5 = Label(frame_skill , text = "이름 :", font=generalfont)
name6 = Label(frame_skill , text = "이름 :", font=generalfont)
name1.place(x=110 , y = 10)
name2.place(x=110 , y = 40)
name3.place(x=110 , y = 70)
name4.place(x=110 , y = 100)
name5.place(x=110 , y = 130)
name6.place(x=110 , y = 160)
skillinputname1 = Entry(frame_skill, width= 10)
skillinputname2 = Entry(frame_skill, width= 10)
skillinputname3 = Entry(frame_skill, width= 10)
skillinputname4 = Entry(frame_skill, width= 10)
skillinputname5 = Entry(frame_skill, width= 10)
skillinputname6 = Entry(frame_skill, width= 10)
skillinputname1.place(x= 150 ,y = 10)
skillinputname2.place(x= 150 ,y = 40)
skillinputname3.place(x= 150 ,y = 70)
skillinputname4.place(x= 150 ,y = 100)
skillinputname5.place(x= 150 ,y = 130)
skillinputname6.place(x= 150 ,y = 160)

dmgper1 = Label(frame_skill , text = "딜지분 :", font=generalfont)
dmgper2 = Label(frame_skill , text = "딜지분 :", font=generalfont)
dmgper3 = Label(frame_skill , text = "딜지분 :", font=generalfont)
dmgper4 = Label(frame_skill , text = "딜지분 :", font=generalfont)
dmgper5 = Label(frame_skill , text = "딜지분 :", font=generalfont)
dmgper6 = Label(frame_skill , text = "딜지분 :", font=generalfont)
dmgper1.place(x=230 , y = 10)
dmgper2.place(x=230 , y = 40)
dmgper3.place(x=230 , y = 70)
dmgper4.place(x=230 , y = 100)
dmgper5.place(x=230 , y = 130)
dmgper6.place(x=230 , y = 160)
skillinputdmgper1 = Entry(frame_skill, width= 5)
skillinputdmgper2 = Entry(frame_skill, width= 5)
skillinputdmgper3 = Entry(frame_skill, width= 5)
skillinputdmgper4 = Entry(frame_skill, width= 5)
skillinputdmgper5 = Entry(frame_skill, width= 5)
skillinputdmgper6 = Entry(frame_skill, width= 5)
skillinputdmgper1.place(x= 290 ,y = 10)
skillinputdmgper2.place(x= 290 ,y = 40)
skillinputdmgper3.place(x= 290 ,y = 70)
skillinputdmgper4.place(x= 290 ,y = 100)
skillinputdmgper5.place(x= 290 ,y = 130)
skillinputdmgper6.place(x= 290 ,y = 160)

level1dmg1 = Label(frame_skill , text = "스킬 데미지 :", font=generalfont)
level1dmg2 = Label(frame_skill , text = "스킬 데미지 :", font=generalfont)
level1dmg3 = Label(frame_skill , text = "스킬 데미지 :", font=generalfont)
level1dmg4 = Label(frame_skill , text = "스킬 데미지 :", font=generalfont)
level1dmg5 = Label(frame_skill , text = "스킬 데미지 :", font=generalfont)
level1dmg6 = Label(frame_skill , text = "스킬 데미지 :", font=generalfont)
level1dmg1.place(x=340 , y = 10)
level1dmg2.place(x=340 , y = 40)
level1dmg3.place(x=340 , y = 70)
level1dmg4.place(x=340 , y = 100)
level1dmg5.place(x=340 , y = 130)
level1dmg6.place(x=340 , y = 160)
skillinputlevel1dmg1 = Entry(frame_skill, width= 10)
skillinputlevel1dmg2 = Entry(frame_skill, width= 10)
skillinputlevel1dmg3 = Entry(frame_skill, width= 10)
skillinputlevel1dmg4 = Entry(frame_skill, width= 10)
skillinputlevel1dmg5 = Entry(frame_skill, width= 10)
skillinputlevel1dmg6 = Entry(frame_skill, width= 10)
skillinputlevel1dmg1.place(x= 430 ,y = 10)
skillinputlevel1dmg2.place(x= 430 ,y = 40)
skillinputlevel1dmg3.place(x= 430 ,y = 70)
skillinputlevel1dmg4.place(x= 430 ,y = 100)
skillinputlevel1dmg5.place(x= 430 ,y = 130)
skillinputlevel1dmg6.place(x= 430 ,y = 160)

levelupdmg1 = Label(frame_skill , text = "상승량 :", font=generalfont)
levelupdmg2 = Label(frame_skill , text = "상승량 :", font=generalfont)
levelupdmg3 = Label(frame_skill , text = "상승량 :", font=generalfont)
levelupdmg4 = Label(frame_skill , text = "상승량 :", font=generalfont)
levelupdmg5 = Label(frame_skill , text = "상승량 :", font=generalfont)
levelupdmg6 = Label(frame_skill , text = "상승량 :", font=generalfont)
levelupdmg1.place(x=510 , y = 10)
levelupdmg2.place(x=510 , y = 40)
levelupdmg3.place(x=510 , y = 70)
levelupdmg4.place(x=510 , y = 100)
levelupdmg5.place(x=510 , y = 130)
levelupdmg6.place(x=510 , y = 160)
skillinputlevelupdmg1 = Entry(frame_skill, width= 6)
skillinputlevelupdmg2 = Entry(frame_skill, width= 6)
skillinputlevelupdmg3 = Entry(frame_skill, width= 6)
skillinputlevelupdmg4 = Entry(frame_skill, width= 6)
skillinputlevelupdmg5 = Entry(frame_skill, width= 6)
skillinputlevelupdmg6 = Entry(frame_skill, width= 6)
skillinputlevelupdmg1.place(x= 570 ,y = 10)
skillinputlevelupdmg2.place(x= 570 ,y = 40)
skillinputlevelupdmg3.place(x= 570 ,y = 70)
skillinputlevelupdmg4.place(x= 570 ,y = 100)
skillinputlevelupdmg5.place(x= 570 ,y = 130)
skillinputlevelupdmg6.place(x= 570 ,y = 160)

level1 = Label(frame_skill , text = "레벨 :", font=generalfont)
level2 = Label(frame_skill , text = "레벨 :", font=generalfont)
level3 = Label(frame_skill , text = "레벨 :", font=generalfont)
level4 = Label(frame_skill , text = "레벨 :", font=generalfont)
level5 = Label(frame_skill , text = "레벨 :", font=generalfont)
level6 = Label(frame_skill , text = "레벨 :", font=generalfont)
level1.place(x=630 , y = 10)
level2.place(x=630 , y = 40)
level3.place(x=630 , y = 70)
level4.place(x=630 , y = 100)
level5.place(x=630 , y = 130)
level6.place(x=630 , y = 160)
skillinputlevel1 = Entry(frame_skill, width= 5)
skillinputlevel2 = Entry(frame_skill, width= 5)
skillinputlevel3 = Entry(frame_skill, width= 5)
skillinputlevel4 = Entry(frame_skill, width= 5)
skillinputlevel5 = Entry(frame_skill, width= 5)
skillinputlevel6 = Entry(frame_skill, width= 5)
skillinputlevel1.place(x= 680 ,y = 10)
skillinputlevel2.place(x= 680 ,y = 40)
skillinputlevel3.place(x= 680 ,y = 70)
skillinputlevel4.place(x= 680 ,y = 100)
skillinputlevel5.place(x= 680 ,y = 130)
skillinputlevel6.place(x= 680 ,y = 160)

'''active 버튼'''
def active():
    if version.get() == "1. 조각의 효율성 계산":
        mycharacter = CharacterV1(int(inputbossdamage.get()) , float(inputignoredef.get()))
    elif version.get() == "1.1 조각의 효율성 계산(장기)":
        mycharacter = CharacterV1_1(int(inputbossdamage.get()) , float(inputignoredef.get()))
    elif version.get() == "2. 솔 에르다의 효율성 계산":
        mycharacter = CharacterV2(int(inputbossdamage.get()) , float(inputignoredef.get()))
    elif version.get() == "2.1 솔 에르다의 효율성 계산(장기)":
        mycharacter = CharacterV2_1(int(inputbossdamage.get()) , float(inputignoredef.get()))
    
    if enhanceinputname1.get() != "":
        if enhanceinputlevel1.get() != "":
            mycharacter.enhance_addname_and_level(enhanceinputname1.get(),enhanceinputlevel1.get())
        else:
            mycharacter.enhance_addname_and_level(enhanceinputname1.get())
        mycharacter.enhance_adddamagepercent(float(enhanceinputdmgper1.get())/100)
    if enhanceinputname2.get() != "":
        if enhanceinputlevel2.get() != "":
            mycharacter.enhance_addname_and_level(enhanceinputname2.get(),enhanceinputlevel2.get())
        else:
            mycharacter.enhance_addname_and_level(enhanceinputname2.get())
        mycharacter.enhance_adddamagepercent(float(enhanceinputdmgper2.get())/100)
    if enhanceinputname3.get() != "":
        if enhanceinputlevel3.get() != "":
            mycharacter.enhance_addname_and_level(enhanceinputname3.get(),enhanceinputlevel3.get())
        else:
            mycharacter.enhance_addname_and_level(enhanceinputname3.get())
        mycharacter.enhance_adddamagepercent(float(enhanceinputdmgper3.get())/100)
    if enhanceinputname4.get() != "":
        if enhanceinputlevel4.get() != "":
            mycharacter.enhance_addname_and_level(enhanceinputname4.get(),enhanceinputlevel4.get())
        else:
            mycharacter.enhance_addname_and_level(enhanceinputname4.get())
        mycharacter.enhance_adddamagepercent(float(enhanceinputdmgper4.get())/100)
        
    if masteryinputname1.get() != "":
        if masteryinputlevel1.get() != "":
            mycharacter.mastery_addname_and_level(masteryinputname1.get(),masteryinputlevel1.get())
        else:
            mycharacter.mastery_addname_and_level(masteryinputname1.get())
        mycharacter.mastery_adddamagepercent(float(masteryinputdmgper1.get())/100)
        mycharacter.mastery_adddamagerise(masteryinputname1.get(),int(masteryinputlevel1dmg1.get()),int(masteryinputlevelupdmg1.get()))
    if masteryinputname2.get() != "":
        if masteryinputlevel2.get() != "":
            mycharacter.mastery_addname_and_level(masteryinputname2.get(),masteryinputlevel2.get())
        else:
            mycharacter.mastery_addname_and_level(masteryinputname2.get())
        mycharacter.mastery_adddamagepercent(float(masteryinputdmgper2.get())/100)
        mycharacter.mastery_adddamagerise(masteryinputname2.get(),int(masteryinputlevel1dmg2.get()),int(masteryinputlevelupdmg2.get()))
    if masteryinputname3.get() != "":
        if masteryinputlevel3.get() != "":
            mycharacter.mastery_addname_and_level(masteryinputname3.get(),masteryinputlevel3.get())
        else:
            mycharacter.mastery_addname_and_level(masteryinputname3.get())
        mycharacter.mastery_adddamagepercent(float(masteryinputdmgper3.get())/100)
        mycharacter.mastery_adddamagerise(masteryinputname3.get(),int(masteryinputlevel1dmg3.get()),int(masteryinputlevelupdmg3.get()))
    if masteryinputname4.get() != "":
        if masteryinputlevel4.get() != "":
            mycharacter.mastery_addname_and_level(masteryinputname4.get(),masteryinputlevel4.get())
        else:
            mycharacter.mastery_addname_and_level(masteryinputname4.get())
        mycharacter.mastery_adddamagepercent(float(masteryinputdmgper4.get())/100)
        mycharacter.mastery_adddamagerise(masteryinputname4.get(),int(masteryinputlevel1dmg4.get()),int(masteryinputlevelupdmg4.get()))
        
    if skillinputname1.get() != "":
        if skillinputlevel1.get() != "":
            mycharacter.skill_addname_and_level(skillinputname1.get(),skillinputlevel1.get())
        else:
            mycharacter.skill_addname_and_level(skillinputname1.get())
        mycharacter.skill_adddamagepercent(float(skillinputdmgper1.get())/100)
        mycharacter.skill_adddamagerise(skillinputname1.get(),int(skillinputlevel1dmg1.get()),int(skillinputlevelupdmg1.get()))
    if skillinputname2.get() != "":
        if skillinputlevel2.get() != "":
            mycharacter.skill_addname_and_level(skillinputname2.get(),skillinputlevel2.get())
        else:
            mycharacter.skill_addname_and_level(skillinputname2.get())
        mycharacter.skill_adddamagepercent(float(skillinputdmgper2.get())/100)
        mycharacter.skill_adddamagerise(skillinputname2.get(),int(skillinputlevel1dmg2.get()),int(skillinputlevelupdmg2.get()))
    if skillinputname3.get() != "":
        if skillinputlevel3.get() != "":
            mycharacter.skill_addname_and_level(skillinputname3.get(),skillinputlevel3.get())
        else:
            mycharacter.skill_addname_and_level(skillinputname3.get())
        mycharacter.skill_adddamagepercent(float(skillinputdmgper3.get())/100)
        mycharacter.skill_adddamagerise(skillinputname3.get(),int(skillinputlevel1dmg3.get()),int(skillinputlevelupdmg3.get()))
    if skillinputname4.get() != "":
        if skillinputlevel4.get() != "":
            mycharacter.skill_addname_and_level(skillinputname4.get(),skillinputlevel4.get())
        else:
            mycharacter.skill_addname_and_level(skillinputname4.get())
        mycharacter.skill_adddamagepercent(float(skillinputdmgper4.get())/100)
        mycharacter.skill_adddamagerise(skillinputname4.get(),int(skillinputlevel1dmg4.get()),int(skillinputlevelupdmg4.get()))
    if skillinputname5.get() != "":
        if skillinputlevel5.get() != "":
            mycharacter.skill_addname_and_level(skillinputname5.get(),skillinputlevel5.get())
        else:
            mycharacter.skill_addname_and_level(skillinputname5.get())
        mycharacter.skill_adddamagepercent(float(skillinputdmgper5.get())/100)
        mycharacter.skill_adddamagerise(skillinputname5.get(),int(skillinputlevel1dmg5.get()),int(skillinputlevelupdmg5.get()))
    if skillinputname6.get() != "":
        if skillinputlevel6.get() != "":
            mycharacter.skill_addname_and_level(skillinputname6.get(),skillinputlevel6.get())
        else:
            mycharacter.skill_addname_and_level(skillinputname6.get())
        mycharacter.skill_adddamagepercent(float(skillinputdmgper6.get())/100)
        mycharacter.skill_adddamagerise(skillinputname6.get(),int(skillinputlevel1dmg6.get()),int(skillinputlevelupdmg6.get()))
        
    mycharacter.printresult()
    
activebutton = Button(root ,text= "계산" , font=activefont, width= 7, height = 1 ,command= active)
activebutton.place(x= 40 , y= 490)
root.mainloop()