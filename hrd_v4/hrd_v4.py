import json
# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Load panduan wawancara
with open("question_guidelines.json", "r") as file:
    QUESTION_GUIDELINES = json.load(file)

class VirtualHRD:
    def __init__(self, position, salary, company_type, cv_path):
        self.chat_model = ChatOpenAI(model_name="gpt-4o-mini")
        self.position = position
        self.salary = salary
        self.company_type = company_type
        self.cv_text = self.extract_text_from_pdf(cv_path)
        self.chat_history = [
            SystemMessage(content=f"""
                Anda adalah HRD yang melakukan wawancara untuk posisi {self.position} di perusahaan {self.company_type}.
                Kandidat memiliki CV sebagai berikut:
                {self.cv_text}
                
                Gunakan panduan wawancara berikut untuk menyusun pertanyaan:
                {QUESTION_GUIDELINES}
                
                Jangan ulangi pertanyaan yang sama. Kembangkan pertanyaan agar terdengar alami.
                Jika kandidat kurang jelas dalam jawabannya, tanyakan lebih lanjut.
                Jika semua kategori sudah ditanyakan, akhiri wawancara dengan evaluasi dan skor.
            """)
        ]
        self.categories = list(QUESTION_GUIDELINES.keys())
        self.current_category_index = 0

    def extract_text_from_pdf(self, file_path):
        """Simulasi ekstraksi teks dari PDF CV kandidat."""
        return "Pengalaman: Frontend Developer di startup. Keahlian: React, JavaScript, CSS."

    def ask_question(self):
        """HRD mengajukan pertanyaan berbasis AI yang dikembangkan dari panduan manual."""
        if self.current_category_index < len(self.categories):
            category = self.categories[self.current_category_index]
            key_points = QUESTION_GUIDELINES[category]

            # Minta AI mengembangkan pertanyaan dari key points
            prompt = f"""
                Anda adalah HRD dalam wawancara. Buat pertanyaan berbasis topik berikut:
                {key_points}
                Pastikan pertanyaan alami dan tidak terlalu robotik.
            """
            response = self.chat_model([HumanMessage(content=prompt)])
            question = response.content

            # Simpan ke histori
            self.chat_history.append(AIMessage(content=question))
            print(f"\nHRD: {question}")

            # Pindah ke kategori berikutnya
            self.current_category_index += 1
            return question
        else:
            return self.evaluate_candidate()

    def evaluate_candidate(self):
        """AI memberikan evaluasi dan skor setelah wawancara selesai."""
        eval_prompt = """
            Wawancara telah selesai. Berikan evaluasi dan skor kandidat berdasarkan jawaban mereka.
            Gunakan skala 1-10 untuk setiap aspek (komunikasi, teknis, teamwork, dll.).
            Berikan umpan balik yang bisa membantu kandidat memperbaiki diri.
        """
        response = self.chat_model([HumanMessage(content=eval_prompt)])
        evaluation = response.content

        print(f"\nHRD (Evaluasi):\n{evaluation}")
        return evaluation
    
if __name__ == "__main__":
    position = "Frontend Developer"
    salary = "$50,000 per year"
    company_type = "startup"
    cv_path = "cv.pdf"

    hrd = VirtualHRD(position, salary, company_type, cv_path)
    print("Virtual HRD - Simulasi Wawancara Kerja\n")
    
    while True:
        user_input = input("Kandidat: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Wawancara selesai.")
            break

        response = hrd.ask_question()
        print(f"Kandidat: {user_input}")
        print(f"HRD: {response}")
