Name: hyphen-tt
Summary: Tatarian hyphenation rules
Version: 20080619
Release: alt2
Group: Text tools
License: GPLv2

Requires: libhyphen

Source: %name-%version.tar

BuildArch: noarch

%description
Tatarian hyphenation rules.

%prep
%setup -q

%build

%install
mkdir -p %buildroot%_datadir/hyphen
install -m644 hyph_tt_RU.dic %buildroot%_datadir/hyphen/

cd %buildroot%_datadir/hyphen/
tt_RU_aliases="tt"
for lang in $tt_RU_aliases; do
	ln -s hyph_tt_RU.dic hyph_$lang.dic
done

%files
%_datadir/hyphen/*

%changelog
* Fri Jun 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080619-alt2
- build for Sisyphus

* Fri Jun 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080619-alt1
- initial release

