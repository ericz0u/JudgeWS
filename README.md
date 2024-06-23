# JudgeWS
Langchain based RAG implementation to help with ruling questions for the card game Weiss Schwarz. 
### 6/21/24
A RAG being able to do judge rulings seems to be pretty easy, my basic llamaindex impelmentation seems to work for pretty much all the rules, maybe needs more training data. I'm playing around more with having a llm play the game, but I think writing out the script for the weiss schwarz simulator like I suggested earlier might be a bit too much for an llm even if I break it down(requires a lot of foresight, planning, ect.). I'll start with just making it make decisions, prompts for each game phase I think that's totally doable. Learning langchain though I feel like while the basics is really simple, there's just so many packages and third party things that the more I look at things the less certain I get lol. 

One of the most underrated things I've looked at that pretty much all the tutorials just glossed over is the openAI temperature variable I spent so long at first prompt engineering it to only reply when it was 100% sure of the answer, but just by turning the temperature down to something like 0.7 I got what I wanted. Probably the biggest thing that helped in making it work for game judge rulings.
### 6/18/24
Studied up on different embedding and text splitting methods. As my documents are pretty short themselves, I think sticking with just length-based text splitting is good enough(although I'll probably end up trying different methods later). I started to use openAI embeddings, and the results are noticably better. Best results so far and seems to be pretty reliable. 
### 6/13/24
Experimented with using llms to make embeddings. Had great progress, the chatbot can now "understand" a lot more, if I put in a guide to playing a deck it can spit out what to do in situations and even how to counter the deck. having this chatbot make the 'AI' scripts for a game is totally doable.
### 6/12/24
Spent a couple hours today experimenting with the possibility of being able to play the game. While llms have no thinking or logic, maybe if I feed it enough guides it can spit out answers that are good enough! I started by seeing if it could make an ai for the weiss schawrz simulator. All "ai" in there are hardcoded, so it shouldn't be that much of a challenge as long as the RAG works and my chatbot can understand the cards. I found that it was having trouble looking through all the cards, and it only asks a couple questions. I think for this to work rather than having it just look at a list of all the cards I might need to make a file where I tag cards, or label what they are. Another solution might be to tack on more llms, having them ask questions to eachother. 

Ended up making a script to turn the files into a csv to be parseable(setToCSV). Took me a while but was a good refresher on regular expressions lol. The plan now is to give the model data on the cards first using this tabular data, then have it ask questions. I found that even with the perfect data, it would get answers right but just hallucinate answers 1/5 of the times. While this could be fixed with an answer parser/hallucination checker llm, I'd rather just pass in basic information with python so there's a 0% chance of error. The llm can then make decisions and ask more questions from there
### 6/11/24
Played around with llamaindex, making a first working POC with just a document retriever and openAI api. It provides correct answers on most simple new-player questions like *"do cards go back into the deck on refresh after brainstorming"*, but it struggles on some rarer situations. For example *"If the last card in deck is dealt as damage what comes first: refresh damage or that damage"* either gives a wrong answer or gives an unrelated answer even after tweaking the question. I think(hopefully) this can be solved after implementing the other two "checker" llms.

If you ask what a specific card does, it can get that correctly but if you ask what cards have an effect, it just makes stuff up. I found that it's a lot better if rather than one document with every card in it, I have a folder for the set of cards then each card is a text file with the effects inside. That would be thousands of text files though, so I'll try and find another way. maybe a json file for each set with tags? Or possible use a different embedding/vector store
###  6/10/24
Starting off, I'm going to use RAG as opposed to fine tuning because I'm not too concerned about the exact wording, but I want to throw in various documents on the rules(as of now, 2 official rule PDFs and 10 blog posts). I won't be implementing an internet search function as there isn't much online content and the bits that exist(mostly reddit) are questionably reliable... I've started with a llamaindex "template", but plan to add onto it. The current plan is to use llama/openAI, a generic document retriever(I don't have enough documents to justify a database... I think), into two llms: one to check accuracy and one to make sure the output answers the initial question.
