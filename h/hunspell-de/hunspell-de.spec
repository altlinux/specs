Name: hunspell-de
Summary: German hunspell dictionaries
Version: 20051111
Release: alt3
Group: Text tools
License: GPL
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/

Source0: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/de_DE.zip
Source1: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/de_CH.zip

Requires: libhunspell

BuildArch: noarch
BuildRequires: unzip

%description
German (Germany, Switzerland, etc.) hunspell dictionaries.

%prep
%setup -q -c -n %name -a1

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/myspell
iconv -fISO8859-1 -tUTF-8 de_DE.aff > %buildroot%_datadir/myspell/de_DE.aff
iconv -fISO8859-1 -tUTF-8 de_DE.dic > %buildroot%_datadir/myspell/de_DE.dic
iconv -fISO8859-1 -tUTF-8 de_AT.dic > %buildroot%_datadir/myspell/de_AT.dic
iconv -fISO8859-1 -tUTF-8 de_CH.aff > %buildroot%_datadir/myspell/de_CH.aff
iconv -fISO8859-1 -tUTF-8 de_CH.dic > %buildroot%_datadir/myspell/de_CH.dic
subst 's|^SET ISO8859-1|SET UTF-8|' %buildroot%_datadir/myspell/de_??.aff

cd %buildroot%_datadir/myspell
de_DE_aliases="de_BE de_LU"
for lang in $de_DE_aliases; do
	ln -s de_DE.aff $lang.aff
	ln -s de_DE.dic $lang.dic
done
de_CH_aliases="de_LI"
for lang in $de_CH_aliases; do
	ln -s de_CH.aff $lang.aff
	ln -s de_CH.dic $lang.dic
done

%files
%doc README_de_??.txt
%_datadir/myspell/*

%changelog
* Tue Jan 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 20051111-alt3
- converted to UTF-8

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20051111-alt2
- new varient alias

* Wed Jul 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 20051111-alt1
- initial release
