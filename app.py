import streamlit as st

# 간단한 추천용 노래 데이터베이스
song_database = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "pop", "mood": "energetic"},
    {"title": "Someone Like You", "artist": "Adele", "genre": "pop", "mood": "sad"},
    {"title": "Lose Yourself", "artist": "Eminem", "genre": "hip-hop", "mood": "motivated"},
    {"title": "Peaches", "artist": "Justin Bieber", "genre": "r&b", "mood": "chill"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "genre": "pop", "mood": "romantic"},
]

st.title("🎵 노래 추천기")

genre = st.selectbox("좋아하는 장르는?", ["pop", "hip-hop", "r&b"])
mood = st.selectbox("현재 기분은?", ["energetic", "sad", "motivated", "chill", "romantic"])

if st.button("추천받기"):
    recommendations = [song for song in song_database if song["genre"] == genre and song["mood"] == mood]

    if recommendations:
        st.subheader("🎧 추천 노래:")
        for song in recommendations:
            st.write(f"**{song['title']}** - {song['artist']}")
    else:
        st.warning("해당 조건에 맞는 노래를 찾지 못했어요 😢")
