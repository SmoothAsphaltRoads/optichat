from markov import markov
import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
console = Console()
bot = markov(order=2)
def Banner():
    banner = Text(r"""
                        $$\     $$\           $$\                  $$\     
                        $$ |    \__|          $$ |                 $$ |    
    $$$$$$\   $$$$$$\ $$$$$$\   $$\  $$$$$$$\ $$$$$$$\   $$$$$$\ $$$$$$\   
    $$  __$$\ $$  __$$\\_$$  _|  $$ |$$  _____|$$  __$$\  \____$$\\_$$  _|  
    $$ /  $$ |$$ /  $$ | $$ |    $$ |$$ /      $$ |  $$ | $$$$$$$ | $$ |    
    $$ |  $$ |$$ |  $$ | $$ |$$\ $$ |$$ |      $$ |  $$ |$$  __$$ | $$ |$$\ 
    \$$$$$$  |$$$$$$$  | \$$$$  |$$ |\$$$$$$$\ $$ |  $$ |\$$$$$$$ | \$$$$  |
    \______/ $$  ____/   \____/ \__| \_______|\__|  \__| \_______|  \____/ 
            $$ |                                                          
            $$ |                                                          
            \__|
    """, style = "bold cyan")
    console.print(banner)
def slow_typing(text):
    console.print("[bold green]Bot:[/bold green]", end = "")
    for word in text.split():
        console.print(word + " ", end = "", highlight = False)
        time.sleep(random.uniform(0.03, 0.15))
    console.print()
def help():
    helplist = Text()
    helplist.append("/quit", style="bold yellow")
    helplist.append ("       -> quit optichat\n")
    helplist.append ("/clear", style="bold yellow")
    helplist.append ("       -> clear past messages\n")
    helplist.append("/stats", style = "bold yellow")
    helplist.append("        -> show the stats of your chat")
    console.print(Panel(helplist, title="[bold]Commands[/bold]", border_style="yellow"))
def stats():
    total_states = len(bot.chain)
    total_words = sum(len(v) for v in bot.chain.values())
    text = Text()
    text.append(f"Order: {bot.order}\n")
    text.append(f"Unique States: {total_states}")
    text.append(f"Total Words: {total_words}")
    console.print(Panel(text, title="[bold]Stats[/bold]", border_style="green"))

console.clear()
Banner()
console.print("[dim] type /help for commands[/dim] \n")
while True:
    try:
        user_in = Prompt.ask("[bold blue]You[/bold blue]")
    except(KeyboardInterrupt):
        break
    command = user_in.lower().strip()
    if command == "/quit":
        break
    elif command == "/help":
        help()
        continue
    elif command == "/stats":
        stats()
        continue
    bot.train(user_in)
    words = user_in.split()
    seed = words[-1] if words else None
    reply = bot.generate(length=15, seed = seed)
    if reply:
        slow_typing(reply)
    else:
        console.print("[dim] Bot: I dont know enough, continue chatting! [/dim]")
    