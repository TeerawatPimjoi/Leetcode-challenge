class Solution:
    def isValid(self, s: str) -> bool:
        openb ={'(','[','{'}
        closeb={')',']','}'}
        store=[]
        
        for c in s:
            if c in openb : store.append(c)
            elif c in closeb :
                if len(store)==0 :return False
                if store[-1]=="{" and c =='}' :store.pop(-1)
                elif store[-1]=="{" and c !='}' :return False
                    
                elif store[-1]=="[" and c ==']' :store.pop(-1)
                elif store[-1]=="[" and c !=']' :return False
                
                elif store[-1]=="(" and c ==")": store.pop(-1)
                elif store[-1]=="(" and c !=')' :return False
        if len(store)==0 :return True;
        if len(store)!=0:return False;