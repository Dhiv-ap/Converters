import mysql.connector
import random
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oviya2722",
    database="music"
)
cur = con.cursor()
def recommend(language=None,n=5):
    if language:
        query = "SELECT title, artist, genre, link FROM songs WHERE language=%s"
        cur.execute(query, (language,))
    else:
        query = "SELECT title, artist, genre, link FROM songs"
        cur.execute(query)
    
    songs = cur.fetchall()
    if not songs:
        print("No songs found!")
        return
    
    playlist = random.sample(songs, min(n, len(songs)))
    print(f"\n🎶 Recommended Songs Playlist 🎶")
    print("-"*60)
    for s in playlist:
        print(f"🎵 {s[0]} by {s[1]} | Genre: {s[2]} | Link: {s[3]}")
print("=== Music Generator ===")
while True:
    lang = input("\nEnter language (English/Hindi/Korean/Tamil) or press Enter for mixed: ").strip()
    lang = lang if lang else None
    recommend(lang)
    
    choice = input("\nDo you want to generate another playlist? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("\n🎵 Thank you for using Music Generator! 🎵")
        break
con.close()
