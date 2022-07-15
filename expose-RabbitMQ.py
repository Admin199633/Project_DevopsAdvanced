import os
os.system('cmd /k " kubectl port-forward --namespace default svc/raabitmq 5672:5672"')
