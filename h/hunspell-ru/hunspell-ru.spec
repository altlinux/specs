Name: hunspell-ru
Summary: Russian hunspell dictionaries
Version: 20110128
Release: alt1
Group: Text tools
License: BSD
URL: http://hg.mozilla.org/l10n-central/ru/file/7125484f3dce/extensions/spellcheck/hunspell

Source: ru_RU.zip

Requires: libhunspell
Obsoletes: hunspell-ru-io < %version

BuildArch: noarch
BuildRequires: unzip

%description
Russian hunspell dictionaries

%prep
%setup -q -c -n hunspell-ru

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/myspell
iconv -fKOI8-R -tUTF-8 ru.aff > %buildroot%_datadir/myspell/ru_RU.aff
iconv -fKOI8-R -tUTF-8 ru.dic > %buildroot%_datadir/myspell/ru_RU.dic
subst 's|^SET KOI8-R|SET UTF-8|' %buildroot%_datadir/myspell/ru_RU.aff

%files
%_datadir/myspell/*

%changelog
* Fri Jan 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 20110128-alt1
- 2011-01-28 snapshot
- obsoletes hunspell-ru-io

* Wed Feb 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 20040406-alt6
- grouped alternative (closes: #23026)

* Tue Jan 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 20040406-alt5
- converted to UTF-8

* Mon Jul 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 20040406-alt4
- rebuild

* Tue Nov 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 20040406-alt3
- not support Cyrillic_io. Cyrillic_io support %name-io package

* Tue Jul 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 20040406-alt2
- support Cyrillic_io

* Wed Jul 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 20040406-alt1
- initial release
