weather=(1,0,0,0,1,0,1)
sunny=0
rainy=0
for i in range (0,7):
    if weather[i]==0:
        sunny=sunny+1
    else:
        rainy=rainy+1
if (sunny<rainy):
    print("its a good weather")
else:
    print("it is not a good weather")