
bot Url: https://discord.com/api/oauth2/authorize?client_id=787975406024261643&permissions=8&scope=bot
Bot_name: Assignment

Features:

1. If a user sends 'hi', the bot will reply 'hey'
2. if a user sends '!google MESSAGE', and it'll reply with the top five links
3. if a user sends '!recent MESSAGE', and it'll reply with a list of similar searches in the user's history

1. Install reqirements.txt

2. Create Table Name:searches
   Create table searches (user_id varchar(256), keyword varchar(256), search_time timestamp);
