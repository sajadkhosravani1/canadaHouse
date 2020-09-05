from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Gets all imported JavaScript files in http://gopalsharma.ca/1000000-1500000/ page.'

    def handle(self, *args, **options):
        from bs4 import BeautifulSoup
        import html
        import requests
        from requests.exceptions import ConnectionError,HTTPError

        r = None
        try:
            r = requests.get("http://gopalsharma.ca/1000000-1500000")
            if r.status_code != 200:
                r.raise_for_status()
        except ConnectionError:
            self.stderr.write("Connection error")
            return
        except HTTPError as e:
            self.stderr.write(str(e))
            return


        content = html.unescape(r.text)
        soup = BeautifulSoup(content, 'html.parser')
        for scriptTag in soup.findAll('script'):
            if scriptTag.has_attr('src'):
                link = scriptTag.attrs['src']
                self.stdout.write(link)
            else:
                pass
