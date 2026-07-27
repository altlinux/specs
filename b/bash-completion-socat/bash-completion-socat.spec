Name: bash-completion-socat
Version: 1.0
Release: alt1

Summary: Bash completion for socat
License: GPL-3.0-or-later
Group: Shells
URL: https://man7.org/linux/man-pages/man1/socat.1.html

BuildArch: noarch

Source: %name-%version.tar

%description
socat [options] <address> <address>
Advanced bash completion for socat. It can suggest not only flags
and addresses, but also names of address parameters after commas.

%prep
%setup

%install
install -pD -m644 socat %buildroot%_datadir/bash-completion/completions/socat

%files
%_datadir/bash-completion/completions/socat

%changelog
* Thu Jul 23 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt1
- Initial build.
