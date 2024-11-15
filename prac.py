txt = ("""pakistan is Bullshit , i have not seen more dogshit than them and they suck so hard that t
hey backfired at the people who fucked their own""")
maxWidth = int(input("Enter the max width per line: "))

txt_s = txt.split()
txt_l = list(txt_s)

print(len(txt_l))

print(txt_l[0:maxWidth])
print(txt_l[maxWidth:maxWidth+maxWidth])
print(txt_l[maxWidth+maxWidth:maxWidth+maxWidth+maxWidth+maxWidth])