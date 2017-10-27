# A chatbot trained with « The Big Bang Theory » dialogues

Conversational modelling is an important task in natural language processing as well as machine learning. A model was trained using the dialogues of a popular TV show: “The Big Bang Theory”. 
The chatbot has been developed using Python on IBM PowerAI for IBM Power Systems, ChatterBot a Python library using a selection of machine learning algorithms to produce different types of responses, MongoDB to store statements and dialogues. ChatterBot is really easy to install and use. 

The result is quite funny: 

# To run the code:

* Install ChatterBot: https://github.com/gunthercox/ChatterBot
* Install MongoDB: https://docs.mongodb.com/manual/administration/install-community/
* Download The Big Bang Theory Corpus: https://github.com/skashyap7/TBBTCorpus
* Use yml_converter.py in utils to the raw data (preprocessing/raw_corpus/). You will need to change input/outputs in the file. 
* Copy/Paste the output (filename.yml) in corpus_data
* Before running the code, do not forget to start Mongodb:

      mongod --dbpath <path to data directory>

Then,

      python3 chatbot_english.py

The following part of the code aims to provide feedback to the chatbot. Just comment this part if you want to stop providing feedback. 

      while True:
        try:
            input_statement = bot.input.process_input_statement()
            statement, response = bot.generate_response(input_statement, CONVERSATION_ID)
            bot.output.process_response(response)
            print('\n Is "{}" a coherent response to "{}"? \n'.format(response, input_statement))
            if get_feedback():
                  print("please input the correct one")
                  response1 = bot.input.process_input_statement()
                  bot.learn_response(response1, input_statement)
                  bot.storage.add_to_conversation(CONVERSATION_ID, statement, response1)
                  print("Responses added to bot!")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


If you run it on IBM Power Systems:

Install IBM PowerAI for IBM Power Systems: https://www.ibm.com/bs-en/marketplace/deep-learning-platform/details

PowerAI is a software distribution for machine learning running on the Enterprise Platform for AI: IBM Power Systems. IBM PowerAI includes most ML/DL frameworks built with optimized versions of leading frameworks including: Caffe-bvlc, Caffe-ibm, Caffe-nv, Chainer, DIGITS, Torch, Theano, and TensorFlow.
Software requirements Ubuntu 16.04 LTS
