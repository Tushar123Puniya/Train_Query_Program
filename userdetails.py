def write(username,password):
    file=open('user detail.txt','a')
    file.write(username+' '+password+'\n')
    
def read(username,password):
    file = open('user detail.txt','r')
    complete_file=file.read()
    store=complete_file.split('\n')
    search=username+' '+password
    for x in store:
        print(x,' ',search)
        if x==search:
            return True
    else:
        return False
