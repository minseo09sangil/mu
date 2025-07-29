import streamlit as st

# 더 다양한 노래 데이터베이스
song_database = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "pop", "mood": "energetic"},
    {"title": "Someone Like You", "artist": "Adele", "genre": "pop", "mood": "sad"},
    {"title": "Lose Yourself", "artist": "Eminem", "genre": "hip-hop", "mood": "motivated"},
    {"title": "Peaches", "artist": "Justin Bieber", "genre": "r&b", "mood": "chill"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "genre": "pop", "mood": "romantic"},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": "rock", "mood": "epic"},
    {"title": "Numb", "artist": "Linkin Park", "genre": "rock", "mood": "angry"},
    {"title": "Levitating", "artist": "Dua Lipa", "genre": "pop", "mood": "happy"},
    {"title": "Sunflower", "artist": "Post Malone", "genre": "hip-hop", "mood": "chill"},
    {"title": "Uptown Funk", "artist": "Bruno Mars", "genre": "funk", "mood": "energetic"},
    {"title": "Thinking Out Loud", "artist": "Ed Sheeran", "genre": "pop", "mood": "romantic"},
    {"title": "Bad Guy", "artist": "Billie Eilish", "genre": "alternative", "mood": "dark"},
    {"title": "Viva La Vida", "artist": "Coldplay", "genre": "rock", "mood": "inspiring"},
    {"title": "Happy", "artist": "Pharrell Williams", "genre": "pop", "mood": "happy"},
    {"title": "Can’t Stop", "artist": "Red Hot Chili Peppers", "genre": "rock", "mood": "energetic"},
    {"title": "No Tears Left to Cry", "artist": "Ariana Grande", "genre": "pop", "mood": "hopeful"},
    {"title": "Finesse", "artist": "Bruno Mars", "genre": "funk", "mood": "fun"},
    {"title": "drivers license", "artist": "Olivia Rodrigo", "genre": "pop", "mood": "sad"},
    {"title": "All of Me", "artist": "John Legend", "genre": "r&b", "mood": "romantic"},
    {"title": "Don’t Start Now", "artist": "Dua Lipa", "genre": "pop", "mood": "confident"},
    {"title": "Stronger", "artist": "Kanye West", "genre": "hip-hop", "mood": "motivated"},
    {"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper", "genre": "pop", "mood": "dramatic"},
]

# 장르와 기분 리스트 자동 추출
genres = sorted(list(set(song["genre"] for song in song_database)))
moods = sorted(list(set(song["mood"] for song in song_database)))

st.title("🎵 노래 추천기")
st.write("당신의 취향과 기분에 맞는 노래를 추천해드릴게요!")

genre = st.selectbox("좋아하는 장르는?", genres)
mood = st.selectbox("현재 기분은?", moods)

if st.button("🎧 추천받기"):
    recommendations = [song for song in song_database if song["genre"] == genre and song["mood"] == mood]

    if recommendations:
        st.success(f"장르: {genre}, 기분: {mood} 에 맞는 추천 결과입니다!")
        for song in recommendations:
            st.markdown(f"- **{song['title']}** – *{song['artist']}*")
    else:
        st.warning("조건에 맞는 노래를 찾지 못했어요 😢 다른 조합을 시도해보세요.")
