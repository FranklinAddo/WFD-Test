# PartA.py

import random

# Song Class
class Song:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year

    def display_info(self):
        print("Song Title:", self.title)
        print("Artist:", self.artist_name)
        print("Year:", self.year)



# Album Class
class Album:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        self.songs = []

    def display_info(self):
        print("Album Title:", self.title)
        print("Artist:", self.artist_name)
        print("Year:", self.year)
        print("Songs in Album:")
        for song in self.songs:
            print(" ", song.title)

    def add_song(self, title, year):
        new_song = Song(title, self.artist_name, year)
        self.songs.append(new_song)


# Artist Class
class Artist:
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        self.albums = []
        self.songs = []

    def display_info(self):
        print("Artist:", self.name)
        print("Date of Birth:", self.dob)
        print("Country:", self.country)

        print("\nAlbums:")
        for album in self.albums:
            print(" ", album.title)

        print("\nSongs:")
        for song in self.songs:
            print(" ", song.title)

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)


# ------------------------
# Playlist Class
# ------------------------
class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_song(self):
        print("\nSongs in Playlist:")
        for song in self.songs:
            print(" ", song.title)

    def sort_playlist(self, order='ASC'):
        if order == 'ASC':
            self.songs.sort(key=lambda song: song.title)
        elif order == 'DES':
            self.songs.sort(key=lambda song: song.title, reverse=True)

    def shuffle_playlist(self):
        random.shuffle(self.songs)


# Demonstration Section

# Create an artist
artist = Artist("Taylor Swift", "13-12-1989", "USA")

# Create an album
album = Album("Speak Now", "Taylor Swift", 2008)

# Add songs to album
album.add_song("Love Story", 2008)
album.add_song("You Belong With Me", 2008)

# Add album to artist
artist.add_album(album)

# Add songs to artist
for song in album.songs:
    artist.add_song(song)

# Create playlist
playlist = Playlist("My Playlist")

# Add songs from album to playlist
for song in album.songs:
    playlist.add_song(song)

# Display information
print("\n--- Artist Info ---")
artist.display_info()

print("\n--- Album Info ---")
album.display_info()

print("\n--- Playlist ---")
playlist.print_all_song()

# Sort playlist
playlist.sort_playlist("ASC")
print("\n--- Ascending Playlist ---")
playlist.print_all_song()

playlist.sort_playlist("DES")
print("\n--- Descending Playlist ---")
playlist.print_all_song()

# Shuffle playlist
playlist.shuffle_playlist()
print("\n--- Shuffled Playlist ---")
playlist.print_all_song()