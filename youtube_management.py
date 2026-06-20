import json

def load_data():
  try:
    with open('youtube.txt','r') as file:
      test = json.load(file)
      print(type(test))
      return test
  except FileNotFoundError:
      return []
def save_data_helper(videos):
  with open('youtube.txt','w') as file:
   json.dump(videos,file)
def list_all_video(videos):
   for index,video in enumerate(videos,start = 1):
     print("/n")
   print(f"{index}.{video['name']}, Duration = {video['time']}")
def add_all_video(videos):
  name = input("enter video name:")
  time = input("enter video time:")
  videos.append({'name': name ,'time': time})
  save_data_helper(videos)
def update_all_video(videos):
  list_all_video(videos)
  index = input("enter the number to update:")
  if 1<= index <= len(videos):
    name = input ("enter the name:")
    time = input("enter the number:")
    videos[index-1] = {'name':name,'time':time}
    save_data_helper(videos)
else:
  print("invalid error")
 
def delete_all_video(videos):
  list_all_video(videos)
  index = input("enter the number to delete:")
  if 1<= index <= len(videos):
    del videos[index-1]
    save_data_helper(videos)
  else:
  print("invalid error")

def main():
 videos = load_data()
 while True:
    print("/Open a youtube video")
    print("1.list all youtube videos")
    print("2.add a youtube video")
    print("3.update a youtube video")
    print("4.delete a youtube video")
    print("5.exit the app")
    Choice = input("enter your choice")
    
    match Choice:
        case '1':
          list_all_video(videos)
        case '2':
          add_all_video(videos)
        case '3':
          update_all_video(videos)
        case '4':
          delete_all_video(videos)
        case '5':
          break
        case _:
          print("invalid choice")

if __name__ == "__main__" :
   main()  

'[{} ,{}]'
          