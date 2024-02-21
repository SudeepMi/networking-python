# Create a Python script to perform a basic security scan on a web application. Check for common vulnerabilities such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF)


import requests

def web_security_scan(url):
   response = requests.get(url)
   print("Scanning: "+url)
   if "SQL error" in response.text:
       print("SQL Injection vulnerability found!")
   else:
       print("X SQL Injection vulnerability not found!")
   if "<script>alert('XSS')</script>" in response.text:
       print("Cross-Site Scripting (XSS) vulnerability found!")
   else:
       print("X Cross-Site Scripting (XSS) vulnerability not found")
       

web_security_scan("https://nagarjunaictclub.com")