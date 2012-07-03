Name: hyphen-ru
Summary: Russian hyphenation rules
Version: 20020727
Release: alt3
Group: Text tools
URL: http://lingucomponent.openoffice.org/hyphenator.html
License: LGPL

Requires: libhyphen

Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_ru_RU.zip

BuildArch: noarch
BuildRequires: unzip

%description
Russian hyphenation rules.

%prep
%setup -q -c -n hyphen-ru

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/hyphen
iconv -fKOI8-R -tUTF-8 hyph_ru_RU.dic > %buildroot%_datadir/hyphen/hyph_ru_RU.dic
subst 's|^KOI8-R|UTF-8|' %buildroot%_datadir/hyphen/hyph_ru_RU.dic

cd %buildroot%_datadir/hyphen/
ru_RU_aliases="ru"
for lang in $ru_RU_aliases; do
	ln -s hyph_ru_RU.dic hyph_$lang.dic
done

%files
%doc README_hyph_ru_RU.txt
%_datadir/hyphen/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 20020727-alt3
- convert to UTF-8

* Sun Dec 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 20020727-alt2
- new varient alias

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20020727-alt1
- initial release
