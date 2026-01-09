# Expense Tracker Automation 💰

A powerful and easy-to-use Telegram bot for tracking your daily expenses, managing budgets, and analyzing spending patterns.

## 📋 Description

This Expense Tracker Telegram Bot helps you manage your personal finances directly through Telegram. Simply chat with the bot to add expenses, view your spending history, get detailed summaries, and stay on top of your budget. All your data is stored locally and securely.

### Key Features

- 💸 **Easy Expense Logging**: Add expenses with just a simple command
- 📊 **Spending Analytics**: Get daily, weekly, and monthly summaries
- 🏷️ **Category Management**: Track expenses across multiple categories (Food, Transport, Shopping, Bills, etc.)
- 💰 **Budget Tracking**: Set budgets and monitor your spending
- 📈 **Visual Insights**: See spending breakdown by category
- 📤 **Data Export**: Export your expense data to CSV
- 🔒 **Privacy First**: All data stored locally on your server

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- A Telegram account
- A Telegram Bot Token (get it from [@BotFather](https://t.me/botfather))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/GKRBROS/Expense-Tracker-Automation.git
   cd Expense-Tracker-Automation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```
   
   Replace `your_bot_token_here` with your actual bot token from BotFather.

4. **Run the bot**
   ```bash
   python expense_tracker_bot.py
   ```

## 📱 Usage

### Bot Commands

Once the bot is running, you can interact with it using these commands:

- **`/start`** - Start the bot and see the welcome message
- **`/add`** - Add a new expense
  - Example: `/add 25.50 Food Lunch at restaurant`
- **`/history`** - View your recent expense history
- **`/summary`** - Get spending summary for different time periods
  - Daily, weekly, or monthly summaries
- **`/budget`** - Set or view your current budget
- **`/categories`** - View all available expense categories
- **`/export`** - Export your expenses to CSV file
- **`/help`** - Show all available commands with examples

### Example Workflow

1. Start a chat with your bot on Telegram
2. Send `/start` to initialize
3. Add an expense: `/add 50 Transport Taxi to office`
4. View your history: `/history`
5. Get a summary: `/summary weekly`
6. Set a budget: `/budget 1000`

## 🏗️ Project Structure

```
Expense-Tracker-Automation/
├── expense_tracker_bot.py   # Main bot implementation
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (create this)
├── .gitignore              # Git ignore file
├── expenses.json           # Expense data (created automatically)
├── LICENSE                 # MIT License
└── README.md               # This file
```

## 🛠️ Configuration

### Expense Categories

The bot comes with default categories:
- Food
- Transport
- Shopping
- Bills
- Entertainment
- Healthcare
- Other

You can customize these by modifying the `categories` list in the `ExpenseTracker` class.

### Data Storage

Expenses are stored in `expenses.json` in the project directory. Each expense includes:
- Unique ID
- User ID
- Amount
- Category
- Description
- Date and timestamp

## 🔧 Technical Details

### Built With

- **Python 3.7+**: Core programming language
- **python-telegram-bot**: Telegram Bot API wrapper
- **JSON**: For data persistence

### Architecture

The project consists of two main classes:

1. **ExpenseTracker**: Handles all expense-related operations
   - Add, retrieve, and analyze expenses
   - Category management
   - Data persistence

2. **TelegramBot**: Manages Telegram bot interactions
   - Command handlers
   - Message formatting
   - User interface

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**GKRBROS**

- GitHub: [@GKRBROS](https://github.com/GKRBROS)

## 🙏 Acknowledgments

- Thanks to the python-telegram-bot community
- Inspired by personal finance management needs
- Built with ❤️ for better expense tracking

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation

## 🔮 Future Enhancements

- [ ] Multi-currency support
- [ ] Recurring expense tracking
- [ ] Budget alerts and notifications
- [ ] Graphical charts and visualizations
- [ ] Receipt image upload and OCR
- [ ] Expense splitting for shared costs
- [ ] Database integration for better scalability
- [ ] Web dashboard for detailed analytics

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
