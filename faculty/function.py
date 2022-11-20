import time
timestr = time.strftime("%Y%m%d-%H%M%S")
def handle_uploaded_file(f):  
    with open('faculty/files/'+timestr+".csv", 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    
    