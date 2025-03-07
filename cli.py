import time




#def algoritmo(a, b):
#    start = time.time()
#    time.sleep(1)
#    #print(f"El tiempo transcurrido fue {time.time() - start:.4f}")
#    return a + b

#algoritmo(5 , 3)

def timer_decorator(decorated_funtion):#Lo que a mi me interesa es la funcion que esta dentro de la funcion exterior, la funcion que estoy decorando es la funcion que estoy recibiendo.
    
    def decorator_wrapper(a, b):
        start = time.time()
        result = decorated_funtion(a, b)
        print(f"Tiempo: {time.time()-start:.4f}")
        #tengo que retorn el result para que pueda leer a y b en la funcion cuando la llame
        return result
    return decorator_wrapper
#algoritmo = timer_decorator(algoritmo)

@timer_decorator
def algoritmo(a, b):
    start = time.time()
    time.sleep(1)
    #print(f"El tiempo transcurrido fue {time.time() - start:.4f}")
    return a + b
algoritmo(1, 2)
    


