<<<<<<< HEAD
def http_status(status):
    match status:
        case 200:
              return "ok"
        
        case 404:
              return "Not found"
        
        case 200:
              return "internal servern Error"
        
        case __:
              return"Unknown status"
         
print(http_status(10100))       
print(http_status(200))  
=======
def http_status(status):
    match status:
        case 200:
              return "ok"
        
        case 404:
              return "Not found"
        
        case 200:
              return "internal servern Error"
        
        case __:
              return"Unknown status"
         
print(http_status(10100))       
print(http_status(200))  
>>>>>>> f6f7fac5c49720125f1c8cd565a352fcb902095d
        