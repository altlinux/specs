Name:           zsh-completion-socat
Version:        2013.0
Release:        alt1
License:        ALT-Public-Domain
Summary:        Zsh completion for socat
BuildArch:      noarch

URL:            https://github.com/Valodim/zsh-socat-completion
Group:          Shells
Source:         _socat

%description
%summary

%install
install -D %SOURCE0 %buildroot%_datadir/zsh/site-functions/_socat

%files
%_datadir/zsh/site-functions/_socat

%changelog
* Wed Jul 24 2024 Fr. Br. George <george@altlinux.org> 2013.0-alt1
- Initial build for ALT
