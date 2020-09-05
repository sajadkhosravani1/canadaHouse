from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Gets all imported JavaScript files in http://gopalsharma.ca/1000000-1500000/ page.'

    def handle(self, *args, **options):
        from bs4 import BeautifulSoup
        import re
        import html
        import requests

        # r = requests.get("http://gopalsharma.ca/1000000-1500000/")
        # content = html.unescape(r.text)
        # f = open("allContents.html", 'w+')
        # f.write(content)
        # f.close()


        content = open("allContents.html",'r').read()
        soup = BeautifulSoup(content, 'html.parser')
        for scriptTag in soup.findAll('script'):
            if scriptTag.has_attr('src'):
                link = scriptTag.attrs['src']
                # if not link.startswith('http'): link=rootPath+re.search('[^\/]+.+','//use.edgefonts.net/source-sans-pro:n4.js?ver=1').group()
                self.stdout.write(link)
            else:
                # f.write(scriptTag.__str__())
                pass
