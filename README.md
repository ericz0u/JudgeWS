# JudgeWS
Langchain based RAG implementation to help with ruling questions for the card game Weiss Schwarz. 
### 6/11/24
Played around with llamaindex, making a first working POC with just a document retriever and openAI api. It provides correct answers on most simple new-player questions like *"do cards go back into the deck on refresh after brainstorming"*, but it struggles on some rarer situations. For example *"If the last card in deck is dealt as damage what comes first: refresh damage or that damage"* either gives a wrong answer or gives an unrelated answer even after tweaking the question. I think(hopefully) this can be solved after implementing the other two "checker" llms.

###  6/10/24
Starting off, I'm going to use RAG as opposed to fine tuning because I'm not too concerned about the exact wording, but I want to throw in various documents on the rules(as of now, 2 official rule PDFs and 10 blog posts). I won't be implementing an internet search function as there isn't much online content and the bits that exist(mostly reddit) are questionably reliable... I've started with a llamaindex "template", but plan to add onto it. The current plan is to use llama/openAI, a generic document retriever(I don't have enough documents to justify a database... I think), into two llms: one to check accuracy and one to make sure the output answers the initial question.
