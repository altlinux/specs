Name: hyphen-fr
Summary: French hyphenation rules
Version: 20031004
Release: alt3
Group: Text tools
URL: http://lingucomponent.openoffice.org/hyphenator.html
License: LGPL

Requires: libhyphen

Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_fr_FR.zip

BuildArch: noarch
BuildRequires: unzip

%description
French hyphenation rules.

%prep
%setup -q -c -n %name

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/hyphen
iconv -fISO8859-1 -tUTF-8 hyph_fr_FR.dic > %buildroot%_datadir/hyphen/hyph_fr_FR.dic
subst 's|^ISO8859-1|UTF-8|' %buildroot%_datadir/hyphen/hyph_fr_FR.dic

cd %buildroot%_datadir/hyphen/
fr_FR_aliases="fr fr_BE"
for lang in $fr_FR_aliases; do
	ln -s hyph_fr_FR.dic hyph_$lang.dic
done

%files
%doc README*
%_datadir/hyphen/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 20031004-alt3
- convert to UTF-8

* Sun Dec 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 20031004-alt2
- new varient alias

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20031004-alt1
- initial release
