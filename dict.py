me = {
    "firstname" : "Kris",
    "lastname" : "Burk",
    "birthdate" : 2001,
    "living" : "Kuressaare",
    "food" : "Pitsa"
    }
x = me.get("living")
print(x)

for z in me:
    print(me)

print(me["living"])
me["food"]  = "lasanje"
for y in me:
    print(me[y])
    
if "birthcert" in me:
    print("Jah isikukood on olemas")
else:
    print("Seda ei ole siin olemas")

print(len(me))

me["length"] = 186
me.pop("birthdate")



