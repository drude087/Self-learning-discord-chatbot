import discord
from discord.ext import commands
import json
from difflib import get_close_matches

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

def load_info(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_info(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question: str, info: dict) -> str | None:
    for q in info["questions"]:
        if q["questions"] == question:
            return q["answer"]

info = load_info('info.json')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore messages sent by the bot itself
        return

    user_input = message.content.lower()

    if user_input == 'quit':
        await message.channel.send("Exiting...")
        await bot.close()

    if user_input in ['skip', 'explain']:
        return

    best_match = find_best_match(user_input, [q["questions"] for q in info["questions"]])
    if best_match:
        answer = get_answer(best_match, info)
        await message.channel.send(f'{answer}')
    else:
        await message.channel.send("I don't understand this. Explain?")
        explanation_message = await bot.wait_for('message', check=lambda m: m.author == message.author)
        new_answer = explanation_message.content

        if new_answer.lower() != 'skip':
            info["questions"].append({"questions": user_input, "answer": new_answer})
            save_info('info.json', info)
            await message.channel.send('Bot: Thank you')

if __name__ == '__main__':
    bot.run('your discord bot token')
