from src.langgraphagenticai.state.bloggenerator_state import BlogGeneratorState

class BlogGeneratorNode:
    def __init__(self, model):
        self.llm = model

    def titleagent(self, state: BlogGeneratorState):
        """LLM call to generate title"""
        msg=self.llm.invoke(
            "<instruction>"
            f"You are an intelligent blog title generator. Your task is to create catchy, engaging,and relevant single title based on the {state['topic']} provided to you \n" + \
            "Ensure that the titles are concise, informative, and tailored to attract readers' attention. Aim for creativity while maintaining clarity and relevance to the topic at hand."
            "</instruction>"
            )
        return {"title": msg.content}
    
    def blogagent(self, state: BlogGeneratorState):
        """LLM call to generate blog"""
        blog=self.llm.invoke(
            "<instruction>"
            f"You are an intelligent blog content generator. Your task is to create a blog content based on the {state['topic']} provided to you \n" + \
            "Ensure that the blog is informative, engaging, and tailored to attract readers' attention. Aim for clarity, depth, and engagement while maintaining a high level of quality and accuracy."
            "</instruction>"
            )
        return {"blog": blog.content}
    
    def finalblogagent(self, state: BlogGeneratorState):
        """Combine the title and blog into a single output"""

        combined = f"Here's a title and blog about {state['topic']}!\n\n"
        combined += f"Title:\n{state['title']}\n\n"
        combined += f"Blog:\n{state['blog']}\n\n"
        return {"finalblog": combined}
    
    def process(self, state: BlogGeneratorState):
        """process for generating a final blog
        """
        return {"topic":self.llm.invoke(state['topic'])}