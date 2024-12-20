import pinecone

pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="us-west1-gcp")

index = pinecone.Index("notion-blog")

def upsert_vector(id, embedding, metadata):
    index.upsert([(id, embedding, metadata)])

def query_vector(query_embedding, top_k=5):
    return index.query(query_embedding, top_k=top_k, include_metadata=True)
