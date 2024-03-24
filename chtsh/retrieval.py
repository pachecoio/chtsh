from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent, load_tools
from langchain.agents import AgentExecutor
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool


def chat_openai():
    return ChatOpenAI(model="gpt-4", temperature=0)


def query_with_serpapi(input, llm_factory=chat_openai):
    search = SerpAPIWrapper()
    search_tool = Tool(
        name="search",
        description="Search the web for information",
        func=search.run,
    )
    tools = [search_tool]
    llm = llm_factory()

    # Get the prompt to use - you can modify this!
    prompt = hub.pull("hwchase17/openai-functions-agent")

    agent = create_openai_functions_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor.invoke({"input": input})


def coding_query(input, llm_factory=chat_openai):
    tools = load_tools(['serpapi'])
    llm = llm_factory()
    prompt = hub.pull("hwchase17/openai-functions-agent")
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor.invoke({"input": input})

