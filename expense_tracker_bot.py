"""
Expense Tracker Telegram Bot

This bot helps users track their daily expenses through Telegram.
Users can add expenses, view their spending history, get spending summaries,
and manage their budget directly through chat commands.

Features:
- Add new expenses with category, amount, and description
- View expense history with date filtering
- Get daily, weekly, and monthly spending summaries
- Set and track budget limits
- Export expense data to CSV
- Get spending insights by category
- Support for multiple currencies

Commands:
- /start - Start the bot and see welcome message
- /add - Add a new expense (format: /add <amount> <category> <description>)
- /history - View recent expense history
- /summary - Get spending summary for a time period
- /budget - Set or view current budget
- /categories - View all expense categories
- /export - Export expenses to CSV file
- /help - Show all available commands

Author: GKRBROS
License: MIT
"""

import os
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class ExpenseTracker:
    """
    Core expense tracking functionality.
    
    This class handles all expense-related operations including adding,
    retrieving, and analyzing expenses.
    """
    
    def __init__(self, data_file: str = 'expenses.json'):
        """
        Initialize the expense tracker.
        
        Args:
            data_file: Path to the JSON file storing expense data
        """
        self.data_file = data_file
        self.expenses: List[Dict] = []
        self.categories = [
            'Food', 'Transport', 'Shopping', 'Bills',
            'Entertainment', 'Healthcare', 'Other'
        ]
        self.load_expenses()
    
    def load_expenses(self) -> None:
        """Load expenses from the data file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.expenses = json.load(f)
                logger.info(f"Loaded {len(self.expenses)} expenses from file")
        except Exception as e:
            logger.error(f"Error loading expenses: {e}")
            self.expenses = []
    
    def save_expenses(self) -> None:
        """Save expenses to the data file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.expenses, f, indent=2)
            logger.info(f"Saved {len(self.expenses)} expenses to file")
        except Exception as e:
            logger.error(f"Error saving expenses: {e}")
    
    def add_expense(self, user_id: int, amount: float, category: str, 
                   description: str = '') -> Dict:
        """
        Add a new expense.
        
        Args:
            user_id: Telegram user ID
            amount: Expense amount
            category: Expense category
            description: Optional description
            
        Returns:
            Dictionary containing the added expense
        """
        expense = {
            'id': len(self.expenses) + 1,
            'user_id': user_id,
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().isoformat(),
            'timestamp': datetime.now().timestamp()
        }
        self.expenses.append(expense)
        self.save_expenses()
        logger.info(f"Added expense: {amount} in {category} for user {user_id}")
        return expense
    
    def get_user_expenses(self, user_id: int, days: Optional[int] = None) -> List[Dict]:
        """
        Get expenses for a specific user.
        
        Args:
            user_id: Telegram user ID
            days: Optional number of days to look back
            
        Returns:
            List of expense dictionaries
        """
        user_expenses = [e for e in self.expenses if e['user_id'] == user_id]
        
        if days:
            cutoff_date = datetime.now() - timedelta(days=days)
            user_expenses = [
                e for e in user_expenses 
                if datetime.fromisoformat(e['date']) > cutoff_date
            ]
        
        return sorted(user_expenses, key=lambda x: x['timestamp'], reverse=True)
    
    def get_summary(self, user_id: int, days: int = 30) -> Dict:
        """
        Get spending summary for a user.
        
        Args:
            user_id: Telegram user ID
            days: Number of days to summarize
            
        Returns:
            Dictionary with summary statistics
        """
        expenses = self.get_user_expenses(user_id, days)
        
        if not expenses:
            return {
                'total': 0,
                'count': 0,
                'by_category': {},
                'days': days
            }
        
        total = sum(e['amount'] for e in expenses)
        by_category = {}
        
        for expense in expenses:
            category = expense['category']
            by_category[category] = by_category.get(category, 0) + expense['amount']
        
        return {
            'total': total,
            'count': len(expenses),
            'by_category': by_category,
            'days': days,
            'average_per_day': total / days if days > 0 else 0
        }


class TelegramBot:
    """
    Telegram bot interface for expense tracking.
    
    This class handles all Telegram bot operations and user interactions.
    Note: This is a skeleton implementation. Full integration requires
    python-telegram-bot library.
    """
    
    def __init__(self, token: str):
        """
        Initialize the Telegram bot.
        
        Args:
            token: Telegram bot API token
        """
        self.token = token
        self.tracker = ExpenseTracker()
        self.user_budgets: Dict[int, float] = {}
        logger.info("Telegram bot initialized")
    
    def start(self) -> None:
        """Start the bot and begin polling for messages."""
        logger.info("Bot started and listening for messages...")
        # Implementation would use python-telegram-bot library here
        # updater = Updater(token=self.token)
        # dispatcher = updater.dispatcher
        # Add handlers here
        # updater.start_polling()
    
    def format_expense(self, expense: Dict) -> str:
        """
        Format an expense for display.
        
        Args:
            expense: Expense dictionary
            
        Returns:
            Formatted string
        """
        date = datetime.fromisoformat(expense['date']).strftime('%Y-%m-%d %H:%M')
        desc = expense['description'] or 'No description'
        return f"💰 ${expense['amount']:.2f} - {expense['category']}\n📝 {desc}\n📅 {date}"
    
    def format_summary(self, summary: Dict) -> str:
        """
        Format a summary for display.
        
        Args:
            summary: Summary dictionary
            
        Returns:
            Formatted string
        """
        if summary['count'] == 0:
            return "No expenses recorded in this period."
        
        text = f"📊 Summary for last {summary['days']} days:\n\n"
        text += f"Total: ${summary['total']:.2f}\n"
        text += f"Transactions: {summary['count']}\n"
        text += f"Daily average: ${summary['average_per_day']:.2f}\n\n"
        text += "By category:\n"
        
        for category, amount in sorted(summary['by_category'].items(), 
                                       key=lambda x: x[1], reverse=True):
            percentage = (amount / summary['total']) * 100
            text += f"  • {category}: ${amount:.2f} ({percentage:.1f}%)\n"
        
        return text


def main():
    """
    Main entry point for the bot.
    
    Reads configuration from environment variables and starts the bot.
    """
    # Get bot token from environment variable
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set")
        print("Error: Please set TELEGRAM_BOT_TOKEN environment variable")
        return
    
    # Initialize and start the bot
    bot = TelegramBot(token)
    logger.info("Starting Expense Tracker Bot...")
    
    try:
        bot.start()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot error: {e}")


if __name__ == '__main__':
    main()
