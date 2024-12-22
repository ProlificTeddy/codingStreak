"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

"""
def domain_name(url):
 
    # Remove protocol (http:// or https://)
    domain = url.replace("https://", "").replace("http://", "")
    
    # Remove www. if present
    domain = domain.replace("www.", "")
    
    # Get the first part of the remaining string (before any /)
    domain = domain.split('/')[0]
    
    # Get the domain name (part before the last dot)
    domain = domain.split('.')[0]
    
    return domain
