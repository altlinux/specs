Name: hunspell-pt
Summary: Portuguese hunspell dictionaries
Version: 20081113
Release: alt2
License: LGPLv2 and GPLv2+
Group: Text tools
URL: http://www.broffice.org/verortografico/baixar

Requires: hunspell

Source0: http://natura.di.uminho.pt/download/sources/Dictionaries/hunspell/hunspell-pt_PT-20081113.tar.gz
Source1: http://www.deso-se.com.br/downloads/pt_BR-2008-07-07C.zip

BuildArch: noarch
BuildRequires: unzip

%description
Portuguese hunspell dictionaries.

%prep
%setup -q -n hunspell-pt_PT-20081113
unzip -q -o %SOURCE1

%build

%install
mkdir -p %buildroot%_datadir/myspell
iconv -fISO8859-1 -tUTF-8 pt_BR.aff > %buildroot%_datadir/myspell/pt_BR.aff
iconv -fISO8859-1 -tUTF-8 pt_BR.dic > %buildroot%_datadir/myspell/pt_BR.dic
subst 's|^SET ISO8859-1|SET UTF-8|' %buildroot%_datadir/myspell/pt_BR.aff

%files
%doc README_pt_BR.TXT README_pt_PT.txt COPYING
%_datadir/myspell/*

%changelog
* Tue Jan 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 20081113-alt2
- converted to UTF-8

* Fri Dec 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081113-alt1
- initial release

