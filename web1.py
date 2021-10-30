import os

s = input("Está utilizando qual sistema ?\nWindows[1]\nLinux[2]\n ")
if s == "1":
    site = input("Domínio: ")
    link = ("start chrome {}/robots.txt".format(site))
    link2 = ("start chrome {}/sitemap".format(site))
    os.system(link)
    os.system(link2)

if s == "2":
    site = input("Domínio: ")
    link = ("firefox {}/robots.txt".format(site))
    link2 = ("firefox {}/sitemap".format(site))
    os.system(link)
    os.system(link2)
    

