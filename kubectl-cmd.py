import os
os.system('cmd /k " kubectl port-forward --namespace default svc/rabbitmq 15672:15672"')
