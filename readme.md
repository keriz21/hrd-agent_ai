
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