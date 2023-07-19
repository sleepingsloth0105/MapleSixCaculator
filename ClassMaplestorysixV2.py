import os

class Enhance: # 5차 강화 코어
    def __init__(self):
        self.name = []
        self.damage_percent = []
        self.damage_rise = [ 112/111 , 113/112 , 114/113 , 115/114 , 116/115 , 117/116 , 118/117 , 119/118 , 125/119 , 126/125 , 
                        127/126 , 128/127 , 129/128 , 130/129 , 131/130 , 132/131 , 133/132 , 134/133 , 140/134 , 141/140, 
                        142/141, 143/142 , 144/143 , 145/144 , 146/145 , 147/146 , 148/147 , 149/148 , 160/149, 1 ]
        self.piece = [ 23,27,30,34,38,42,45,49,150,60,68,75,83,90,98,105,113,120,263,128,135,143,150,158,165,173,180,188,375,10] 
        self.level= [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    
    def addname(self, newname):
        for i in range(len(newname)):
            self.name.append(newname[i])   
    def adddamagepercent(self,newdamage):
        for i in range(len(newdamage)):
            self.damage_percent.append(newdamage[i])
        
class Mastery: # 마스터리 코어
    def __init__(self):
        self.name = []
        self.damage_percent = []
        self.damage_rise = {}
        self.piece = [15,18,20,23,25,28,30,33,100,40,45,50,55,60,65,70,75,80,175,85,90,95,100,105,110,115,120,125,250,10]
        self.level = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    
    def addname(self, newname):
        for i in range(len(newname)):
            self.name.append(newname[i])   
    def adddamagepercent(self,newdamage):
        for i in range(len(newdamage)):
            self.damage_percent.append(newdamage[i])
    def adddamagerise(self,skillname,newdmgrise):
        self.damage_rise[skillname] = newdmgrise
        
class Skill: # 6차 스킬 (오리진 등등)
    def __init__(self):
        self.name = []
        self.damage_percent = []
        self.damage_rise = {}
        self.piece = [ 30,35,40,45,50,55,60,65,200,80,90,100,110,120,130,140,150,160,350,170,180,190,200,210,220,230,240,250,500,10 ] 
        self.level = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        
    def addname(self, newname):
        for i in range(len(newname)):
            self.name.append(newname[i])   
    def adddamagepercent(self,newdamage):
        for i in range(len(newdamage)):
            self.damage_percent.append(newdamage[i])
    def adddamagerise(self,skillname,newdmgrise):
        self.damage_rise[skillname] = newdmgrise
        
class CharacterV2:
    def __init__(self,bossdamage,ignoredef):
        self.current_enhance = []
        self.current_mastery = []
        self.current_skill = []
        self.enhanceinfo = Enhance()
        self.masteryinfo = Mastery()
        self.skillinfo = Skill()
        self.bossdmg = 100 + bossdamage
        self.ignoredef=ignoredef
        
    
    ''' 캐릭터 스킬 정보 추가 '''
    def enhance_addname(self,*newname):
        self.enhanceinfo.addname(newname)
        for i in range(len(newname)):
            self.current_enhance.append(1)
    def enhance_adddamagepercent(self,*newdmgper):
        self.enhanceinfo.adddamagepercent(newdmgper)
        
    def mastery_addname(self,*newname):
        self.masteryinfo.addname(newname)
        for i in range(len(newname)):
            self.current_mastery.append(1)
    def mastery_adddamagepercent(self,*newdmgper):
        self.masteryinfo.adddamagepercent(newdmgper)
    def mastery_adddamagerise(self,skillname,firstleveldmg,increaseddmg):
        dmgrise = []
        old = firstleveldmg
        for i in range(29):
            new = old + increaseddmg
            newdmg = new / old
            dmgrise.append(newdmg)
            old = new
        dmgrise.append(1)
        self.masteryinfo.adddamagerise(skillname,dmgrise)

    def skill_addname(self,*newname):
        self.skillinfo.addname(newname)
        for i in range(len(newname)):
            self.current_skill.append(1)
    def skill_adddamagepercent(self,*newdmgper):
        self.skillinfo.adddamagepercent(newdmgper)
    def skill_adddamagerise(self,skillname,firstleveldmg,increaseddmg):
        dmgrise = []
        old = firstleveldmg
        for i in range(29):
            new = old + increaseddmg
            newdmg = new / old
            dmgrise.append(newdmg)
            old = new
        dmgrise.append(1)
        self.skillinfo.adddamagerise(skillname,dmgrise)
        self.skillinfo.damage_rise[skillname][8] = self.skillinfo.damage_rise[skillname][8] * self.calcdef20()
        self.skillinfo.damage_rise[skillname][18] = self.skillinfo.damage_rise[skillname][18] * self.calcboss20()
        self.skillinfo.damage_rise[skillname][28] =  self.skillinfo.damage_rise[skillname][28] * self.calcboss50() * self.calcdef50()
        
    '''오리진스킬 보공 계산'''    
    def calcboss20(self):
        newdmg = self.bossdmg + 20
        return newdmg / self.bossdmg
    def calcboss50(self):
        newdmg = self.bossdmg + 50
        return newdmg / self.bossdmg
    
    '''오리진스킬 방무 계산'''
    def calcdef20(self):
        oldignoredef = (1 - (self.ignoredef/100))
        newignoredef = (1 - (self.ignoredef/100)) * (1 - 0.2)
        recentdmg = (1 - ( 3 * oldignoredef)) 
        newdmg = (1 - ( 3 * newignoredef)) 
        return newdmg / recentdmg
    def calcdef50(self):
        oldignoredef = (1 - (self.ignoredef/100))
        newignoredef = (1 - (self.ignoredef/100)) * (1 - 0.5)
        recentdmg = (1 - ( 3.8 * oldignoredef)) 
        newdmg = (1 - ( 3.8 * newignoredef)) 
        return newdmg / recentdmg
    
        
             
    ''' 가장 효율적인 스킬 레벨업 계산'''    
    def calculate(self):
        result = []
        result_dic = {}
        for i in range(len(self.current_enhance)):
            nextlevel = self.current_enhance[i] + 1
            idx = self.enhanceinfo.level.index(nextlevel)
            add = self.enhanceinfo.damage_percent[i] * (self.enhanceinfo.damage_rise[idx]-1) / self.enhanceinfo.piece[idx]
            result.append(add)
            result_dic[add] = ['enhance',i,nextlevel,self.enhanceinfo.name[i]]
        for i in range(len(self.current_mastery)):
            nextlevel = self.current_mastery[i] + 1
            idx = self.masteryinfo.level.index(nextlevel)
            add = self.masteryinfo.damage_percent[i] * (self.masteryinfo.damage_rise[self.masteryinfo.name[i]][idx]-1) / self.masteryinfo.piece[idx]
            result.append(add)
            result_dic[add] = ['mastery',i,nextlevel,self.masteryinfo.name[i]]
        for i in range(len(self.current_skill)):
            nextlevel = self.current_skill[i] + 1
            idx = self.skillinfo.level.index(nextlevel)
            add = self.skillinfo.damage_percent[i] * (self.skillinfo.damage_rise[self.skillinfo.name[i]][idx]-1) / self.skillinfo.piece[idx]
            result.append(add)
            result_dic[add] = ['skill',i,nextlevel,self.skillinfo.name[i]]
        maxresult = max(result)
        if maxresult == 0:
            return 0
        else:
            return result_dic[maxresult]
        
    '''캐릭터 레벨 업'''        
    def levelup(self,calcresult):
        if calcresult[0] == 'enhance':
            self.current_enhance[calcresult[1]] = calcresult[2]
        elif calcresult[0] == 'mastery':
            self.current_mastery[calcresult[1]] = calcresult[2]   
        else:
            self.current_skill[calcresult[1]] = calcresult[2]
            
    ''' 만랩까지 반복'''
    def levelup_max(self):
        record = []
        old = "시작"
        num = 0
        while self.calculate() != 0:
            calcinfo = self.calculate()
            new = calcinfo[3]
            if new != old:
                record.append([old , num])
                old = new
                num = calcinfo[2]     
            else:
                num = calcinfo[2]
            self.levelup(calcinfo)
            if self.calculate() == 0:
                record.append([old, num])
        return record
    
    '''출력'''
    def printresult(self):
        result = self.levelup_max()
        recentdir = os.path.dirname(os.path.realpath(__file__))
        usedir = recentdir + "/result.txt"
        resultfile = open(usedir, 'w')
        for i in range(len(result)):
            data = "스킬 : " +  result[i][0]  + " / 레벨 : "  + str(result[i][1])
            print(data)
            resultfile.write(data)
            resultfile.write('\n')
        resultfile.close()

        
        
                
'''       
class Sixskill: # 6차 전체를 관리하는 클래스
    def __init__(self):
        self.enhance = Enhance()
        self.mastery = Mastery()
        self.skill = Skill()
        self.result = []
        self.resultdamage = []
        self.result_dic = {}
        
    def enhance_addname(self,*newname):
        self.enhance.addname(newname)
    def enhance_adddamagepercent(self,*newdmgper):
        self.enhance.adddamagepercent(newdmgper)
        
    def mastery_addname(self,*newname):
        self.mastery.addname(newname)
    def mastery_adddamagepercent(self,*newdmgper):
        self.mastery.adddamagepercent(newdmgper)
    def mastery_adddamagerise(self,skillname,firstleveldmg,increaseddmg):
        dmgrise = []
        old = firstleveldmg
        for i in range(29):
            new = old + increaseddmg
            newdmg = new / old
            dmgrise.append(newdmg)
            old = new
        self.mastery.adddamagerise(skillname,dmgrise)

    def skill_addname(self,*newname):
        self.skill.addname(newname)
    def skill_adddamagepercent(self,*newdmgper):
        self.skill.adddamagepercent(newdmgper)
    def skill_adddamagerise(self,skillname,firstleveldmg,increaseddmg):
        dmgrise = []
        old = firstleveldmg
        for i in range(29):
            new = old + increaseddmg
            newdmg = new / old
            dmgrise.append(newdmg)
            old = new
        self.skill.adddamagerise(skillname,dmgrise)


    def calculate(self):
        for i in range(len(self.enhance.name)):
            current = self.enhance.name[i]
            current_damage_percent = self.enhance.damage_percent[i]
            for j in range(len(self.enhance.piece)):
                increased_damage_per_piece = current_damage_percent * (self.enhance.damage_rise[j] - 1) * 100 / self.enhance.piece[j]
                self.result.append(increased_damage_per_piece)
                self.result_dic[increased_damage_per_piece] = [current , self.enhance.level_change[j] , current_damage_percent * (self.enhance.damage_rise[j] - 1) * 100 ]
                
        for i in range(len(self.mastery.name)):
            current = self.mastery.name[i]
            current_damage_percent = self.mastery.damage_percent[i]
            for j in range(len(self.mastery.piece)):
                increased_damage_per_piece = current_damage_percent * (self.mastery.damage_rise[current][j] - 1) * 100 / self.mastery.piece[j]
                self.result.append(increased_damage_per_piece)
                self.result_dic[increased_damage_per_piece] = [current , self.mastery.level_change[j] , current_damage_percent * (self.mastery.damage_rise[current][j] - 1) * 100]

        for i in range(len(self.skill.name)):
            current = self.skill.name[i]
            current_damage_percent = self.skill.damage_percent[i]
            for j in range(len(self.skill.piece)):
                increased_damage_per_piece = current_damage_percent * (self.skill.damage_rise[current][j] - 1) * 100 / self.skill.piece[j]
                self.result.append(increased_damage_per_piece)
                self.result_dic[increased_damage_per_piece] = [current , self.skill.level_change[j] , current_damage_percent * (self.skill.damage_rise[current][j] - 1) * 100]
        
        self.result.sort(reverse = True)

    def printresult(self): 
        currentnum = 0
        old = ""
        new = ""
        for i in range(len(self.result)):
            new = self.result_dic[self.result[i]][0]
            if i == 0:
                currentnum = self.result_dic[self.result[i]][1]
                old = self.result_dic[self.result[i]][0]
            elif old != new:
                print("스킬 :", old, "/", "레벨 :", currentnum)
                old = new
                currentnum = self.result_dic[self.result[i]][1]
            else:
                currentnum = self.result_dic[self.result[i]][1]

"""      
    def printresult_withnumber(self): 
        for i in range(len(self.result)):
            print(self.result_dic[self.result[i]][0] ," ", self.result_dic[self.result[i]][1] ," " ,self.result_dic[self.result[i]][2] ,"%" ,sep="")
"""
'''