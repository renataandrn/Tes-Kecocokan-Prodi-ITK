import streamlit as st

# Judul Aplikasi
st.title("Tes Kecocokan Program Studi - Institut Teknologi Kalimantan")

# Deskripsi singkat
st.write("""
Aplikasi ini membantu Anda menemukan program studi yang cocok berdasarkan minat dan preferensi Anda. 
Jawablah beberapa pertanyaan di bawah ini, dan kami akan memberikan rekomendasi program studi yang sesuai!
""")

# Pertanyaan Tes
st.write("### Pertanyaan")

# Slider untuk beberapa aspek minat
minat_matematika = st.slider('Seberapa besar ketertarikan Anda pada Matematika?', 0, 10, 5)
minat_teknologi = st.slider('Seberapa besar ketertarikan Anda pada Teknologi?', 0, 10, 5)
minat_informatika = st.slider('Seberapa besar ketertarikan Anda pada Ilmu Komputer dan Pemrograman?', 0, 10, 5)
minat_aktuaris = st.slider('Seberapa besar ketertarikan Anda pada Ilmu Aktuaria?', 0, 10, 5)
minat_desain = st.slider('Seberapa besar ketertarikan Anda pada Desain dan Seni Visual?', 0, 10, 5)
minat_fisika = st.slider('Seberapa besar ketertarikan Anda pada Fisika?', 0, 10, 5)
minat_kimia = st.slider('Seberapa besar ketertarikan Anda pada Kimia?', 0, 10, 5)
minat_bisnis = st.slider('Seberapa besar ketertarikan Anda pada Bisnis dan Manajemen?', 0, 10, 5)
minat_kelautan = st.slider('Seberapa besar ketertarikan Anda pada Ilmu Kelautan dan Teknik Perkapalan?', 0, 10, 5)
minat_rekayasa = st.slider('Seberapa besar ketertarikan Anda pada Teknik dan Rekayasa?', 0, 10, 5)

# Kalkulasi hasil berdasarkan jawaban
if st.button("Lihat Hasil"):
    if minat_matematika > 7:
        st.write("Program Studi yang cocok untuk Anda adalah: **Matematika**, **Statistika**, **Ilmu Aktuaria**.")
    elif minat_informatika > 7:
        st.write("Program Studi yang cocok untuk Anda adalah: **Informatika**, **Sistem Informasi**.")
    elif minat_teknologi > 7:
        st.write("Program Studi yang cocok untuk Anda adalah: **Teknik Mesin**, **Teknik Elektro**, **Teknik Kimia**.")
    elif minat_desain > 7:
        st.write("Program Studi yang cocok untuk Anda adalah: **Desain Komunikasi Visual**, **Arsitektur**.")
    elif minat_bisnis > 7:
        st.write("Program Studi yang cocok untuk Anda adalah: **Bisnis Digital**, **Teknik Logistik**.")
    elif minat_kelautan > 7:
        st.write("Program Studi yang cocok untuk Anda adalah: **Teknik Kelautan**, **Fisika Teknik Perkapalan**.")
    elif minat_fisika > 7 or minat_kimia > 7:
        st.write("Program Studi yang cocok untuk Anda adalah: **Fisika Teknik Perkapalan**, **Teknik Material dan Metalurgi**.")
    elif minat_rekayasa > 7:
        st.write("Program Studi yang cocok untuk Anda adalah: **Teknik Industri**, **Rekayasa Keselamatan**, **Teknik Sipil**, **Perencanaan Wilayah dan Kota**.")
    else:
        st.write("Anda mungkin tertarik untuk mengeksplorasi berbagai bidang lebih lanjut.")