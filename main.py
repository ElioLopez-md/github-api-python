import json
import argparse
import requests

def main():
  base = "/orgs/freenet-group/repos?per_page=100"
  server = "https://api.github.com"
  url = server + base

  parser = argparse.ArgumentParser()

  parser.add_argument(
      "-u",
      "--user",
      default="",
      help="Specify the username to log into github")

  parser.add_argument(
      "-t",
      "--token",
      default="",
      help="Specify the token to use github")

  options = parser.parse_args()

#API query to get a json answer
#  r = requests.get(url, auth = (options.user, options.token))
#  dump = r.json()
  dump = requests.get(url, auth = (options.user, options.token)).json()

#with this query you can see the structure fetched
  print(json.dumps(dump[1], indent=4, sort_keys=True))

#with this on you can iterate through first page answer
  for index in range(0,len(dump)):
    print(json.dumps(dump[index]['id']), " ", dump[index]['full_name'])

#with this on you get a second poage answer and parse it
  url = url + "&page=2"
  dump = requests.get(url, auth = (options.user, options.token)).json()

  for index in range(0,len(dump)):
    print(json.dumps(dump[index]['id']), " ", dump[index]['full_name'])

if __name__ == "__main__":
    main()
