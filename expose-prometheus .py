import os
os.system('cmd /k "kubectl port-forward --namespace monitoring svc/prometheus-server 80:80"')
