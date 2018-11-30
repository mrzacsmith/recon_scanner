import urllib.request
# On C9.io an error is thrown, however using the command python3 robots_txt.py it should run without issue. 
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
        
    request = urllib.request.urlopen(path + 'robots.txt', data = None)
    data = io.TextIOWrapper(request, encoding = 'utf-8')
    return data.read()
    
print(get_robots_txt('https://www.reddit.com'))