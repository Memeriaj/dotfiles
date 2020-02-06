# Start the ssh-agent if it isn't already running
if [ -n "$(pgrep ssh-agent)" ]; then
    # Already running, maybe set some env var?
else
    eval "$(ssh-agent -t 12h -s)"
fi