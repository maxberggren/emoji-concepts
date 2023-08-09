source .env
rsync -aP scripts/supervisor.conf root@$SERVER_ADDR:/../etc/supervisor/conf.d/supervisor.conf 