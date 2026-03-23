# PartB.py

import unittest
from PartA import Artist, Song, Album, Playlist


class TestMusic(unittest.TestCase):

    # instance tests
    def test_artist_instance(self):
        a = Artist("Taylor", "1989", "USA")
        self.assertIsInstance(a, Artist)

    def test_song_instance(self):
        s = Song("Love Story", "Taylor", 2008)
        self.assertIsInstance(s, Song)

    def test_album_instance(self):
        al = Album("Fearless", "Taylor", 2008)
        self.assertIsInstance(al, Album)

    def test_playlist_instance(self):
        p = Playlist("My List")
        self.assertIsInstance(p, Playlist)

    # not instance tests
    def test_song_not_artist(self):
        s = Song("Love Story", "Taylor", 2008)
        self.assertNotIsInstance(s, Artist)

    def test_album_not_song(self):
        al = Album("Fearless", "Taylor", 2008)
        self.assertNotIsInstance(al, Song)

    def test_playlist_not_album(self):
        p = Playlist("List")
        self.assertNotIsInstance(p, Album)

    def test_artist_not_playlist(self):
        a = Artist("Taylor", "1989", "USA")
        self.assertNotIsInstance(a, Playlist)

    # identical tests
    def test_identical_objects(self):
        s1 = Song("Love Story", "Taylor", 2008)
        s2 = s1
        self.assertIs(s1, s2)

    def test_not_identical(self):
        s1 = Song("Love Story", "Taylor", 2008)
        s2 = Song("Love Story", "Taylor", 2008)
        self.assertIsNot(s1, s2)

    # add_song and add_album tests
    def test_add_song_album(self):
        al = Album("Fearless", "Taylor", 2008)
        al.add_song("Love Story", 2008)
        self.assertEqual(len(al.songs), 1)

    def test_add_song_artist(self):
        a = Artist("Taylor", "1989", "USA")
        s = Song("Love Story", "Taylor", 2008)
        a.add_song(s)
        self.assertEqual(len(a.songs), 1)

    def test_add_album(self):
        a = Artist("Taylor", "1989", "USA")
        al = Album("Fearless", "Taylor", 2008)
        a.add_album(al)
        self.assertEqual(len(a.albums), 1)

    def test_playlist_add_song(self):
        p = Playlist("Test")
        s = Song("Love Story", "Taylor", 2008)
        p.add_song(s)
        self.assertEqual(len(p.songs), 1)

    # sorting
    def test_sort_playlist(self):
        p = Playlist("Test")

        s1 = Song("B Song", "A", 2000)
        s2 = Song("A Song", "A", 2000)

        p.add_song(s1)
        p.add_song(s2)

        p.sort_playlist("ASC")

        self.assertEqual(p.songs[0].title, "A Song")

    # shuffle
    def test_shuffle_playlist(self):
        p = Playlist("Test")

        s1 = Song("Song1", "A", 2000)
        s2 = Song("Song2", "A", 2000)

        p.add_song(s1)
        p.add_song(s2)

        p.shuffle_playlist()

        self.assertEqual(len(p.songs), 2)


if __name__ == "__main__":
    unittest.main()