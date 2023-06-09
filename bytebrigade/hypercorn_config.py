bind = 'bytebrigade.net:443'
certfile = 'cert.crt'
keyfile = 'cert.key'
workers = 1
accesslog = '-'
errorlog = '-'
graceful_timeout = 60
keepalive_timeout = 5
forwarded_allow_ips = '*'
hsts = true
hsts_max_age = 31536000
hsts_include_subdomains = true