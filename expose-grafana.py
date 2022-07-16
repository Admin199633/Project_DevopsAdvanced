import os
os.system('cmd /k "kubectl port-forward --namespace monitoring svc/grafana 80"')
