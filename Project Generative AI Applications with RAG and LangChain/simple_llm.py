# simple_llm.py — Terminal-based Q&A bot using IBM watsonx.ai
#
# Requirements (install in your virtual environment):
#   pip install ibm-watsonx-ai==1.1.2 langchain==0.2.11 langchain-ibm==0.1.11 pydantic==2.10.6
#
# NOTE: project_id="skills-network" only works inside IBM Skills Network Cloud IDE.
#       For local use, set your own project_id and provide credentials via environment
#       variables WATSONX_APIKEY and WATSONX_URL, or pass them explicitly.

from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM

# ── Model selection ─────────────────────────────────────────────────────────
# Uncomment the model you want to use (comment out the other one):
# model_id = 'mistralai/mistral-small-3-1-24b-instruct-2503'  # Mixtral 8x7B
model_id = 'ibm/granite-3-3-8b-instruct'                     # Granite 3.3 8B (default)

# ── Generation parameters ────────────────────────────────────────────────────
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,   # Maximum tokens to generate
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

# ── Run the Q&A loop ─────────────────────────────────────────────────────────
query = input("Please enter your query: ")
print(watsonx_llm.invoke(query))
