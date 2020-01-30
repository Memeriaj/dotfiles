autoload -U colors && colors
PS1="%{$fg[red]%}%n%{$reset_color%}@%{$fg[cyan]%}%m %{$fg[yellow]%}%(5~|%-1~/.../%3~|%4~) %{$reset_color%}$ "