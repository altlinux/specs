Name: hunspell-uk
Summary: Ukrainian hunspell dictionaries
Version: 20051106
Release: alt2
Group: Text tools
License: LGPL
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/

Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/uk_UA.zip

Requires: libhunspell

BuildArch: noarch
BuildRequires: unzip

%description
Ukrainian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-uk

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/myspell
iconv -fCP1251 -tUTF-8 uk_UA.aff > %buildroot%_datadir/myspell/uk_UA.aff
iconv -fCP1251 -tUTF-8 uk_UA.dic > %buildroot%_datadir/myspell/uk_UA.dic
subst 's|^SET microsoft-cp1251|SET UTF-8|' %buildroot%_datadir/myspell/uk_UA.aff

%files
%doc README_uk_UA.txt
%_datadir/myspell/*

%changelog
* Tue Jan 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 20051106-alt2
- converted to UTF-8

* Wed Jul 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 20051106-alt1
- initial release
