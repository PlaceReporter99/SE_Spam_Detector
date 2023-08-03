def get_spam(site: str = "stackoverflow") -> str:
  true = True
  false = False
  json = eval(requests.get(f"https://api.stackexchange.com/2.3/questions?page=1&pagesize=30&order=desc&sort=creation&site={site}&filter=!Fc6b9*tI0e7rqpMIoRUAgp8tJ8").text)['items']
  spam = [x for x in json if re.search(r'(?:\d-*){10}',x['link'])]
  return '\n'.join(x['link'] for x in spam)

def actout(name: str, value: str) -> None:
  with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'{name}={value}', file=fh)

with open("sitename.txt") as f:
  actout("spam_links", get_spam(f.read().replace('\n','') or "stackoverflow").replace("\n","<br>"))
