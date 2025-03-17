
## hrd_v1.ipynb

pada program pertama ini, ai sudah bisa menjawab pertanyaannya
tapi karena masih kosong banget, kek mentah bland gitu.

maka tidak ada semacam limitasi nya. sehingga ai akan ngalor ngidul menanyakan tanpa henti. 
diperlukan sebuah cara memberikan limitasi pertanyaan yang akan diberikan.

## hrd_v2.ipynb

ai hrd yang bisa membaca file pdf, dengan input file pdf ke prompt nya

pada hrd v2, ini. sebenarnya sudah memasukkan cara untuk mengakhiri wawancara ini. 
tapi karena terlalu hard code, dengan cara. jika balasan mengandung kata 

"terima kasih" atau "wawancara selesai"

percakapan akan diakhiri

ada kekurangan, ketika aku mencoba nya. baru aja perkenalan, dan ai nya membalas dengan baik

> 🤖 HRD: Terima kasih, Reza. Senang berkenalan dengan Anda! Mari kita mulai wawancara ini.

> Dari CV Anda, saya melihat bahwa Anda memiliki pengalaman sebagai Front-End Developer dalam proyek chatbot untuk SDPPI Kominfo. Bisa Anda ceritakan lebih lanjut tentang tantangan yang Anda hadapi dalam proyek tersebut dan bagaimana Anda mengatasinya?

baru aja mulai sudah selesai. ckckckck. 

saran : 
> pengambilan keputusan diserahkan ke ai, dengan output nilai boolean

## hrd_v3.ipynb

ini sudah mulai lebih baik
format output yang dihasilkan adalah json
dengna struktur

``` language:json
    {{
        "response": "<jawaban AI>",
        "is_finish": <true/false>
    }}
```


> mulai dari sekarang akan ditulis di file python langsung demi kemudahan testing

yang sebaiknya perlu ditambahkan di hrd_v4

- pertanyaannya lebih bagus
- menghasilkan json yang lebih baik
- mencoba menggunakan list pertanyaan

## hrd_v4.py

hasil awal ketika pakai kode langsung copas dari chat gpt jelek parah

```
    Kandidat: halo perkenalkan nama saya reza bisa dipanggil reza
HRD: Tentu! Berikut adalah beberapa pertanyaan yang dapat Anda gunakan dalam wawancara untuk topik yang telah Anda sebutkan:

### Latar Belakang
1. "Bisa ceritakan sedikit tentang latar belakang pendidikan dan pengalaman kerja Anda? Apa yang menurut Anda paling membentuk diri Anda hingga saat ini?"
2. "Apa yang membuat Anda memilih jalur karier yang Anda ambil? Adakah pengalaman tertentu yang sangat berkesan bagi Anda?"
3. "Bagaimana perjalanan karier Anda sejauh ini? Apakah ada pengalaman atau tantangan khusus yang ingin Anda bagikan?"

### Ketertarikan pada Posisi
1. "Apa yang membuat Anda tertarik untuk melamar posisi ini di perusahaan kami? Adakah aspek tertentu yang menarik perhatian Anda?"
2. "Dari informasi yang Anda ketahui tentang posisi ini, apa yang paling Anda antisipasi? Mengapa itu penting bagi Anda?"
3. "Bagaimana Anda melihat diri Anda berkontribusi dalam posisi ini? Adakah elemen dari posisi ini yang sangat sesuai dengan keahlian atau minat Anda?"

Semoga pertanyaan-pertanyaan ini membantu menciptakan suasana wawancara yang alami dan interaktif!
Kandidat:

```

masa baru aja perkenalan diri, langsung dikasih pertanyaan semua. ini kah hrd itu?

jadi perlu hrd_v4_new.py untuk bisa dibandingkan dengan sebelumnya

atau lebih baik pakai folder aja ya biar rapi?

```
🤖 HRD: Halo! Selamat datang di wawancara untuk posisi Junior Frontend Engineer di perusahaan kami. Bisa perkenalkan diri Anda?


👤 Kandidat : halo perkenalkan nama saya reza bisa dipanggil reza

🤖 HRD: Terima kasih, Reza! Senang bisa berbicara dengan Anda.

Selanjutnya, bisa ceritakan sedikit tentang pengalaman Anda sebagai Front-End Developer di proyek Chatbot SDPPI Kominfo? Apa tantangan yang Anda hadapi dan bagaimana Anda mengatasinya?

State : isFinish = False

👤 Kandidat : itu adalah project pertama saya dibidang frontend, dan proyek pertama saya yang profesional. jadi cukup sulit awalnya. dimana bersifat profesional pada ngerjain project nya. yang mana biasanya kalau sebelumnya aku ngerjain santai santai-an. tapi ini aku harus dikejar waktu.

🤖 HRD: Terima kasih, Reza, atas penjelasan mengenai pengalaman Anda di proyek tersebut. Saya menghargai kejujuran Anda dalam menghadapi tantangan tersebut.

Sekarang, saya ingin mengetahui lebih lanjut tentang keterampilan teknis Anda. Dari pengalaman Anda, seberapa sering Anda menggunakan React.js dalam proyek Anda, dan bisa ceritakan fitur atau komponen apa yang paling Anda nikmati untuk dikembangkan menggunakan React.js?

State : isFinish = False

👤 Kandidat : baru pertama kali di proyek sddppi. untuk fitur dan komponen favorit itu, react router, dimana kita membua
t kustom route nya yang menyenangkan bagi aku. yang mana react itu kan single web app.

🤖 HRD: Terima kasih, Reza, atas penjelasan mengenai penggunaan React.js dan fitur yang Anda sukai. Menarik sekali mendengar bahwa Anda menyukai pengembangan routing.

Saya ingin menanyakan satu hal lagi. Bagaimana Anda biasanya mengelola waktu dan prioritas Anda dalam menyelesaikan proyek, terutama saat menghadapi deadline yang ketat?

State : isFinish = False

👤 Kandidat : biasanya saya ngerjain nya pada akhiran aja sih. dengan ditemani lepi kesayangan ku, dan kopi hitam yang s
angat kental di tengah kesunyian malam

🤖 HRD: Terima kasih, Reza, atas jawaban Anda yang jujur. Saya menghargai cara Anda menemukan kenyamanan saat bekerja, meskipun itu di akhir waktu.

Berdasarkan wawancara ini, saya melihat Anda memiliki semangat yang baik dan pengalaman yang relevan untuk posisi ini. Anda menunjukkan kemampuan teknis dan pemahaman yang baik tentang frontend development, meskipun masih dalam tahap awal karier.

Saya akan memberikan evaluasi akhir dan skor untuk wawancara ini sebesar 75 dari 100. Anda memiliki potensi yang baik dan dengan pengalaman lebih lanjut, saya yakin Anda akan berkembang pesat.

Terima kasih sudah meluangkan waktu untuk berbicara dengan kami hari ini. Kami akan menghubungi Anda untuk langkah selanjutnya. Semoga sukses!

{
    "response": "Terima kasih, Reza, atas jawaban Anda yang jujur. Saya menghargai cara Anda menemukan kenyamanan saat bekerja, meskipun itu di akhir waktu. Berdasarkan wawancara ini, saya melihat Anda memiliki semangat yang baik dan pengalaman yang relevan untuk posisi ini. Anda menunjukkan kemampuan teknis dan pemahaman yang baik tentang frontend development, meskipun masih dalam tahap awal karier. Saya akan memberikan evaluasi akhir dan skor untuk wawancara ini sebesar 75 dari 100. Anda memiliki potensi yang baik dan dengan pengalaman lebih lanjut, saya yakin Anda akan berkembang pesat. Terima kasih sudah meluangkan waktu untuk berbicara dengan kami hari ini. Kami akan menghubungi Anda untuk langkah selanjutnya. Semoga sukses!",
    "is_finish": true
}

State : isFinish = False

👤 Kandidat :
```

respon diatas adalah respon yang salah, dikarenakan pada evaluasi prompot nya tidak mempertahankan format json nya

```

🤖 HRD: Halo! Selamat datang di wawancara untuk posisi Junior Frontend Engineer di perusahaan kami. Bisa perkenalkan diri Anda?


👤 Kandidat : halo perkenalkan nama saya reza, bisa dipanggil reza

 *** Respon RAW ***


 {
    "response": "Terima kasih Reza, senang berkenalan dengan Anda. Sekarang, saya ingin bertanya tentang pengalaman Anda sebagai Front-End Developer. Bisa Anda ceritakan lebih detail tentang proyek chatbot yang Anda kerjakan untuk SDPPI Kominfo? Apa tantangan terbesar yang Anda hadapi dan bagaimana Anda mengatasinya?",
    "is_finish": false
}


 *** akhir Respon RAW ***

🤖 HRD: Terima kasih Reza, senang berkenalan dengan Anda. Sekarang, saya ingin bertanya tentang pengalaman Anda sebagai Front-End Developer. Bisa Anda ceritakan lebih detail tentang proyek chatbot yang Anda kerjakan untuk SDPPI Kominfo? Apa tantangan terbesar yang Anda hadapi dan bagaimana Anda mengatasinya?

State : isFinish = False

👤 Kandidat : itu adlah proyek pertama saya, banyak pengalaman berharga disana. saya mengerjakan bagian user interface d
an front end. membangun antar muka chatbot dengan react js, dan tailwind

 *** Respon RAW ***


 {
    "response": "Terima kasih atas penjelasan Anda, Reza. Sangat menarik mendengar tentang pengalaman pertama Anda. Sekarang, saya ingin tahu lebih lanjut tentang alat dan teknologi yang Anda gunakan. Dalam proyek tersebut, bagaimana Anda mengintegrasikan front-end dengan back-end? Apakah Anda memiliki pengalaman dalam bekerja dengan API? Jika iya, bisa Anda ceritakan sedikit tentang itu?",
    "is_finish": false
}


 *** akhir Respon RAW ***

🤖 HRD: Terima kasih atas penjelasan Anda, Reza. Sangat menarik mendengar tentang pengalaman pertama Anda. Sekarang, saya ingin tahu lebih lanjut tentang alat dan teknologi yang Anda gunakan. Dalam proyek tersebut, bagaimana Anda mengintegrasikan front-end dengan back-end? Apakah Anda memiliki pengalaman dalam bekerja dengan API? Jika iya, bisa Anda ceritakan sedikit tentang itu?

State : isFinish = False

👤 Kandidat : saya pakai api untuk hubungi be nya. karena kami terbagi jadi 3 tim. fe, be, dan ai. jadi untuk menghubung
kannya. pakai api.

 *** Respon RAW ***


 {
    "response": "Terima kasih Reza, penjelasan Anda tentang penggunaan API dalam proyek tersebut sangat membantu. Selanjutnya, saya ingin tahu tentang pengalaman Anda dengan teknologi lain yang Anda sebutkan di CV, seperti Node.js dan Bootstrap. Bagaimana Anda menggunakannya dalam proyek Anda sebelumnya? Dan apakah Anda memiliki pengalaman dalam menggunakan sistem kontrol versi seperti Git?",
    "is_finish": false
}


 *** akhir Respon RAW ***

🤖 HRD: Terima kasih Reza, penjelasan Anda tentang penggunaan API dalam proyek tersebut sangat membantu. Selanjutnya, saya ingin tahu tentang pengalaman Anda dengan teknologi lain yang Anda sebutkan di CV, seperti Node.js dan Bootstrap. Bagaimana Anda menggunakannya dalam proyek Anda sebelumnya? Dan apakah Anda memiliki pengalaman dalam menggunakan sistem kontrol versi seperti Git?

State : isFinish = False

👤 Kandidat : node js itu hanya untuk compiler server aja, bootstarp itu untuk ui nya. dan tentu saja aku pakai git. kar
ena aku bekerja dalam tim. git itu pasti kepake. kalau enggak ya ntar masa aku harus kirim file ku pakai flashdisk wkwkw
k

 *** Respon RAW ***


 {
    "response": "Terima kasih atas penjelasan Anda, Reza. Sangat baik mendengar bahwa Anda memiliki pengalaman dengan Node.js, Bootstrap, dan Git. Sekarang, saya ingin bertanya tentang soft skills Anda. Dalam pekerjaan tim, bagaimana Anda berkomunikasi dengan anggota tim lainnya, dan bagaimana Anda menangani konflik yang mungkin muncul dalam proyek? Apakah Anda memiliki contoh konkret yang bisa Anda bagikan?",
    "is_finish": false
}


 *** akhir Respon RAW ***

🤖 HRD: Terima kasih atas penjelasan Anda, Reza. Sangat baik mendengar bahwa Anda memiliki pengalaman dengan Node.js, Bootstrap, dan Git. Sekarang, saya ingin bertanya tentang soft skills Anda. Dalam pekerjaan tim, bagaimana Anda berkomunikasi dengan anggota tim lainnya, dan bagaimana Anda menangani konflik yang mungkin muncul dalam proyek? Apakah Anda memiliki contoh konkret yang bisa Anda bagikan?

State : isFinish = False

👤 Kandidat : saya menjadi yes man aja. jadi apa yang disuruh,  aku iya aja dan mengerjakan. dan berikan hasil sesuai ke
inginan mereka

 *** Respon RAW ***


 {
    "response": "Terima kasih Reza, pendekatan yang Anda ambil dalam berkomunikasi dan berkolaborasi dengan tim sangat penting. Sekarang, untuk pertanyaan terakhir, bagaimana Anda tetap update dengan perkembangan terbaru dalam teknologi frontend? Apakah Anda mengikuti kursus, membaca artikel, atau bergabung dengan komunitas? Saya ingin tahu bagaimana Anda mengembangkan keterampilan Anda di luar pendidikan formal.",
    "is_finish": false
}


 *** akhir Respon RAW ***

🤖 HRD: Terima kasih Reza, pendekatan yang Anda ambil dalam berkomunikasi dan berkolaborasi dengan tim sangat penting. Sekarang, untuk pertanyaan terakhir, bagaimana Anda tetap update dengan perkembangan terbaru dalam teknologi frontend? Apakah Anda mengikuti kursus, membaca artikel, atau bergabung dengan komunitas? Saya ingin tahu bagaimana Anda mengembangkan keterampilan Anda di luar pendidikan formal.

State : isFinish = False

👤 Kandidat : saya lebih sering ikut forum gitu. kek forum gdsc. karena disana selain dapat info baru, aku dapat makanan
 gratis

 *** Respon RAW ***


 {
    "response": "Terima kasih Reza, informasi yang Anda berikan sangat membantu. Anda memiliki pengalaman dan pendekatan yang baik dalam pengembangan frontend serta kolaborasi tim. Berdasarkan wawancara ini, saya akan memberikan evaluasi dan skor untuk Anda. Secara keseluruhan, Anda menunjukkan pemahaman yang solid tentang teknologi yang relevan dan pengalaman praktis yang baik. Namun, Anda mungkin perlu memberikan lebih banyak contoh konkret tentang penyelesaian konflik dan komunikasi dalam tim. Skor akhir untuk Anda adalah 80. Terima kasih atas partisipasi Anda dalam wawancara ini.",
    "is_finish": true
}


 *** akhir Respon RAW ***

🤖 HRD: Terima kasih Reza, informasi yang Anda berikan sangat membantu. Anda memiliki pengalaman dan pendekatan yang baik dalam pengembangan frontend serta kolaborasi tim. Berdasarkan wawancara ini, saya akan memberikan evaluasi dan skor untuk Anda. Secara keseluruhan, Anda menunjukkan pemahaman yang solid tentang teknologi yang relevan dan pengalaman praktis yang baik. Namun, Anda mungkin perlu memberikan lebih banyak contoh konkret tentang penyelesaian konflik dan komunikasi dalam tim. Skor akhir untuk Anda adalah 80. Terima kasih atas partisipasi Anda dalam wawancara ini.

State : isFinish = True

```

ini adalah hasilnya, setelah debug. dan di bagian evaluate nya. kita maksa untuk outputnya harus sesuai format.

```

    def evaluate(self):
        evaluation_prompt = """
        Anda adalah pewawancara profesional AI. Evaluasi apakah wawancara sudah cukup berdasarkan percakapan sejauh ini dan informasi dari CV kandidat.

        **Format Output (WAJIB JSON, tanpa teks lain di luar JSON):**

        {
            "response": "<jawaban AI>",
            "is_finish": <true/false>
        }
        

        **Instruksi Evaluasi:**
        1. Periksa jumlah pertanyaan yang telah diajukan (`<jumlah_pertanyaan_sekarang>`) dibandingkan dengan batas maksimum (`<batas_maksimal_pertanyaan>`).
        2. Jika wawancara sudah cukup, berikan respons terakhir dan berikan input is_finish true
        3. Jika wawancara belum cukup, ajukan pertanyaan lain yang relevan dengan posisi yang dilamar.
        4. Nada harus tetap profesional tetapi ramah.

        **Catatan:**
        - Apapun hasilnya, **jawaban harus selalu dalam format JSON yang valid**, tanpa tambahan teks lain.
        """

        self.chat_history.append(SystemMessage(content=evaluation_prompt))