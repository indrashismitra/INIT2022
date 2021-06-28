from random import randint
entering = True
songs = []
while entering:
    entered = input("enter song name or enter 'END' to signify finishing\n")
    if entered == "END":
        entering = False
    else:
        songs.append(entered)
print(str(len(songs)) + " songs available")
num = input("enter a number up to or including " + str(len(songs)))
print(num)

playlist = []
for i in range(int(num)):
    playlist.append(songs[randint(0,int(num)-1)])

print("Your playlist")
for i in range(len(playlist)):
    print(playlist[i])