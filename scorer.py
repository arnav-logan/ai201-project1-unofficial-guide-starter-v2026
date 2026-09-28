import store
import re

def judge(question: str, expects: str, answer: str, results: list) -> bool:
    # process the expects variable, and check answer for expects count
    answer = answer.lower()
    expects = simplify_answer(expects)
    expectsTerms = expects.split(" ")
    expectsCount = 0

    for term in expectsTerms:
        if term in answer:
            expectsCount += 1

    return expectsCount == len(expectsTerms)

def simplify_answer(answer: str) -> str:
    answer = answer.strip()
    answer = answer.lower()
    answer = re.sub(r"[^A-Za-z0-9\s]", "", answer)
    
    return answer
