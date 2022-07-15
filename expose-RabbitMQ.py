import os
os.system('cmd /k " kubectl port-forward --namespace default svc/grafana 3000:3000"')
