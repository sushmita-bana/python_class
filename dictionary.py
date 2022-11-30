contition=True
dict={}
while contition==True:

    dict_key=input('Enter the name: ')
    dict_value=input('Enter the DOB: ')

    if dict_key in dict:
        update_add=input('This user exist do u want to Update/Add : ')
        if update_add=='Update':
            dict[dict_key]=dict_value
            print(dict)
        else:
            list(dict[dict_key])
            dict[dict_key]=[dict[dict_key],dict_value]
            print(dict)
    else:
        dict[dict_key]=dict_value
        print(dict)
    y_n=input('Do you want to continue Yes/No: ')
    if y_n=='Yes':
        condition=True
        continue
    else:
        condition=False
        break

