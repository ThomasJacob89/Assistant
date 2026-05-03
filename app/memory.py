# super simple placeholder
# replace with FAISS later

memory_store = []

def add_memory(text: str):
    memory_store.append(text)

def get_context(query: str):
    # naive: return last 3 entries
    return "\n".join(memory_store[-3:])