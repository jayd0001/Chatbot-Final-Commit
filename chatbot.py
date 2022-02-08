from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'ChatBot',
     storage_adapter='chatterbot.storage.SQLStorageAdapter',
   logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': '<b>Press 0 for Campus</b> <br> <b>Press 1 for Admission</b> <br> <b>Press 2 for Eligibility</b> <br> <b>Press 3 for Rural Quota</b> <br> <b>Press 4 for BTech</b> <br> <b>Press 5 for MTech</b> <br> <b>Press 6 for Fee Waiver</b> <br> <b>Press 7 for Sikh Quota</b> <br> <b>Press 8 for Scholarship</b> <br> <b>Press 9 for MBA Or BBA</b> <br> <b>Press * for MCA Or BCA</b> <br> <b>Press # for Ph.D</b>',
            'maximum_similarity_threshold': 0.65
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(chatbot)



 # Training with Personal Ques & Ans 
training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)  

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 