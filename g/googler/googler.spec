%global _unpacked_files_terminate_build 1

Name:    googler
Version: 3.5
Release: alt1

Summary: Google Search, Google Site Search, Google News from the terminal
License: GPL-3.0
Group:   Networking/Other
URL:     https://github.com/jarun/googler

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%install
make disable-self-upgrade
make install PREFIX=%buildroot%_prefix

install -Dm 644 auto-completion/zsh/_googler %buildroot/%_datadir/zsh/site-functions/_%name
install -Dm 644 auto-completion/bash/googler-completion.bash %buildroot/%_sysconfdir/bash_completion.d/%name
install -Dm 644 auto-completion/fish/googler.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%_sysconfdir/bash_completion.d/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish
%_man1dir/*
%_docdir/%name/*

%changelog
* Fri Mar 23 2018 Mikhail Gordeev <obirvalger@altlinux.org> 3.5-alt1
- new version 3.5

* Mon Oct 02 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.3-alt3
- Fix path to zsh completion

* Mon Aug 21 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.3-alt2
- Package autocompletions (zsh, bash, fish)

* Wed Aug 02 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.3-alt1
- Initial build for Sisyphus
