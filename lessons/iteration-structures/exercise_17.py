data = list(range(1, 101))  # Do not modify this line... I will know if you do!
log=[]
for i in data:
    temp=""
    if i%3==0:
        temp="Fizz"
    if i%5==0:
        temp+="Buzz"
    if len(temp)==0:
        temp="idk"
    log.append(temp)
print(log)
