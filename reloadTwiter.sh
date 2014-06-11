# put this on cron.daily
kill $(ps aux | grep '[p]ython /usr/local/bin/aaTwitter' | awk '{print $2}')
aaTwiter &
