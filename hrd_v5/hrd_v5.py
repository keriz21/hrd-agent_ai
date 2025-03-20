from flask import Flask, request, jsonify
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv, find_dotenv
import fitz
import json

_ = load_dotenv(find_dotenv())
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = '\n'.join([page.get_text() for page in doc])
    return text.strip()


class VirtualHRD:
    def __init__(self, position, salary, company_type, cv_text):
        self.chat_model = ChatOpenAI(model='gpt-4o-mini')
        self.position = position
        self.salary = salary
        self.company_type = company_type
        self.cv_text = cv_text
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
            """
            )
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
        return response_text, is_finish

    def answer_question(self, user_input):
        self.chat_history.append(HumanMessage(content=user_input))

    def evaluate(self):
        evaluation_prompt = """
        Anda adalah pewawancara profesional AI. Evaluasi apakah wawancara sudah cukup berdasarkan percakapan sejauh ini dan informasi dari CV kandidat.

        **Format Output (WAJIB JSON, tanpa teks lain di luar JSON):**

        {
            "response": "<jawaban AI>",
            "is_finish": <true/false>
        }
        
        **Instruksi Evaluasi:**
        1. Periksa jumlah pertanyaan yang telah diajukan dibandingkan dengan batas maksimum.
        2. Jika wawancara sudah cukup, berikan respons terakhir dan berikan input is_finish true.
        3. Jika wawancara belum cukup, ajukan pertanyaan lain yang relevan dengan posisi yang dilamar.
        4. Nada harus tetap profesional tetapi ramah.

        **Catatan:**
        - Apapun hasilnya, **jawaban harus selalu dalam format JSON yang valid**, tanpa tambahan teks lain.
        """

        self.chat_history.append(SystemMessage(content=evaluation_prompt))


virtual_hrd = None


@app.route('/start_interview', methods=['POST'])
def start_interview():
    global virtual_hrd
    data = request.json
    position = data.get('position')
    salary = data.get('salary')
    company_type = data.get('company_type')
    cv_path = data.get('cv_path')

    if not all([position, salary, company_type, cv_path]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cv_text = extract_text_from_pdf(cv_path)
        virtual_hrd = VirtualHRD(position, salary, company_type, cv_text)
        return jsonify({"message": "Interview started"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/ask_question', methods=['GET'])
def ask_question():
    global virtual_hrd
    if virtual_hrd is None:
        return jsonify({"error": "Interview has not started"}), 400
    question, is_finish = virtual_hrd.ask_question()
    return jsonify({"response": question, "is_finish": is_finish})


@app.route('/answer_question', methods=['POST'])
def answer_question():
    global virtual_hrd
    if virtual_hrd is None:
        return jsonify({"error": "Interview has not started"}), 400
    data = request.json
    user_input = data.get('answer')
    if not user_input:
        return jsonify({"error": "Answer is required"}), 400
    virtual_hrd.answer_question(user_input)
    return jsonify({"message": "Answer received"})


if __name__ == '__main__':
    app.run(debug=True)
