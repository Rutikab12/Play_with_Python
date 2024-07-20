#Youtube Manager App
import json

#load data into file in read mode
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test=json.load(file)
            #print(test)
            return test
    except FileNotFoundError:
        return []

# helper method for save functionality
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        return json.dump(videos,file)

#using enumerate cause of indexing is necessary for update and delete functionality
def list_all_videos(videos):
    for i,video in enumerate(videos,start=1):
        print(f"{i}. {video['name']}, Duration: {video['time']} ")
def add_video(videos):
    name=input("Enter video Name: ")
    time=input("Enter Video Time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected :(")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected :(")

def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update the youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the App ")
        choice = input("Enter the choice :")

        #match-case statement takes an expression and compares
        #its value to successive patterns given as one or more case blocks
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Option")

if __name__== "__main__":
    main()