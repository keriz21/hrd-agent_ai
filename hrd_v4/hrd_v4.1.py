from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

import os
from dotenv import load_dotenv, find_dotenv
import fitz

import json

_ = load_dotenv(find_dotenv())
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = '\n'.join([page.get_text() for page in doc])
    return text.strip()

class VirtualHRD:
    def __init__(self, position, salary, company_type, cv_path):
        self.chat_model = ChatOpenAI(model='gpt-4o-mini')
        self.position = position
        self.salary = salary
        self.company_type = company_type
        self.cv_text = extract_text_from_pdf(cv_path)
        self.chat_history = [
            SystemMessage(content=f"""
                Anda adalah seorang HRD di perusahaan {self.company_type}.
                Saat ini Anda sedang melakukan wawancara untuk posisi {self.position} dengan gaji {self.salary}.
                CV kandidat telah diberikan berikut:
                {self.cv_text}
                
                Tanyakan pertanyaan secara proaktif, mulai dari pengenalan diri, pengalaman, hingga pertanyaan teknis.
                Setelah cukup, akhiri wawancara dengan memberikan evaluasi & skor (0-100).
                dan kasih output is_finish jadi true, jika dirasa sudah cukup wawancaranya.
                kamu akan bertanya maksimal 10 pertanyaan.

                format output yang harus diberikan dalam JSON:
                {{
                    "response": "<jawaban AI>",
                    "is_finish": <true/false>
                }}
            """)
        ]
    
    def ask_question(self):
        response = self.chat_model.invoke(self.chat_history)

        try:
            response_data = json.loads(response.content)
            response_text = response_data.get("response")
            is_finish = response_data.get("is_finish", False)
        except json.JSONDecodeError:
            response_text = response.content
            is_finish = False

        self.chat_history.append(HumanMessage(content=response_text))
        print(f"\n *** Respon RAW *** \n \n\n {response.content} \n\n \n *** akhir Respon RAW ***")
        print(f"\n🤖 HRD: {response_text}")
        return response_text, is_finish
    
    def answer_question(self, user_input):
        self.chat_history.append(HumanMessage(content=user_input))

    def init_interview(self):
        print("\n🤖 HRD: Halo! Selamat datang di wawancara untuk posisi Junior Frontend Engineer di perusahaan kami. Bisa perkenalkan diri Anda?\n")
        self.chat_history.append(AIMessage(content="Halo! Selamat datang di wawancara untuk posisi Junior Frontend Engineer di perusahaan kami. Bisa perkenalkan diri Anda?"))
        pass

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

    def run_interview(self):

        self.init_interview()        

        while True:

            user_input = input("\n👤 Kandidat : ")
            self.answer_question(user_input)

            self.evaluate()

            question, is_finish = self.ask_question()
            print(f"\nState : isFinish = {is_finish}")
            if is_finish:
                break

            pass

if __name__ == '__main__':
    cv_path = 'public/CV_Reza Ali Nirwansyah (2).pdf'
    virtual_hrd = VirtualHRD(
                position='frontend Developer',
                salary='Rp 4.000.000',
                company_type='non-profit',
                cv_path=cv_path
            )

    virtual_hrd.run_interview()
