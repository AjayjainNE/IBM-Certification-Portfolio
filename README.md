# IBM AI Engineering Professional Certificate — Project Portfolio

This repository contains the project work I completed as part of the IBM AI Engineering Professional Certificate on Coursera. The cert covers the full stack from classical ML through to deep learning, generative AI, and LLMs. I used it specifically to fill gaps in applied DL and LLM work that sit outside my MSc in Applied Data Science at Royal Holloway.

---

## What's in here

| Folder | What it covers |
|--------|---------------|
| `Machine_Learning_Algorithm` | Supervised and unsupervised models, cross-validation, model selection |
| `Neural_Network_Pytorch` | Building and training neural networks from scratch in PyTorch |
| `Deep_Learning_Keras` | CNNs, regularisation, transfer learning using Keras |
| `Deep_Learning_Pytorch` | PyTorch equivalents — same concepts, different framework |
| `Transformers_Fine_Tuning` | Fine-tuning pre-trained transformer models on classification tasks |
| `PEFT_HF_PYT` | LoRA and soft prompt tuning with Hugging Face + PyTorch |
| `GenAI and LLMs` | RAG pipelines, LangChain agents, prompt engineering |
| `Project_Classification_News_Article` | End-to-end NLP classification project |
| `Project_DL` | Structured deep learning project with training, evaluation, and analysis |
| `Project_Histogram_NGram_for_Pop_Lyrics` | N-gram language modelling on text data |
| `AI_Capstone_Project` | Capstone bringing together CV, NLP, and model deployment |

---

## Projects worth looking at

### PEFT and LLM Fine-Tuning (`PEFT_HF_PYT`)
This was the most useful module for me practically. I worked through LoRA and soft prompt tuning to adapt pre-trained language models for downstream tasks, comparing it directly against full fine-tuning. The main takeaway: you can get within a few percentage points of full fine-tuning accuracy while updating less than 10% of the parameters. That matters a lot when you are working with limited compute or small labelled datasets.

### Generative AI with RAG and LangChain (`GenAI and LLMs`)
Built a retrieval-augmented generation pipeline where the model pulls relevant documents before generating a response. The difference in factual accuracy between RAG and a plain prompt is noticeable even on small document sets. Also set up a multi-step agent using LangChain tool-calling and memory, which gave me a clearer picture of where agents break down and why prompt design matters.

### Transformer Fine-Tuning (`Transformers_Fine_Tuning`)
Covers the basics of adapting BERT-style models to text classification. Nothing exotic here, but it was useful grounding before moving into the PEFT work above.

---

## Notes

- All notebooks are Jupyter (.ipynb) and should run in a standard Python 3.9+ environment with the packages listed in each folder
- Some notebooks were written during the course and reflect learning-in-progress rather than polished final code
- If something is broken or unclear, raise an issue

---

## Contact

**Ajay Khadke**
callitajay@gmail.com | [linkedin.com/in/callitajay](https://linkedin.com/in/callitajay) | [dataopsdigest.wordpress.com](https://dataopsdigest.wordpress.com)
