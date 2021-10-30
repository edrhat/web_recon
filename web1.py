import os

site = input("Domínio: ")
link = ("start chrome {}/robots.txt".format(site))
link2 = ("start chrome {}/sitemap".format(site))
os.system(link)
os.system(link2)
