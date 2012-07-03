Name: sword-bibles-he
Version: 0.1
Release: alt1

Summary: A set of freely distributable Hebrew Bible for SWORD (virtual package)
Summary(ru_RU.UTF-8): Тексты Библии на еврейском языке для системы SWORD (виртуальный пакет)

License: GPL
Group: Education

Url: http://www.crosswire.org/sword

Requires: sword-bible-he-aleppo
Requires: sword-bible-he-wlc

BuildArch: noarch

Provides: sword-bibles-hebrew = 1.0-alt2
Obsoletes: sword-bibles-hebrew <= 1.0-alt2

%description
A set of freely distributable Hebrew Bible for SWORD.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
Набор свободно распроcтраняемых текстов Библии на еврейском языке
для системы SWORD.

Внимание! Если вы живёте в стране, где христианство преследуется,
будьте осторожны при использовании этого пакета.

%files

%changelog
* Wed Jun 28 2006 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- rename package from sword-bibles-hebrew to sword-bibles-he
- remove ERen_he module, unknown copyright status
- add WLC module
- sword-bibles-he is a virtual package now

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix bible name in russian
- fix spec (install and files sections)

* Fri Jul 30 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- first build for Sisyphus

* Fri Sep 05 2003 David Sainty <saint@arklinux.org> 1.0-1ark
- First AL pkg
