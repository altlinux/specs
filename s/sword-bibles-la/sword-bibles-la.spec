Name: sword-bibles-la
Version: 0.1
Release: alt1

Summary: A set of freely distributable Latin Bible for SWORD (virtual package)
Summary(ru_RU.UTF-8): Тексты Библии на латинском языке для системы SWORD (виртуальный пакет)

License: GPL
Group: Education

Url: http://www.crosswire.org/sword

Requires: sword-bible-la-vulgate
Requires: sword-bible-la-vulgate_hebps

BuildArch: noarch

Provides: sword-bibles-latin = 1.0-alt2
Obsoletes: sword-bibles-latin <= 1.0-alt2

%description
A set of freely distributable Latin Bible for SWORD.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
Набор свободно распроcтраняемых текстов Библии на латинском языке
для системы SWORD.

Внимание! Если вы живёте в стране, где христианство преследуется,
будьте осторожны при использовании этого пакета.

%files

%changelog
* Sat May 06 2006 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- rename package from sword-bibles-latin to sword-bibles-la
- split package into sword-bible-la-vulgate and sword-bible-la-vulgate_hebps
- sword-bibles-la is a virtual package now

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix spec (install and files sections)

* Mon Jan 24 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- first build for Sisyphus

* Fri Sep 05 2003 David Sainty <saint@arklinux.org> 1.0-1ark
- First AL pkg
