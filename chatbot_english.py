from chatterbot import ChatBot

bot = ChatBot(
              'Luigi',
              storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
              logic_adapters=[
                              "chatterbot.logic.BestMatch"
                              ],
              input_adapter='chatterbot.input.TerminalAdapter',
              output_adapter='chatterbot.output.TerminalAdapter',
              trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
              database='chatterbot-database'
              )

bot.train("corpus_data/")
          
CONVERSATION_ID = bot.storage.create_conversation()

def get_feedback():
    from chatterbot.utils import input_function
    
    text = input_function()
    
    if 'yes' in text.lower():
        return False
    elif 'no' in text.lower():
        return True
    elif 'maybe' in text.lower():
        print('ok')
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()


print("Type something to begin...")

# The following loop will execute each time the user enters input
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

# Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
