

class PlaylistGenerator:
    def __init__(self):
        self.users = {}
        self.playlists = {}

    def register_user(self, username, password):
        if username not in self.users:
            self.users[username] = {'password': password}
            print(f"User {username} registered successfully.")
        else:
            print(f"Username {username} already exists. Please choose a different username.")

   
playlist_generator = PlaylistGenerator()

playlist_generator.register_user("User1", "password1")
playlist_generator.register_user("User2", "password2")

class PlaylistGenerator:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

    def generate_playlist(self):
        print("\nYour Playlist:")
        for index, song in enumerate(self.playlist, start=1):
            print(f"{index}. {song}")

    def collaborate(self):
        print("\nCollaborative Playlist Generator")
        while True:
            print("\n1. Add your Song\n2. Generate the Playlist\n3. Exit")
            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                song = input("Enter the song: ")
                self.add_song(song)
                print(f"{song} added to the playlist!")

            elif choice == "2":
                self.generate_playlist()
                print("You have created the wonderful Playlist")

            elif choice == "3":
                print("Signing off from the Playlist Generator.Take care!"
)
                break

            else:
                print("Invalid choice. Please enter a valid option.")
               

if __name__ == "__main__":
    playlist_generator = PlaylistGenerator()
    playlist_generator.collaborate()

