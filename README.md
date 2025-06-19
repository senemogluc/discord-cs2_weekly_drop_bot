# Discord Multi-Utility Bot

A modular and extensible Discord bot built with Python and `discord.py`. This bot offers various commands and features including:

- 🎮 **CS2 Weekly Drop Reset Countdown**
- 🛠️ **Role assignment/removal**
- 💬 **DM messaging**
- 📦 Support for additional modular cogs (command modules)

---

## 📁 Project Structure

```
project-root/
├── bot.py
├── requirements.txt
├── railway.toml
├── .env                 # Only used for local development
├── cogs/                # Modular command files
│   └── general.py
├── services/            # Reusable service logic
│   └── cs2_service.py
└── config/
    └── environment_variables_config.py
```

---

## 🚀 Features

- **CS2 Countdown**: Shows the time left until the next CS2 weekly drop reset (resets every Wednesday 03:00 AM UTC+3).
- **Hybrid Commands**: Works with both `!prefix` and `/slash` commands.
- **Role Management**: Self-assign or remove roles using command autocomplete.
- **Direct Messaging**: Let users receive bot messages via DM.
- **Logging**: All command usage and errors are logged to `discord.log`.

---

## 🧪 Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/discord-multi-utility-bot.git
cd discord-multi-utility-bot
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # On Linux/macOS
.venv\Scripts\activate         # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a `.env` file with your bot token:

```
DISCORD_TOKEN=your_token_here
```

### 5. Run the bot

```bash
python bot.py
```

---

## ☁️ Deployment on Railway

1. Push your code to GitHub
2. Go to [Railway](https://railway.app/)
3. Create a new project and link your GitHub repo
4. In the **Environment** tab, add:
   ```
   DISCORD_TOKEN=your_token_here
   ```
5. Ensure your `railway.toml` contains:

```toml
[build]
builder = "nixpacks"
buildCommand = "pip install -r requirements.txt"

[deploy]
startCommand = "python bot.py"
restartPolicyType = "on_failure"
```

6. Done! Railway will build and run your bot in the cloud.

---

## 📜 License

MIT License. Feel free to fork, modify, and contribute.

---

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 💡 Credits

Made with ❤️ by [your-name]  
Powered by [discord.py](https://discordpy.readthedocs.io/)