Grades={"suma":1,"Naresh":2,"Lekha":3,"Archana":4}
suma_grade=Grades["suma"]
print suma_grade
try:
    kate_grade=Grades["Kate"]
except KeyError:
    print "No grade for Kate!"

#You can check for existence
ramesh_has_grade="Ramesh" in Grades
sumagrade=Grades.get("suma",0)
print sumagrade
rameshgrade=Grades.get("ramesh",None)
print rameshgrade

#Manipuation

Grades["Lekha"]=5
lekha_grade=Grades["Lekha"]
print lekha_grade

Grades["Kate"]=6
Kate_grade=Grades["Kate"]
print Kate_grade



profile={"user":"suma",
         "text":"Data Science is Awesome",
         "retweet_count":180,
         "hashtags":["#data","#science","#datascience"]
         }
profile_keys=profile.keys()
print profile_keys
prifile_values=profile.values()
print prifile_values
profile_items=profile.items()
print profile_items
         
