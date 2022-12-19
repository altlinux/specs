Name: ddgr
Version: 2.1
Release: alt1

Summary: DuckDuckGo from the terminal

License: GPLv3+
Group: Other
Url: https://github.com/jarun/ddgr

# Source-url: https://github.com/jarun/ddgr/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3

%description
ddgr is a cmdline utility to search DuckDuckGo from the terminal.
While googler is highly popular among cmdline users, in many forums the need
of a similar utility for privacy-aware DuckDuckGo came up. DuckDuckGo Bangs
are super-cool too! So here's ddgr for you!

Unlike the web interface, you can specify the number of search results you
would like to see per page. It's more convenient than skimming through
30-odd search results per page. The default interface is carefully
designed to use minimum space without sacrificing readability.

ddgr isn't affiliated to DuckDuckGo in any way.

%prep
%setup

%__subst "s|\tinstall -|\t\$(INSTALL) -|" Makefile
%__subst '1s/env //' ddgr

%build
# Nothing to do

%install
%makeinstall_std PREFIX=%prefix
install -Dpm0644 -t %buildroot%_datadir/bash-completion/completions \
  auto-completion/bash/ddgr-completion.bash
install -Dpm0644 -t %buildroot%_datadir/fish/vendor_functions.d \
  auto-completion/fish/ddgr.fish
install -Dpm0644 -t %buildroot%_datadir/zsh/site-functions \
  auto-completion/zsh/_ddgr

rm -fv %buildroot/usr/share/doc/ddgr/README.md

%check
make test

%files
%doc CHANGELOG README.md
%doc --no-dereference LICENSE
%_bindir/%name
%_man1dir/%name.1*
%_datadir/bash-completion/completions/ddgr-completion.bash
%dir %_datadir/fish/vendor_functions.d
%_datadir/fish/vendor_functions.d/ddgr.fish
%dir %_datadir/zsh/site-functions
%_datadir/zsh/site-functions/_ddgr

%changelog
* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version 2.1 (with rpmrb script)

* Sat Apr 02 2022 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- new version 2.0 (with rpmrb script)

* Sat May 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt2
- use BR: rpm-build-python3

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- new version 1.9 (with rpmrb script)

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Sun Feb 16 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt2
- build for ALT Sisyphus

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_1
- new version

