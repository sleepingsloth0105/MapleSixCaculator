'''
제작자 email : 6zzzzzz610@gmail.com 
각종 문의(오류, 요청사항 등)은 이메일로 보내주세요
'''
import os
'''Class Enhance , Mastery , Skill은 각각 강화코어, 마스터리 코어 , 6차스킬코어의
이름 , 딜지분 , 딜 상승률 , 10레벨 단위 딜 상승률 , 레벨 당 소각 소모량 , 10레벨 당 조각 소모량 정보를 가지고 있다.
'''
class Enhance: # 5차 강화 코어
    def __init__(self):
        self.name = []
        self.damage_percent = []
        self.damage_rise = [ 111/100 , 112/111 , 113/112 , 114/113 , 115/114 , 116/115 , 117/116 , 118/117 , 119/118 , 125/119 , 126/125 , 
                        127/126 , 128/127 , 129/128 , 130/129 , 131/130 , 132/131 , 133/132 , 134/133 , 140/134 , 141/140, 
                        142/141, 143/142 , 144/143 , 145/144 , 146/145 , 147/146 , 148/147 , 149/148 , 160/149, 1 ]
        #self.damage = [100 , 111 , 112 , 113 , 114 , 115 , 116 , 117 , 118 , 119 , 125 , 126 , 127 , 128 , 129 , 130 , 131 , 132 ,133 , 134 , 140 , 141 , 142 , 143 , 144 , 145 , 146 , 147 , 148 , 149 , 160]
        self.sol_erda = [ 4,1,1,1,1,2,2,2,3,3,8,3,3,3,3,3,3,3,3,4,12,4,4,4,4,4,5,5,5,6,15,100]
        self.level= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    
    def addname(self, newname):
        self.name.append(newname)   
    def adddamagepercent(self,newdamage):
        self.damage_percent.append(newdamage)
        
class Mastery: # 마스터리 코어
    def __init__(self):
        self.name = []
        self.damage_percent = []
        self.damage_rise = {}
        #self.damage = {}
        self.sol_erda = [ 1,1,1,2,2,2,3,3,10,3,3,4,4,4,4,4,4,5,15,5,5,5,5,5,6,6,6,7,20,100] 
        self.level = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    
    def addname(self, newname):
        self.name.append(newname)   
    def adddamagepercent(self,newdamage):
        self.damage_percent.append(newdamage)
    def adddamagerise(self,skillname,newdmgrise):
        self.damage_rise[skillname] = newdmgrise
    #def adddamage(self,skillname,first,incresing):
    #    self.damage[skillname] = [first , incresing]
        
class Skill: # 6차 스킬 (오리진 등등)
    def __init__(self):
        self.name = []
        self.damage_percent = []
        self.damage_rise = {}
        #self.damage = {}
        self.sol_erda = [ 1,1,1,2,2,2,3,3,10,3,3,4,4,4,4,4,4,5,15,5,5,5,5,5,6,6,6,7,20,100 ] 
        self.level = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        
    def addname(self, newname):
        self.name.append(newname)   
    def adddamagepercent(self,newdamage):
        self.damage_percent.append(newdamage)
    def adddamagerise(self,skillname,newdmgrise):
        self.damage_rise[skillname] = newdmgrise
    #def adddamage(self,skillname,first,incresing):
    #    self.damage[skillname] = [first , incresing]
''' class CharacterV2_1는 효율과 관련된 모든 연산을 담아둔 class이다.'''        
class CharacterV2_1:
    def __init__(self,bossdamage,ignoredef):
        self.current_enhance = []
        self.current_mastery = []
        self.current_skill = []
        self.enhanceinfo = Enhance()
        self.masteryinfo = Mastery()
        self.skillinfo = Skill()
        self.bossdmg = 100 + bossdamage
        self.ignoredef=ignoredef
    
    ''' 강화 코어 정보 추가 '''
    def enhance_addname_and_level(self,newname,level = 0):
        self.enhanceinfo.addname(newname)
        self.current_enhance.append(int(level))
    def enhance_adddamagepercent(self,newdmgper):
        self.enhanceinfo.adddamagepercent(newdmgper)
        
    '''마스터리 코어 정보 추가'''    
    def mastery_addname_and_level(self,newname,level=1):
        self.masteryinfo.addname(newname)
        self.current_mastery.append(int(level))
    def mastery_adddamagepercent(self,newdmgper):
        self.masteryinfo.adddamagepercent(newdmgper)
    def mastery_adddamagerise(self,skillname,firstleveldmg,increaseddmg):
        dmgrise = []
        old = firstleveldmg + increaseddmg
        for i in range(29):
            new = old + increaseddmg
            newdmg = new / old
            dmgrise.append(newdmg)
            old = new
        dmgrise.append(1)
        self.masteryinfo.adddamagerise(skillname,dmgrise)
        #self.masteryinfo.adddamage(skillname, firstleveldmg , increaseddmg)
    
    '''스킬 코어 정보 추가'''
    def skill_addname_and_level(self,newname,level=1):
        self.skillinfo.addname(newname)
        self.current_skill.append(int(level))
    def skill_adddamagepercent(self,newdmgper):
        self.skillinfo.adddamagepercent(newdmgper)
    def skill_adddamagerise(self,skillname,firstleveldmg,increaseddmg):
        dmgrise = []
        old = firstleveldmg + increaseddmg
        for i in range(29):
            new = old + increaseddmg
            newdmg = new / old
            dmgrise.append(newdmg)
            old = new
        dmgrise.append(1)
        self.skillinfo.adddamagerise(skillname,dmgrise)
        #self.skillinfo.adddamage(skillname,firstleveldmg,increaseddmg)
        self.skillinfo.damage_rise[skillname][8] = self.skillinfo.damage_rise[skillname][8] * self.calcdef20()
        self.skillinfo.damage_rise[skillname][18] = self.skillinfo.damage_rise[skillname][18] * self.calcboss20()
        self.skillinfo.damage_rise[skillname][28] =  self.skillinfo.damage_rise[skillname][28] * self.calcboss50() * self.calcdef50()
    
        
    '''오리진스킬 보공 효율 계산'''    
    def calcboss20(self):
        newdmg = self.bossdmg + 20
        return newdmg / self.bossdmg
    def calcboss50(self):
        newdmg = self.bossdmg + 50
        return newdmg / self.bossdmg
    
    '''오리진스킬 방무 효율 계산'''
    def calcdef20(self):
        oldignoredef = (1 - (self.ignoredef/100))
        newignoredef = (1 - (self.ignoredef/100)) * (1 - 0.2)
        recentdmg = (1 - ( 3.8 * oldignoredef)) 
        newdmg = (1 - ( 3.8 * newignoredef)) 
        return newdmg / recentdmg
    def calcdef50(self):
        oldignoredef = (1 - (self.ignoredef/100))
        newignoredef = (1 - (self.ignoredef/100)) * (1 - 0.5)
        recentdmg = (1 - ( 3.8 * oldignoredef)) 
        newdmg = (1 - ( 3.8 * newignoredef)) 
        return newdmg / recentdmg

    '''
    입력받은 딜지분을 5차 강화코어는 0레벨, 나머지 코어는 1레벨 기준 딜지분으로 변화시키는 함수
    각각의 강화코어의 현재 레벨을 확인하고 , 강화코어가 0레벨, 나머지 코어가 1레벨이 아닐 경우
    updatedmgpercent(유형, 인덱스)를 실행해 기존 딜지분을 새로운 딜지분으로 변경
       
    def dmgpercheck(self):
        for index in range(len(self.current_enhance)):
            if self.current_enhance[index] != 0:
                self.updatedmgpercent('enhance', index)
        for index in range(len(self.current_mastery)):
            if self.current_mastery[index] != 1:
                self.updatedmgpercent('mastery', index)
        for index in range(len(self.current_skill)):
            if self.current_skill[index] != 1:
                self.updatedmgpercent('skill', index)
        
    
    기존 n레벨 딜지분을 새로운 초기레벨 기준 딜지분으로 바꿔주는 함수
    계산식은 다음과 같다.
    1) 기존의 데미지 / 딜지분을 해서 딜지분의 1%에 해당하는 값을 구한다.
    ex) 데미지가 100이고 딜지분이 10%일 경우 딜지분의 1%에 해당하는 값은 100 / 10 = 10이다
    2) 1의 결과에 100을 곱해 100% 딜지분의 값을 구한다.
    ex) 10 * 100 = 1000 , 전체 딜은 1000으로 볼 수 있다.
    3) 전체 데미지 - 해당 스킬의 데미지를 통해 해당 스킬을 제외한 나머지 스킬의 데미지를 구한다.
    ex) 1000 - 100 = 900
    4) 스킬의 초기 데미지 / 나머지 스킬의 데미지 + 초기 데미지를 계산해 새로운 딜지분을 구한다.
    ex) 초기 데미지를 95라 하면 , 95 / 95+900 = 0.0954773867 = 새로운 딜지분
    
    def updatedmgpercent(self, coretype , index):
        if coretype == 'enhance':
            olddmgper = self.enhanceinfo.damage_percent[index]
            recentdmg = self.enhanceinfo.damage[self.current_enhance[index]]
            per1dmg = recentdmg / ( olddmgper * 100)
            per100dmg = per1dmg * 100
            otherskilldmg = per100dmg - recentdmg
            newdmgper = self.enhanceinfo.damage[0] / (self.enhanceinfo.damage[0] + otherskilldmg)
            self.enhanceinfo.damage_percent[index] = newdmgper
        elif coretype == 'mastery':
            olddmgper = self.masteryinfo.damage_percent[index]
            count = 0
            recentdmg = self.masteryinfo.damage[self.masteryinfo.name[index]][0]
            while count != self.current_mastery[index]:
                recentdmg += self.masteryinfo.damage[self.masteryinfo.name[index]][1]
                count += 1
            per1dmg = recentdmg / ( olddmgper * 100)
            per100dmg = per1dmg * 100
            otherskilldmg = per100dmg - recentdmg
            newdmgper = self.masteryinfo.damage[self.masteryinfo.name[index]][0] / (self.masteryinfo.damage[self.masteryinfo.name[index]][0] + otherskilldmg)
            self.masteryinfo.damage_percent[index] = newdmgper
        else:
            olddmgper = self.skillinfo.damage_percent[index]
            count = 0
            recentdmg = self.skillinfo.damage[self.skillinfo.name[index]][0]
            while count != self.current_skill[index]:
                recentdmg += self.skillinfo.damage[self.skillinfo.name[index]][1]
                count += 1
            per1dmg = recentdmg / ( olddmgper * 100)
            per100dmg = per1dmg * 100
            otherskilldmg = per100dmg - recentdmg
            newdmgper = self.skillinfo.damage[self.skillinfo.name[index]][0] / (self.skillinfo.damage[self.skillinfo.name[index]][0] + otherskilldmg)
            self.skillinfo.damage_percent[index] = newdmgper     
    '''        
                    
    ''' 
    1레벨 단위가장 효율적인 스킬 레벨업 계산
    각 강화 코어 , 마스터리 코어 , 스킬 코어에 대해
    특정 스킬의 현재 레벨을 탐색하고 그 레벨에서 레벨업 했을 때의 딜 상승률을 찾아
    (해당 스킬의 딜지분) * (딜 상승률) / (레벨업에 필요한 조각) 연산을 시행해 조각 1개당 딜상승률을 찾은 뒤
    result에 조각당 딜 상승률을 저장하고 result_dic에 코어의 유형 , index , 레벨업한 레벨 , 스킬 이름을 저장한다.
    그리고 result에 저장된 값과 사전에 계산된 10레벨 기준으로 계산된 효율을 모두 합해 최고의 효율을 찾은 뒤
    그 효율에 관련된 result_dic에 담긴 정보를 반환한다.
    '''    
    def calculate(self):
        result = []
        result_dic = {}
        for i in range(len(self.current_enhance)):
            nextlevel = self.current_enhance[i] + 1
            idx = self.enhanceinfo.level.index(nextlevel)
            add = self.enhanceinfo.damage_percent[i] * (self.enhanceinfo.damage_rise[idx]-1) / self.enhanceinfo.sol_erda[idx]
            result.append(add)
            result_dic[add] = ['enhance',i,nextlevel,self.enhanceinfo.name[i]]
            currentlevel = self.current_enhance[i] + 1
            level10dmg = 1
            level10sol_erda = 0
            while currentlevel % 10 != 1 and currentlevel <= 30:
                level10idx = self.enhanceinfo.level.index(currentlevel)
                level10dmg *= self.enhanceinfo.damage_rise[level10idx]
                level10sol_erda += self.enhanceinfo.sol_erda[level10idx]
                currentlevel += 1
                if currentlevel % 10 == 1:
                    add10 = self.enhanceinfo.damage_percent[i] * (level10dmg - 1) /level10sol_erda
                    result.append(add10)
                    result_dic[add10] = ['enhance', i, currentlevel-1, self.enhanceinfo.name[i]]
                    level10dmg = 1
                    level10sol_erda = 0
            
            
        for i in range(len(self.current_mastery)):
            nextlevel = self.current_mastery[i] + 1
            idx = self.masteryinfo.level.index(nextlevel)
            add = self.masteryinfo.damage_percent[i] * (self.masteryinfo.damage_rise[self.masteryinfo.name[i]][idx]-1) / self.masteryinfo.sol_erda[idx]
            result.append(add)
            result_dic[add] = ['mastery',i,nextlevel,self.masteryinfo.name[i]]
            currentlevel = self.current_mastery[i] + 1
            level10dmg = 1
            level10sol_erda = 0
            while currentlevel % 10 != 0 and currentlevel <= 30:
                level10idx = self.masteryinfo.level.index(currentlevel)
                level10dmg *= self.masteryinfo.damage_rise[self.masteryinfo.name[i]][level10idx]
                level10sol_erda += self.masteryinfo.sol_erda[level10idx]
                currentlevel += 1
                if currentlevel % 10 == 0: 
                    add10 = self.masteryinfo.damage_percent[i] * (level10dmg - 1) /level10sol_erda
                    result.append(add10)
                    result_dic[add10] = ['mastery', i, currentlevel-1, self.masteryinfo.name[i]]
                    level10dmg = 1
                    level10sol_erda = 0
                     
            
        for i in range(len(self.current_skill)):
            nextlevel = self.current_skill[i] + 1
            idx = self.skillinfo.level.index(nextlevel)
            add = self.skillinfo.damage_percent[i] * (self.skillinfo.damage_rise[self.skillinfo.name[i]][idx]-1) / self.skillinfo.sol_erda[idx]
            result.append(add)
            result_dic[add] = ['skill',i,nextlevel,self.skillinfo.name[i]]
            currentlevel = self.current_skill[i] + 1
            level10dmg = 1
            level10sol_erda = 0
            while currentlevel % 10 != 1 and currentlevel <= 30:
                level10idx = self.skillinfo.level.index(currentlevel)
                level10dmg *= self.skillinfo.damage_rise[self.skillinfo.name[i]][level10idx]
                level10sol_erda += self.skillinfo.sol_erda[level10idx]
                currentlevel += 1
                if currentlevel % 10 == 1:
                    add10 = self.skillinfo.damage_percent[i] * (level10dmg - 1) /level10sol_erda
                    result.append(add10)
                    result_dic[add10] = ['skill', i, currentlevel-1, self.skillinfo.name[i]]     
                    level10dmg = 1
                    level10sol_erda = 0      
            
            
        maxresult = max(result)
        if maxresult == 0:
            return 0
        else:
            return result_dic[maxresult]
    '''
    캐릭터 레벨 업
    calculator의 결과값 list를 입력받아서
    현재 캐릭터가 가진 스킬 레벨을 변화시킨다.
    '''        
    def levelup(self,calcresult):
        if calcresult[0] == 'enhance':
            self.current_enhance[calcresult[1]] = calcresult[2]         
        elif calcresult[0] == 'mastery':
            self.current_mastery[calcresult[1]] = calcresult[2]  
        else:
            self.current_skill[calcresult[1]] = calcresult[2]
    ''' 만랩까지 반복
    효율 계산을 만렙이 될 때 까지 반복하는 함수이다.
    return 값인 record에는 강화해야할 순서가 [스킬이름, 레벨]의 형태로 저장된다.
    예를 들어 폭시를 5레벨까지 -> 잔시를 2레벨까지 -> 오리진을 2레벨까지가 강화 순서라면
    [[폭시,5] , [잔시,2] , [오리진,2]]와 같이 저장된다.
    calculate10을 실행해 10레벨 효율을 계산한 뒤
    만약 calculate의 값이 0이 아니라면 == 만렙이 아니라면
    calculate의 결과를 calinfo에 저장한다.
    만약 기존의 이름과 새로 들어온 이름이 다르다면 강화해야 할 스킬이 변한 것이므로
    현재 강화해야 할 스킬의 이름과 단계를 record에 저장하고, 과거의 이름과 스킬 단계를 저장해둔다.
    만약 기존에 저장되어 있던 이름과 새로 들어온 이름이 같다면 레벨만을 변경한다.
    그리고 변경한 레벨을 levelup함수를 이용해 변경한다.
    만약 이번 시행으로 만렙이 된다면, 그 값을 저장하고 반복문을 벗어난다.
    이후 record를 리턴값으로 반환한다.
    ''' 
    def levelup_max(self):
        #self.dmgpercheck()
        record = []
        oldskillname = "시작"
        arrivelevel = 0
        startlevel = 0
        while self.calculate() != 0:
            calcinfo = self.calculate()
            newskillname = calcinfo[3]
            if newskillname != oldskillname:
                record.append([oldskillname , startlevel , arrivelevel])
                oldskillname = newskillname
                if calcinfo[0] == 'enhance':
                    startlevel = self.current_enhance[calcinfo[1]]         
                elif calcinfo[0] == 'mastery':
                    startlevel = self.current_mastery[calcinfo[1]]  
                else:
                    startlevel = self.current_skill[calcinfo[1]]             
                arrivelevel = calcinfo[2]     
            else:
                arrivelevel = calcinfo[2]
            self.levelup(calcinfo)
            if self.calculate() == 0:
                record.append([oldskillname, startlevel,arrivelevel])
        return record
   
    '''
    출력
    외부에서 효율을 계산할 때 사용할 함수
    levelup_max의 결과값을 같은 폴더의 result.txt.에 저장한다.
    '''
    def printresult(self):
        result = self.levelup_max()
        recentdir = os.path.dirname(os.path.realpath(__file__))
        usedir = recentdir + "/스킬트리(조각).txt"
        resultfile = open(usedir, 'w')
        for i in range(len(result)):
            data = "스킬 : " +  result[i][0]  + " / 레벨 : "  + str(result[i][1]) + " -> " + str(result[i][2])
            print(data)
            resultfile.write(data)
            resultfile.write('\n')
        resultfile.close()