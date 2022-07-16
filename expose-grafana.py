import os
os.system('cmd /k " kubectl port-forward --namespace monitoring svc/rabbitmq 3000:3000"')
