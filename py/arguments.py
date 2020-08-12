def positionalarg(a,r):
    print("Name=",a)
    print("roll no=",r)
positionalarg(28,"manral")
def keywordarg(d,f):
    print("name=",f)
    print("roll no",d)
keywordarg(f=23,d="mukeshmanral")
def defaultarg(d,f="bhimtal"):
    print(d,f)
defaultarg("gehu")
defaultarg("gehu","dehradun")