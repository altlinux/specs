Name: hunspell-tt
Summary: Tatar hunspell dictionaries
Version: 20080617
Release: alt2
Group: Text tools
License: GPLv2

Requires: libhunspell

Source: %name-%version.tar

BuildArch: noarch

%description
Tatar hunspell dictionaries.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_datadir/myspell
install -m644 tt_RU.* %buildroot%_datadir/myspell/

%files
%_datadir/myspell/*

%changelog
* Fri Jun 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080617-alt2
- build for Sisyphus

* Fri Jun 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080617-alt1
- initial release

