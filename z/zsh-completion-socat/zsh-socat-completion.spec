Name:           zsh-completion-socat
Version:        2013.0
Release:        alt2
License:        ALT-Public-Domain
Summary:        Zsh completion for socat
BuildArch:      noarch

URL:            https://github.com/Valodim/zsh-socat-completion
Group:          Shells
Source:         _socat
Patch:          ALT-epmty-value.patch

%description
%summary

%prep
cp  %SOURCE0 _socat
%patch 

%install
install -D _socat %buildroot%_datadir/zsh/site-functions/_socat

%files
%_datadir/zsh/site-functions/_socat

%changelog
* Sat Sep 14 2024 Fr. Br. George <george@altlinux.org> 2013.0-alt2
- Apply ZSH _store_cache bug QnD workaround

* Wed Jul 24 2024 Fr. Br. George <george@altlinux.org> 2013.0-alt1
- Initial build for ALT
