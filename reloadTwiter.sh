# put this on cron.daily
kill $(ps aux | grep '[p]ython /usr/local/bin/aaTweeter' | awk '{print $2}')
aaTweeter &
