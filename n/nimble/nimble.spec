Name: nimble
Version: 0.14.2
Release: alt1
License: MIT
Group: Development/Other
Summary: A package manager for the Nim programming language
Source: %name-%version.tar.gz
BuildRequires: nim-lang /proc
Requires: nim-lang

%description
Nimble is the default package manager for the Nim programming language.

%prep
%setup

%build
nim c src/nimble.nim

%install
install -D src/nimble %buildroot/%_bindir/nimble
install -D nimble.bash-completion %buildroot%_datadir/bash-completion/completions/nimble
install -D nimble.zsh-completion %buildroot%_datadir/zsh/site-functions/_nimble

%files
%doc *.markdown
%_bindir/*
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*

%changelog
* Mon Jun 05 2023 Fr. Br. George <george@altlinux.org> 0.14.2-alt1
- Autobuild version bump to 0.14.2

* Mon Jun 05 2023 Fr. Br. George <george@altlinux.ru> 0.14.1-alt1
- Initial build for ALT
