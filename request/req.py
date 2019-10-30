import requests, json

localUrl = 'http://127.0.0.1:5000/'
remoteUrl = 'https://kidsbii.herokuapp.com/'

videoApi = 'api/videos/'
categoryApi = 'api/categories/'
quizApi = 'api/quizzes/'

def deleteAll(urlType, apiType, lastItemIndex):
  count = 0
  print('Delete item (~{0}) - {1}'.format(lastItemIndex, urlType + apiType))
  while count < lastItemIndex:
    res = requests.delete(urlType + apiType + str(count))
    print('{0}: deleted'.format(count))
    count += 1
  print('Done')

def addData(urlType, apiType, datas):
  headers = {
    'Content-Type': 'application/json'
  }

  print('Add new item - {0}'.format(urlType + apiType))
  for data in datas:
    # Input format you wanted
    newData = {
      'videoCategory': data['videoCategory'],
      'imageURL': data['imageUrl']
    }
    # -------------------------
    res = requests.post(url=urlType + apiType, headers=headers, data=json.dumps(newData))
    print(res)
    print('Added {0}'.format(str(newData)))

def main():
  # deleteAll (localUrl, categoryApi, 50)
  with open('datas.json', 'r', encoding='utf8') as datas:
    addData(localUrl, categoryApi, json.load(datas))

if __name__ == '__main__':
  main()