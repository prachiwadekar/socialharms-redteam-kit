from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()
reply = client.messages.create(
    model ="claude-haiku-5-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "Say hello in five words"}],
)
print(reply.content[0].text)