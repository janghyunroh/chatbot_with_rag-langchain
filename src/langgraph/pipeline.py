from langgraph import Graph, Node

def create_rag_pipeline():
    graph = Graph()

    # Node: 질문 임베딩 생성
    question_embedding_node = Node(
        name="question_embedding",
        function=lambda question: generate_embedding(question),
        input_keys=["question"],
        output_keys=["query_embedding"]
    )

    # Node: 벡터 데이터베이스 검색
    vector_search_node = Node(
        name="vector_search",
        function=lambda query_embedding: query_vector(query_embedding),
        input_keys=["query_embedding"],
        output_keys=["retrieved_docs"]
    )

    # Node: GPT 응답 생성
    answer_generation_node = Node(
        name="generate_answer",
        function=lambda docs: gpt_generate_answer(docs),
        input_keys=["retrieved_docs"],
        output_keys=["answer"]
    )

    # 워크플로우 구성
    graph.add_nodes([question_embedding_node, vector_search_node, answer_generation_node])
    graph.link(question_embedding_node, vector_search_node)
    graph.link(vector_search_node, answer_generation_node)

    return graph

if __name__ == "__main__":
    pipeline = create_rag_pipeline()
    response = pipeline.run({"question": "What is LangGraph?"})
    print(response["answer"])
