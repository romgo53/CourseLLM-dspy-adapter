import dspy
from typing import List, Dict
from md_loader import load_markdown_file

lm = dspy.LM("gemini/gemini-2.0-flash", api_key="AIzaSyDU45KHIpqK7KGruLyscjsBkW7Qb2uVbSc")


class TopicExtractor(dspy.Signature):
    """Extract the topics from text that are relevant to the content."""

    text: str = dspy.InputField()
    topic: List[str] = dspy.OutputField()




if __name__ == "__main__":
    # sample_text = """# Introduction to Machine Learning
    # Machine learning is a subset of artificial intelligence that focuses on building systems that can learn from and make decisions based on data. It has applications in various fields such as healthcare, finance, and marketing.
    # ## Supervised Learning
    # Supervised learning involves training a model on a labeled dataset, where the input data is paired with the correct output. Common algorithms include decision trees, support vector machines, and neural networks.
    # ## Unsupervised Learning
    # Unsupervised learning deals with unlabeled data and aims to find hidden patterns or intrinsic structures within the data. Clustering and dimensionality reduction are common techniques used in unsupervised learning.
    # """

    sample_text = load_markdown_file("app\\01_programming_fundamentals.md")
    print(sample_text[:10])
    dspy.configure(lm=lm)
    # extractor = dspy.Predict(TopicExtractor)
    # res = extractor(context="", text=)
    extruct = dspy.ChainOfThought("context, text -> topic: List[str]")

    res = extruct(text=sample_text)
    print(res)