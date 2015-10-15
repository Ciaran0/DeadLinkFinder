import click
import requests
import httplib
import re

@click.command()
@click.argument('files', type=click.File())
def scan(files):
    """Program that scans files for dead links"""
    str = files.read()
    urls = re.findall(r'(https?://\S+|www.\S+)', str)
    deadUrls = list()
    for url in urls:
       if(not "http" in url):
          url = "http://"+url
       try:
         r = requests.head(url)
         if r.status_code != 200:
           deadUrls.append(url)
       except requests.exceptions.ConnectionError:
   	 deadUrls.append(url)
    click.echo("Urls that may not be working:")
    click.echo(deadUrls)

if __name__ == '__main__':
    scan()
