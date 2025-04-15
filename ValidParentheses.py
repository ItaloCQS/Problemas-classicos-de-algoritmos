class Solution(object):
    def isValid(self, s):
        lista = []
        conchetes = []
        parentese = []
        chaves = []
        for string in s:
            lista.append(string)
            
            if "[" in lista:
                conchetes.append("[")
                lista.remove("[") 
            if "]" in lista:
                conchetes.append("]")
                lista.remove("]") 
            elif "[" and "]" in conchetes:
                conchetes.remove("[")
                conchetes.remove("]")
                
            if "(" in lista:
                parentese.append("(")
                lista.remove("(") 
            if ")" in lista:
                parentese.append(")")
                lista.remove(")") 
            if "(" and ")" in parentese:
                parentese.remove("(")
                parentese.remove(")")
                
            if "{" in lista:
                chaves.append("{")
                lista.remove("{") 
            if "}" in lista:
                chaves.append("}")
                lista.remove("}") 
            if "{" and "}" in chaves:
                chaves.remove("{")
                chaves.remove("}")

        print(conchetes)
        print(parentese)
        print(chaves)
        
        if len(conchetes) + len(parentese) + len(chaves) > 0:
            return False
        else:
            return True
                
s = "([)]"
print(Solution().isValid(s))