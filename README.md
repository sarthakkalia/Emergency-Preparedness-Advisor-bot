# Emergency Preparedness Chatbot

A chatbot application that provides users with intelligent, contextually aware advice on emergency preparedness. This chatbot is fine-tuned on emergency preparedness guidelines, using a dataset sourced via OCR from PDFs, and leverages GPT-2 to respond effectively to user inquiries.

![Chatbot Interface](https://github.com/sarthakkalia/Emergency-Preparedness-Advisor-bot/blob/main/templates/Screenshot%202024-10-31%20164152.png)

## Project Overview

The Emergency Preparedness Chatbot is designed to assist users in preparing for various emergencies by offering practical advice and answers based on a fine-tuned GPT-2 model. The chatbot has been trained on a dataset of emergency preparedness guidelines, extracted via OCR from documents, to ensure accurate and contextually relevant responses.

The chatbot can answer questions on topics like disaster preparedness, safety measures, and emergency supplies, providing a valuable resource for personalized guidance.

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/sarthakkalia/Emergency-Preparedness-Advisor-bot.git
cd Emergency-Preparedness-Advisor-bot
```

### 2. Install Dependencies

Install all necessary packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Model Fine-Tuning Details

- **Data Source**: The emergency preparedness dataset used for fine-tuning was sourced from [this PDF link](https://drive.google.com/drive/folders/1Ce14-0NvNRGrtjGFkjeRc5QKxTfFuoUx?usp=drive_link), and text was extracted using OCR.
- **Extracted Data**: The preprocessed data used for fine-tuning is available at `data/fine_tuning_data.txt`.
- **Fine-Tuning Process**: The GPT-2 model was fine-tuned using this dataset. For details on the model fine-tuning process, see `notebooks/model_finetuning.ipynb`.
- **Fine-Tuned Model**: The fine-tuned model is saved in `model/fine_tuned_emergency_bot_new`.

### 4. Configuration Steps

- **Model Path Configuration**: The fine-tuned model should be stored in `model/fine_tuned_emergency_bot_new`. If you want to specify a different model path, edit `application.py` to load your desired model.
- **Environment Variables**: There are no specific environment variables required for this application. All configurations are handled within the project files.

## Usage Guide

### Running the Application

To start the chatbot application using Flask, run:

```bash
python application.py
```

### Accessing the Chatbot

Open your browser and go to `http://127.0.0.1:5000` to interact with the chatbot. You should see an input field where you can type questions related to emergency preparedness.

### Example Interactions

- **Question**: "What should I do in case of a flood?"
- **Response**: "In case of a flood, move to higher ground, avoid walking or driving through flood waters, and listen to emergency alerts."

- **Question**: "How do I disinfect well water?"
- **Response**: "To disinfect well water, add a small amount of bleach or use chlorine tablets, then wait before testing for safety."

## File Structure

- **application.py**: The main Flask application, containing routes and response logic.
- **data/fine_tuning_data.txt**: The preprocessed text data used for fine-tuning.
- **model/fine_tuned_emergency_bot_new**: The directory containing the fine-tuned model.
- **notebooks/model_finetuning.ipynb**: Jupyter notebook with the GPT-2 model fine-tuning process.
- **requirements.txt**: Lists all necessary libraries and dependencies.
- **README.md**: Project documentation and setup guide.

## Requirements

Ensure you have the following dependencies, specified in `requirements.txt`:

- `transformers`
- `torch`
- `flask`

## Author

- **Sarthak Kalia**
- **sarthakkalia45@gmail.com**
