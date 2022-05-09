import requests


   
subdomains = {
    'm',
    'blog',
    'support',
    'wiki',
    'kb',
    'help',
    'info',
    'admin',
    'static',
    'api',
    'dev',
    'events',
    'feeds',
    'forums',
    'groups',
    'img',
    'media',
    'news',
    'sites',
    'mysql',
    'store',
    'vpn',
    'beta',
    'photos',
    'files',
    'resources',
    'secure',
    'ssl',
    'apps',
    'pic',
    'status',
    'mobile',
    'search',
    'live',
    'videos',
    'lists',
}





class sublist():

    def make_url(target):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

        urls = target
        discovered_urls = []
        for url in urls:
            for subdomain in subdomains:
               
                # construct the url
                url = f"http://{subdomain}.{urls}"
                
                try:
                    r = requests.get(url, timeout=0.3,headers=headers)
                    stat = r.status_code
                    
                    if stat == 200:
                        data = url
                        
                        discovered_urls.append(data)
                        
    
                except:
                    pass
            results = discovered_urls
            return results

