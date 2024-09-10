from langchain_groq import ChatGroq
import langchain
langchain.verbose = False
langchain.debug = False
langchain.llm_cache = False

def create_llm_client():
    llm = ChatGroq(
        model="llama3-70b-8192",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key = "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"
    )
    return llm

if __name__ == "__main__":
    try:
        llm = create_llm_client()
        while True:
            user_input = input("Question : ")
            response = llm.invoke(user_input)
            print(response.content)
    except Exception as e:
        print(f"An error occurred: {e}")