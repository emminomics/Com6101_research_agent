class MemoryBuffer:
    def __init__(self, max_turns: int = 5):
        """
        Short-term memory buffer.
        Args:
            max_turns (int): Number of turns to remember
        """
        self.max_turns = max_turns
        self.buffer = []

    def add(self, role: str, content: str):
        """
        Add a message to memory.
        Args:
            role (str): 'user' or 'agent'
            content (str): message text
        """
        self.buffer.append({"role": role, "content": content})
        # Keep only last N turns
        if len(self.buffer) > self.max_turns:
            self.buffer.pop(0)

    def get_context(self):
        """
        Return memory buffer as context string.
        """
        return "\n".join([f"{m['role']}: {m['content']}" for m in self.buffer])
