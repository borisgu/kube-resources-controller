import json

with open('/opt/config.json', 'r') as f:
    config = json.load(f)

# Assign configuration values
# Namespace labels in use
name = config['namespace_labels']['name']
created = config['namespace_labels']['created']
stopped = config['namespace_labels']['stopped']
started = config['namespace_labels']['started']
worktime = config['namespace_labels']['worktime']
exception = config['namespace_labels']['exception']
owner = config['namespace_labels']['owner']
status = config['namespace_labels']['status']
ttl = config['namespace_labels']['ttl']
ignored_namespaces = config['ignored_resources']['namespaces']

# Resources limits config
max_replicas = config['resources_limits']['max_pod_replicas']

# App metadata config
app_name = config['app_info']['name']
version = config['app_info']['version']

# Kubernetes API configuration
request_timeout = config['kube_api_config']['request_timeout']
kube_mode = config['kube_api_config']['config_mode']
deletion_candidate_deployment = config['resources_control']['delete_deployment']