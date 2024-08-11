# import os
from mem0 import Memory

# from dotenv import load_dotenv
# 
# lad_dotenv()

config = {
    "llm": {
        "provider": "openai",
        "config": {
            # "api_key": os.environ.get("OPENAI_API_KEY"),
            # "openrouter_base_url": "https://api.deepseek.com/v1",
            "model": "deepseek-chat",
            "temperature": 0.2,
            "max_tokens": 1500,
        },
    }
}

m = Memory().from_config(config)

# For a user
result = m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})

print(result)

# result = m.update(memory_id=<memory_id_1>, data="Likes to play tennis on weekends")
