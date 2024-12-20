import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_embedding(text):
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response["data"][0]["embedding"]

if __name__ == "__main__":
    sample_text = "This is a test blog post."
    embedding = generate_embedding(sample_text)
    print(embedding)
