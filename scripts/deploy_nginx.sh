source .env
echo 'Deploying http nginx on server:' $SERVER_NAME
# Pull environment variables from .env and use template before deploying
DOLLAR="$" SERVER_DOMAIN="$SERVER_DOMAIN" envsubst < scripts/nginx.conf.template > scripts/nginx.conf
rsync -aP scripts/nginx.conf root@$SERVER_ADDR:/../etc/nginx/nginx.conf
ssh root@$SERVER_ADDR nginx -s reload
echo "Running command to create https"
ssh -t root@$SERVER_ADDR "sudo certbot --nginx"