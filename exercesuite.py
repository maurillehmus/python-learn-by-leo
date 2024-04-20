def incluse(a,b):
    rep = False
    for i in a:
        if i in b:
            rep = True
        else:
            return False
        return rep
    
a = ("psa")
b = ("abcdpsxyz-+012")

ans = incluse(a,b)
print(ans)

def verifier_entier_valide(val, inf, sup):
    match inf, sup:
        case (None,None):
            return val.isnumeric()
        case (None, sup):
            return val.isnumeric() and int(val) <= sup
        case (inf, None):
            return val.isnumeric() and int(val) >= inf
        case (inf, sup):
            return val.isnumeric() and inf <= int(val) <= sup
        
print (verifier_entier_valide("123", 100, 200))
print (verifier_entier_valide("56", 400, 500))
print (verifier_entier_valide("123", 100, None))
print (verifier_entier_valide("123", None, 200))
print (verifier_entier_valide("123", None, None))
