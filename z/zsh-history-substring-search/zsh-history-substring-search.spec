Name: zsh-history-substring-search
Version: 1.1.0
Release: alt1

Summary: ZSH port of Fish history search (up arrow)
License: BSD-3-Clause
Group: Shells
Url: https://github.com/zsh-users/zsh-history-substring-search
VCS: https://github.com/zsh-users/zsh-history-substring-search
BuildArch: noarch

Source: %name-%version.tar

Requires: zsh >= 4.3

%description
This is a clean-room implementation of the Fish shell's history search
feature, where you can type in any part of any command from history and
then press chosen keys, such as the UP and DOWN arrows, to cycle through
matches.

%prep
%setup

%install
install -Dm 644 %name.plugin.zsh %buildroot%_datadir/zsh/plugins/%name/%name.plugin.zsh
install -Dm 644 %name.zsh %buildroot%_datadir/zsh/plugins/%name/%name.zsh

%files
%doc README.md
%_datadir/zsh/plugins/%name

%changelog
* Sat Mar 21 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 1.1.0-alt1
- Initial build for ALT.

