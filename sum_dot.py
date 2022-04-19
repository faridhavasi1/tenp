def shpmr(n:str):    
    conter=0
    yek_n=['ز','ظ','ذ','ب','ن','ف','ض','خ','ج','غ']
    doo_n=['ت','ق','ی']
    seh_n=['چ','‍‍‍‍‍‍‍‍‍‍‍پ','ث','ش']

    for char in n.split():
        for i in char:
            if i in yek_n:
                conter=conter+1
                print(i)
            elif i in doo_n:
                conter=conter+2
                print(i)
            elif i in seh_n:
                conter=conter+3
                print(i)    
    print(conter)
shpmr('خدای مهربان')