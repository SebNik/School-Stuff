def table(start,end,x):
    import math
    c=(x-start)/(end-start)
    count=3
    print('Step: ',1,'Value: ',start)
    print('Step: ',2,'Value: ',x)
    #print(end-start)
    #print(x-start)
    alt=x+c*(end-x)
    print('Step: ',count,'Value: ',alt)
    neu=0
    while math.ceil(neu)!=end:
        neu=alt+c*(end-alt)
        print('Step: ',count,'Value: ',neu)
        alt=neu
        count+=1

table(6,26,10)