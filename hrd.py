import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner
from pydantic import BaseModel

# Load API Key
load_dotenv()
os.environ["OPENAI_MODEL"] = "gpt-4o-mini"  # Memastikan menggunakan GPT-4o-mini
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Model untuk guardrail
class InterviewCheckOutput(BaseModel):
    is_interview: bool
    reasoning: str

# Guardrail Agent untuk memastikan pertanyaan terkait wawancara
guardrail_agent = Agent(
    name="Interview Guardrail",
    instructions="Check if the user's question is related to a job interview.",
    output_type=InterviewCheckOutput,
)

# HRD Agent untuk wawancara
hrd_agent = Agent(
    name="Virtual HRD",
    handoff_description="Acts as an HR interviewer for job candidates.",
    instructions="You act as an HR interviewer. Ask relevant questions based on the job role.",
)

# Fungsi guardrail untuk memeriksa apakah input terkait wawancara
async def interview_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(InterviewCheckOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_interview,
    )

# Triage Agent untuk menentukan apakah user ingin wawancara
triage_agent = Agent(
    name="Triage Agent",
    instructions="Determine whether the user's request is related to a job interview.",
    handoffs=[hrd_agent],  # Jika terkait wawancara, akan dialihkan ke HRD Agent
    input_guardrails=[InputGuardrail(guardrail_function=interview_guardrail)],
)

# Fungsi utama untuk menjalankan wawancara
async def main():
    print("Virtual HRD - Simulasi Wawancara Kerja\n")
    
    while True:
        user_input = input("Kandidat: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Wawancara selesai.")
            break

        result = await Runner.run(triage_agent, user_input)
        print("HRD: ", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
