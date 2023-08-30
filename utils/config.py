import os 



# Set up Postgres database credentials
db_credentials = {
    'dbname'    :   os.getenv("PGDATABASE"),# Original var SEMANTIC_DB
    'user'      :   os.getenv("PGUSER"), # Original var POSTGRES_USERNAME
    'password'  :   os.getenv("PGPASSWORD"), #Original var POSTGRES_PASSWORD
    'host'      :   os.getenv("PGHOST"), # Original var HOST
    'port'      :   os.getenv("PGPORT") # Original var PORT
}


# Set up OpenAI variables 
OPENAI_API_KEY  =   os.getenv("OPENAI_API_KEY")
AI_MODEL        =   'gpt-3.5-turbo-16k'
# AI_MODEL        =   'gpt-4'



# Max number of tokens permitted within a conversation exchange via OpenAI API
MAX_TOKENS_ALLOWED      =   3000


# Max number of messages to exchange with OpenAI API
MAX_MESSAGES_TO_OPENAI  =   5



# An arbitrary number to provide a buffer to avoid reaching exact token limits
TOKEN_BUFFER            =   100  
