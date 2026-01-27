from openai import OpenAI

client = OpenAI()

def answer_question(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
    You are a financial analyst.
    Answer the question using only the context provided.

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
