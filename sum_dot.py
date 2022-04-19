def sum_no(n:str):
    yek_n=['ز','ظ','ذ','ب','ن','ف','ض','خ','ج','غ']
    doo_n=['ت','ق','ِِِِِِِِی']
    seh_n=['چ','پ','ژ','ث','ش']
    content_yek=0
    content_doo=0
    content_seh=0
    for i in n:
        if i not in yek_n and i not in doo_n and i not in seh_n:
            pass
        elif i in yek_n:
            yek=+1
            content_yek=+yek
            #print(i)
       
            print('yek',yek)
        elif i in doo_n:
            doo=+2
            content_doo=+doo
            #print(i)
      
            print('do:',doo)
        elif i in seh_n:
            seh=+3
            content_seh=+seh
            #print(i)
    
            print('seh:',seh)
        content_total=content_yek+content_doo+content_seh
    
    return (content_total)     
