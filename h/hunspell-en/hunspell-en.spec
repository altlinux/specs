Name: hunspell-en
Summary: English hunspell dictionaries
Version: 20060207
Release: alt3
Group: Text tools
License: LGPL
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/

Source0: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/en_US.zip
Source1: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/en_GB.zip

Requires: libhunspell

BuildArch: noarch
BuildRequires: unzip

%description
English (US, UK, etc.) hunspell dictionaries.

%prep
%setup -q -c -n %name -a1

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/myspell
iconv -fISO8859-1 -tUTF-8 en_US.aff > %buildroot%_datadir/myspell/en_US.aff
iconv -fISO8859-1 -tUTF-8 en_US.dic > %buildroot%_datadir/myspell/en_US.dic
iconv -fISO8859-1 -tUTF-8 en_GB.aff > %buildroot%_datadir/myspell/en_GB.aff
iconv -fISO8859-1 -tUTF-8 en_GB.dic > %buildroot%_datadir/myspell/en_GB.dic
subst 's|^SET ISO8859-1|SET UTF-8|' %buildroot%_datadir/myspell/en_??.aff

cd %buildroot%_datadir/myspell
en_GB_aliases="en_AU en_BS en_BZ en_CA en_GH en_IE en_IN en_JM en_NA en_NZ en_TT en_ZA en_ZW"
for lang in $en_GB_aliases; do
	ln -s en_GB.aff $lang.aff
	ln -s en_GB.dic $lang.dic
done
en_US_aliases="en_PH"
for lang in $en_US_aliases; do
	ln -s en_US.aff $lang.aff
	ln -s en_US.dic $lang.dic
done

%files
%doc README_en_??.txt
%_datadir/myspell/*

%changelog
* Tue Jan 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 20060207-alt3
- converted to UTF-8

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20060207-alt2
- new varient alias

* Wed Jul 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 20060207-alt1
- initial release
