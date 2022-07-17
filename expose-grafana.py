import os
os.system('cmd /k "kubectl port-forward --namespace monitoring svc/grafana 3000:3000"')
