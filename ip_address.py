import os

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())
    
    marker = results.find('has address') + 12
    
    return results[marker:].splitlines()[0]
    # note colon following marker, without will display only first number of the IP
    
print(get_ip_address('google.com'))