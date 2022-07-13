import os
os.system('cmd /k " kubectl port-forward --namespace default svc/rabbitmq-0 5672:5672"')
