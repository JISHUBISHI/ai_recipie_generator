# Sumir Rannaghar 2.0

## Overview

Sumir Rannaghar 2.0 is an AI-powered recipe assistant that helps users discover and learn various recipes. The chatbot is built using **Streamlit** for the frontend and **LangChain** with **Google Gemini API** for AI-based conversational capabilities. The bot provides users with recipe suggestions, including ingredients and preparation steps, and restricts responses to recipe-related queries.

## Features

- AI-powered recipe recommendations
- Supports natural language queries
- User-friendly interface using Streamlit
- Uses Google Gemini AI via LangChain
- Filters out non-recipe-related queries

## Technologies Used

- **Python** (Core programming language)
- **Streamlit** (Web interface)
- **LangChain** (AI model handling)
- **Google Generative AI API (Gemini 1.5 Pro)**

## Installation

1. Clone this repository:
   ```sh
   git clone https:https://github.com/JISHUBISHI/ai_recipie_generator
   cd sumir-rannaghar
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your Google API key:
   - Replace the `api_key` in `main.py` with your own Google Gemini API key.

## Usage

1. Run the application:
   ```sh
   streamlit run main.py
   ```
2. Enter your cooking-related queries in the chat input box.
3. Get recipe recommendations based on your query.

## Environment Variables

To keep your API key secure, you can set an environment variable instead of hardcoding it:

```sh
export GOOGLE_API_KEY="your_api_key_here"
```

Then, modify the code to use:

```python
api_key = os.getenv("GOOGLE_API_KEY")
```

## Example Queries

- "Give me a recipe for butter chicken."
- "What ingredients do I need for a chocolate cake?"
- "How do I prepare homemade pasta?"


## Author

Agnik Bishi

