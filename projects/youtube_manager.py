import json

filename='youtube.txt'
def load_data():
    try:
        with open(filename,'r') as file:
            test=json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(filename,'w') as file:
        return json.dump(videos ,file)
    
    
def list_all_videos(videos):
    print('\n')
    print('*'*100)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']} ,Duration : {video['time']}")
    print('*'*100)
    

def add_video(videos):
    name=input("Enter Video Name ")
    time=input("Enter Video Time ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update"))
    if 1<=index<= len(videos):
        name=input("Enter new Video name")
        time=input("Enter new Video time")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Index selected")

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter video number to be deleted"))
    if 1<=index<=len(videos):
        del(videos[index-1])
        save_data_helper(videos)
    else:
        print("Invalid Index selected")

def main():
    videos=load_data()
    while True:
        print("\nYOUTUBE MANAGER | Choose and option")
        print("1. List all Video: ")
        print("2. Add a youtube video: ")
        print("3. Update a youtube video details: ")
        print("4. Delete a youtube video: ")
        print("5. Exit the app: ")
        choice=input("Enter your choice: ")
        
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
                print("Invalid Choice")
                break

if __name__== "__main__":
    main()