from duckduckgo_search import DDGS
from rich import print

results = DDGS().news(
    keywords="btc", 
    region="wt-wt", 
    safesearch="off", 
    timelimit="m", 
    max_results=1
)

# print(results)
print(results[0])

for key,value in results[0].items():
    print(f"{key}: {value}")