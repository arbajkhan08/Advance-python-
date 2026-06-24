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
        