# llm_chat.py — Gradio web chatbot powered by IBM watsonx.ai
#
# Requirements (install in your virtual environment):
#   pip install gradio==4.44.0 ibm-watsonx-ai==1.1.2 langchain==0.2.11 \
#               langchain-ibm==0.1.11 pydantic==2.10.6 huggingface_hub==0.23.0
#
# NOTE: project_id="skills-network" only works inside IBM Skills Network Cloud IDE.
#       For local use, replace with your own project_id and supply API credentials.

from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM
import gradio as gr

# ── Model selection ─────────────────────────────────────────────────────────
# Uncomment the model you want to use (comment out the other one):
# model_id = 'mistralai/mistral-small-3-1-24b-instruct-2503'  # Mixtral 8x7B
model_id = 'ibm/granite-3-3-8b-instruct'                     # Granite 3.3 8B (default)

# ── Generation parameters ────────────────────────────────────────────────────
parameters = {
    GenParams.MAX_NEW_TOKENS: 512,   # Increased from 256 to avoid cut-off responses
    GenParams.TEMPERATURE: 0.5,      # Creativity / randomness of responses
}

# ── Project / credentials ────────────────────────────────────────────────────
project_id = "skills-network"  # Free access inside IBM Skills Network Cloud IDE

# ── Initialise WatsonxLLM ────────────────────────────────────────────────────
watsonx_llm = WatsonxLLM(
    model_id=model_id,
    url="https://us-south.ml.cloud.ibm.com",
    project_id=project_id,
    params=parameters,
)

# ── Response generation function ─────────────────────────────────────────────
def generate_response(prompt_txt):
    """Send the user prompt to the LLM and return its response."""
    generated_response = watsonx_llm.invoke(prompt_txt)
    return generated_response

# ── Gradio interface ──────────────────────────────────────────────────────────
chat_application = gr.Interface(
    fn=generate_response,
    allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Watsonx.ai Chatbot",
    description="Ask any question and the chatbot will try to answer."
)

# ── Launch ────────────────────────────────────────────────────────────────────
chat_application.launch(server_name="127.0.0.1", server_port=7860)
