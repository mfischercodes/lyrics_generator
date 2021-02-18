'''User chooses from a list of songs. Print out the lyrics to the chosen song'''

song_name_file_name_dictionary = {"Pokémon Theme Lyrics": "Pokémon_Theme_Lyrics", "Test song": "Test_song", "ETC...":"etc"}
songs_list = list(song_name_file_name_dictionary)

def print_songs_list(_songs_list = songs_list):
    for i in range(len(_songs_list)):
        print(f"{i+1}. {_songs_list[i]}")

def read_song():
    song_file = open(f"{song_name_file_name_dictionary[songs_list[users_song_choice - 1]]}.txt", 'r')
    read_lines = song_file.readlines()

    for line in read_lines:
        print(line.strip())
    
print_songs_list()
users_song_choice = int(input("Type in the song number you want to see the lyrics to: "))
read_song()


