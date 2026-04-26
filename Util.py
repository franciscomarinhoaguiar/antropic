class Util:
    def __init__(self, client, model):
        self.client = client
        self.model = model
        
    def add_user_message(self, messages, text):
        user_message = {
        "role": "user",
        "content": text
        }
        messages.append(user_message)
        
    def add_assistant_message(self, messages, text):
        assistant_message = {
            "role": "assistant",
            "content": text
        }
        messages.append(assistant_message)
        
    def chat(self, messages):
        return self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=messages
        )
    def chat_system_prompts(self, messages, system):
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=messages,
            system=system
        )
        return message.content[0].text
    
    def chat(self,messages, system=None, temperature=1.0, stop_sequences=None):
        params = {
        "model": self.model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
        }
    
        if system:
            params["system"] = system
        if stop_sequences:
            params["stop_sequences"] = stop_sequences
    
        message = self.client.messages.create(**params)
        return message.content[0].text
    
    def chat_stream(self, messages):
        stream = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=messages,
            stream=True
        )
        for event in stream:
            print(event)

    def chat_stream_with(self, messages):
        with self.client.messages.stream(
            model=self.model,
            max_tokens=1000,
            messages=messages,
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
        print()
        #stream.get_final_message()
        
