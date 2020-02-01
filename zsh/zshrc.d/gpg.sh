export GPG_TTY=$(tty)

# In order for gpg to find gpg-agent, gpg-agent must be running,
# and there must be an env variable pointing GPG to the gpg-agent socket.
if [ -n "$(pgrep gpg-agent)" ]; then
    # No need to start the agent if it is running
else
    eval $(gpg-agent --daemon ~/.gnupg/.gpg-agent-info)
fi
