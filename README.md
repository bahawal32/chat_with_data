# Voting Smart Contract Chat App

This project is a chat application built using FastAPI, Streamlit, and OpenAI's GPT-based API, designed to interact with a voting smart contract. The app allows users to fetch voting data from the smart contract and engage in a natural-language conversation to ask questions about the data retrieved.

## Features

- **Data Fetching from Smart Contract**: The app retrieves context data (e.g., voting results, candidate details) from a specified voting smart contract.
- **Question-Answer Interface**: Once data is fetched, users can ask questions in natural language based on the context provided by the smart contract.
- **Conversational Flow**: Users can enter new questions, and the app uses the OpenAI API to generate answers based on the contract data context.
- **User-Friendly Interface**: Built with Streamlit for a seamless chat-like experience.

## How It Works

1. **Fetch Data**: The app connects to the voting smart contract and retrieves relevant data. This data could include voting counts, candidate details, or other context-specific information stored in the contract.
2. **Set Context**: The retrieved data is set as the chat context, providing the basis for all subsequent questions and responses.
3. **Ask Questions**: Users can type in questions about the voting data. The app sends these questions, along with the context, to the OpenAI API, which generates relevant answers.
4. **Display Conversation**: The Q&A history is displayed in a conversational format, allowing users to see both their questions and the AI's responses.

## Tech Stack

- **FastAPI**: Serves as the backend API, providing endpoints for handling the OpenAI ChatGPT-based responses.
- **Streamlit**: Provides a user-friendly web interface to simulate a chat experience.
- **OpenAI API**: Generates natural-language answers based on the fetched contract data.
- **Voting Smart Contract**: The app integrates with a blockchain-based voting smart contract to fetch real-time data for questions.

## Prerequisites

- **Python** 3.7+
- **OpenAI API Key**: Required for generating responses using ChatGPT.
- **Streamlit** and **FastAPI**: Installable via pip.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/voting-smart-contract-chat.git
   cd voting-smart-contract-chat
