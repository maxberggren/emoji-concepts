source .env
echo 'Sending all changed files to server:' $SERVER_NAME
rsync -arv ~/Code/emoji-concepts/* root@$SERVER_ADDR: --exclude '__pycache__' --exclude '.DS_Store' --exclude 'db.sqlite'
rsync -arv ~/Code/emoji-concepts/.env root@$SERVER_ADDR: