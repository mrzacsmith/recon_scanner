from tld import get_fld

def get_domin_name(url):
    
    domain_name = get_fld(url)
    return domain_name
    
# print(get_domin_name('https://www.facebook.com'))