Name: hyphen-de
Summary: German hyphenation rules
Version: 20061130
Release: alt3
Group: Text tools
URL: http://lingucomponent.openoffice.org/hyphenator.html
License: LGPL

Requires: libhyphen

Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_de_DE.zip

BuildArch: noarch
BuildRequires: unzip

%description
German hyphenation rules.

%prep
%setup -q -c -n %name

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/hyphen
iconv -fISO8859-1 -tUTF-8 hyph_de_DE.dic > %buildroot%_datadir/hyphen/hyph_de_DE.dic
subst 's|^ISO8859-1|UTF-8|' %buildroot%_datadir/hyphen/hyph_de_DE.dic

cd %buildroot%_datadir/hyphen/
de_DE_aliases="de de_CH"
for lang in $de_DE_aliases; do
	ln -s hyph_de_DE.dic hyph_$lang.dic
done

%files
%doc README*
%_datadir/hyphen/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 20061130-alt3
- convert to UTF-8

* Sun Dec 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 20061130-alt2
- new varient alias

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20061130-alt1
- initial release
