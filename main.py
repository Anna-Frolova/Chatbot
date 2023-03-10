# newer versions of chatterbot sometimes can be broken by invalid version of its dependencies,
# so we installed chatterbot lib using this commands:

# git clone https://github.com/feignbird/ChatterBot-spacy_fixed
# pip3 install ./ChatterBot-spacy_fixed 　  pip3にしたらできた
# pip3 install chatterbot-corpus　　　　　　　pip3にしたらできた
# pip3 uninstall pyYAML　　　　　　　　　　　 　pip3にしたらできた
# pip3 install pyYAML==5.3.1　　　　　　　　 　pip3にしたらできた
# python -m spacy download en_core_web_sm　 pip3にしたらできた

# ChatterBot-spacy_fixed - this is a fork of original chatterbot repo with
# some minor fixes for spaCy library used in chatterbot library

# chatterbot-corpus is module with some training dataset(just a bunch of text data)

# ChatterBot-spacy_fixed requires pyYAML specifically version of 5.3.1
# so wee need to uninstall already installed version and install exactly 5.3.1

# 'python -m spacy download en_core_web_sm' command is used to download dataset for spacy that is used in chatterbot

# chatterbot library documentation https://chatterbot.readthedocs.io/en/stable/index.html
# possible dataset for future training https://www.kaggle.com/code/kagarg/chatbot/notebook
# dataset used in UbuntuCorpusTrainer https://www.kaggle.com/datasets/rtatman/ubuntu-dialogue-corpus/versions/1

# UbuntuCorpusTrainer - huge conversation dataset trainer
# ChatterBotCorpusTrainer - trainer that allows to train on specific datasets of text
#                           (also allows to specify corpus scope in train(...) method
# ListTrainer - trainer that allows to train bot on list of questions and responses
#               (list of strings formed in 'question, answer' fashion)

# Trainer is used to actually train chatbot on given set of data
# Logic Adapters is responsible for logic behind selecting answer to given data
# Storage Adapters is used to specify how to store bots conversation and training history

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

CHAT_BOT_NAME = 'TestBot'
FLOW_EXIT_KEYWORDS = ("quit", "exit")

# create chatbot object given its name, logic and storage adapters
chatbot = ChatBot(
    name=CHAT_BOT_NAME,
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',  # により、数式の評価が可能です。
        'chatterbot.logic.BestMatch',  # 与えられた質問に対する答えを、データセットの中で最もよく知っているものから選択する。
        'chatterbot.logic.TimeLogicAdapter'  # は、時間に関する記述を識別することができます
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',  # 単一ファイルデータベース形式のストレージアダプタ
    database_uri='sqlite:///chatbot_data.sqlite3'  # ストレージアダプタが必要とするデータベースのURIA
)

# Train created bot using  ListTrainer
trainList = [
    "How are you doing?",
    "Fuck you",
    "Do you like cats?",
    "Yes, I do",
    "You are peace of shit",
    "Of course"
]
ListTrainer(chatbot).train(trainList)

user_name = input('What is your name? ')

while True:
    question = input(f"{user_name}: ")
    if question in FLOW_EXIT_KEYWORDS:
        print('Flow exit keyword detected. Exiting.')
        break
    else:
        print(f"{CHAT_BOT_NAME}: {chatbot.get_response(question)}")
