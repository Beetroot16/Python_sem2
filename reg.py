import re 

# number = input("Enter your credit-card number: ")


# x = re.search("^[456]\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d$",number)
# if x:
#     print("GG")

Txt = '''Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
800-555-5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams
560-555-5153
806 1st St., Faketown AK 86847
laurawilliams@bogusemail.com

Corey Jefferson
900-555-9340
826 Elm St., Epicburg NE 10671
coreyjefferson@bogusemail.in'''

x = re.findall("\d\d\d-\d\d\d-\d\d\d\d",Txt)
y = re.findall("\S+@\S+",Txt)
# print(type(x))
print(x)
print(y)
