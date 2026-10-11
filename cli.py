from markov import markov


bot = markov(order=2)
print("OPTICHAT ITS A MARKOV CHAIN CHATBOT THING :D")
while True:
    user_input = input("\nYou:").strip()
    if not user_input:
        continue

    if user_input.lower() == "/quit":
        break
    bot.train(user_input)
    words = user_input.split()
    seed = words[-1] if words else None
    reply = bot.generate(length=15, seed=seed)
    if reply:
        print(f"Bot: {reply}")
    else:
        print("Bot: Doesn't know enough yet, keep chatting!")