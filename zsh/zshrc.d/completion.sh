autoload -Uz compinit
compinit
fpath[1,0]=~/.zsh/completion/
mkdir -p ~/.zsh/cache
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path ~/.zsh/cache