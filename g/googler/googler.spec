%global _unpackaged_files_terminate_build 1

Name:    googler
Version: 4.3.13
Release: alt1

Summary: Google Search, Google Site Search, Google News from the terminal
License: GPL-3.0
Group:   Networking/Other
URL:     https://github.com/oksiquatzel/googler

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildArch: noarch

BuildRequires: rpm-build-python3

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%install
make disable-self-upgrade
make install PREFIX=%buildroot%_prefix
rm -rf %buildroot%_defaultdocdir/%name

install -Dm 644 auto-completion/zsh/_googler %buildroot/%_datadir/zsh/site-functions/_%name
install -Dm 644 auto-completion/bash/googler-completion.bash %buildroot/%_sysconfdir/bash_completion.d/%name
install -Dm 644 auto-completion/fish/googler.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%doc README*
%doc %_man1dir/*
%_bindir/%name
%_sysconfdir/bash_completion.d/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Mon Feb 27 2023 Mikhail Gordeev <obirvalger@altlinux.org> 4.3.13-alt1
- new version 4.3.13

* Tue May 11 2021 Mikhail Gordeev <obirvalger@altlinux.org> 4.3.2-alt1
- new version 4.3.2

* Fri Feb 15 2019 Grigory Ustinov <grenka@altlinux.org> 3.7.1-alt1
- new version 3.7.1

* Fri Sep 21 2018 Mikhail Gordeev <obirvalger@altlinux.org> 3.7-alt1
- new version 3.7

* Fri Mar 23 2018 Mikhail Gordeev <obirvalger@altlinux.org> 3.5-alt1
- new version 3.5

* Mon Oct 02 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.3-alt3
- Fix path to zsh completion

* Mon Aug 21 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.3-alt2
- Package autocompletions (zsh, bash, fish)

* Wed Aug 02 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.3-alt1
- Initial build for Sisyphus
