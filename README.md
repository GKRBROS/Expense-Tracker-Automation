# Expense-Tracker-Automation

Expense Tracker Automation using Telegram Bot, powered by n8n workflow automation and Google Gemini AI.

## 📋 Overview

This project provides an intelligent expense tracking system that allows you to log your expenses and income through a simple Telegram bot conversation. The workflow uses AI-powered information extraction to automatically parse natural language messages and store structured data in Google Sheets, providing real-time financial summaries.

## ✨ Features

- **💬 Telegram Bot Interface**: Track expenses by simply sending messages to your Telegram bot
- **🤖 AI-Powered Extraction**: Uses Google Gemini AI to extract expense details (cost, description, date, type) from natural language
- **📊 Google Sheets Integration**: Automatically stores all transactions in a Google Sheets spreadsheet
- **📈 Real-time Analytics**: Calculates and displays total income, expenses, balance, and transaction count
- **🔔 Instant Confirmation**: Sends formatted confirmation messages with financial summaries
- **🌐 Cloud-Based**: Runs on n8n workflow automation platform - no server maintenance required

## 🏗️ Workflow Architecture

The n8n workflow consists of 6 main nodes:

1. **Telegram Trigger**: Listens for incoming messages from Telegram
2. **Information Extractor**: Uses AI to extract structured data (cost, description, date, type) from text
3. **Google Gemini Chat Model**: Powers the AI extraction with Google's Gemini LLM
4. **Append Row in Sheet**: Saves the extracted transaction to Google Sheets
5. **Get All Transactions**: Retrieves all existing transactions for summary calculation
6. **Calculate Totals**: Computes financial summaries (total income, expenses, balance)
7. **Send Confirmation**: Sends a formatted message back to Telegram with transaction details and summary

## 🔧 Prerequisites

Before setting up this workflow, you'll need:

- **n8n Account**: Sign up at [n8n.io](https://n8n.io) (cloud or self-hosted)
- **Telegram Bot Token**: Create a bot via [@BotFather](https://t.me/botfather) on Telegram
- **Google Cloud Account**: For Google Sheets and Gemini API access
- **Google Gemini API Key**: Enable the Gemini API in Google Cloud Console
- **Google Sheets**: A spreadsheet with columns: `Description`, `Cost`, `Date`, `Type`

## 🚀 Setup Instructions

### 1. Import the Workflow

1. Download the `Expense Tracker.json` file from this repository
2. Log in to your n8n instance
3. Click on **"Workflows"** → **"Import from File"**
4. Select the downloaded JSON file

### 2. Configure Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` and follow the instructions
3. Copy the API token provided
4. In n8n, configure the **Telegram Trigger** node:
   - Add your Telegram API credentials
   - Save the configuration

### 3. Set Up Google Sheets

1. Create a new Google Spreadsheet
2. Set up the following columns in Sheet1:
   - `Description` (Text)
   - `Cost` (Number)
   - `Date` (Date)
   - `Type` (Text - "expense" or "income")
3. Copy the spreadsheet ID from the URL
4. In n8n, configure both Google Sheets nodes:
   - Add your Google OAuth2 credentials
   - Update the spreadsheet ID in:
     - **Append row in sheet** node
     - **Get All Transactions** node

### 4. Configure Google Gemini API

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create or use an existing API key
3. In n8n, configure the **Google Gemini Chat Model** node:
   - Add your Google Gemini API credentials
   - Save the configuration

### 5. Activate the Workflow

1. Click **"Active"** toggle in the top-right corner
2. The workflow is now live and ready to receive messages!

## 📱 Usage

### Logging Expenses

Simply send a message to your Telegram bot in natural language:

```
Bought groceries for $45 today
```

```
Paid $120 for electricity bill on 2024-01-05
```

```
Coffee at Starbucks $5.50 January 8
```

### Logging Income

```
Received salary $3000 today as income
```

```
Freelance payment $500 on 2024-01-07 income
```

### Bot Response

After each transaction, the bot will reply with:

```
Expense saved! 💸 Groceries - $45.00

📊 Summary:
💰 Total Income: $3500.00
💸 Total Expenses: $675.50
📈 Balance: $2824.50
📝 Total Transactions: 12
```

## 🔍 Workflow Node Details

### Information Extractor
- **Type**: AI Information Extractor
- **Purpose**: Parses natural language and extracts structured data
- **Extracted Fields**:
  - `cost` (number): Amount of the transaction
  - `description` (text): What the transaction was for
  - `date` (date): When the transaction occurred
  - `type` (text): "expense" or "income"

### Google Gemini Chat Model
- **Model**: Google Gemini (PaLM)
- **Purpose**: Provides the AI language model for information extraction
- **Integration**: Connected to the Information Extractor node

### Append Row in Sheet
- **Operation**: Append
- **Purpose**: Adds new transactions to the Google Sheet
- **Columns Mapped**: Description, Cost, Date, Type

### Calculate Totals
- **Type**: Code Node (JavaScript)
- **Purpose**: Aggregates all transactions and calculates:
  - Total income
  - Total expenses
  - Current balance
  - Transaction count

## 💡 Example Scenarios

| Input Message | Extracted Data |
|--------------|----------------|
| "Lunch at McDonald's $12" | Cost: 12, Description: "Lunch at McDonald's", Type: "expense", Date: today |
| "Got paid $2000 as income yesterday" | Cost: 2000, Description: "Got paid", Type: "income", Date: yesterday |
| "Metro card $50 on Jan 5" | Cost: 50, Description: "Metro card", Type: "expense", Date: 2024-01-05 |

## 🛠️ Troubleshooting

### Bot Not Responding
- Verify the workflow is **Active** in n8n
- Check Telegram API credentials are correct
- Ensure the webhook is properly configured

### AI Extraction Errors
- Verify Google Gemini API credentials
- Check API quota and rate limits
- Ensure the message contains cost information

### Google Sheets Errors
- Verify OAuth2 credentials are valid
- Check spreadsheet ID is correct
- Ensure column names match exactly: `Description`, `Cost`, `Date`, `Type`
- Verify the sheet name (default: "Sheet1")

### Calculation Issues
- Ensure `Cost` column contains valid numbers
- Check `Type` column values are "expense" or "income" (case-insensitive)

## 📊 Customization

### Modify Extracted Fields
Edit the **Information Extractor** node to add/remove fields or change descriptions.

### Change Response Format
Edit the **Send Confirmation** node to customize the message format and emojis.

### Add Categories
Extend the Information Extractor to include a `category` field (groceries, utilities, entertainment, etc.).

### Multi-Currency Support
Modify the workflow to extract and convert currencies using an exchange rate API.

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review [n8n documentation](https://docs.n8n.io)
3. Open an issue in this repository

## 🙏 Acknowledgments

- **n8n**: Powerful workflow automation platform
- **Google Gemini**: Advanced AI language model
- **Telegram**: Secure messaging platform
