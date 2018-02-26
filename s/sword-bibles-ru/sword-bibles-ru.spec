Name: sword-bibles-ru
Version: 0.1
Release: alt1

Summary: A set of freely distributable Russian Bible for SWORD (virtual package)
Summary(ru_RU.UTF-8): Тексты Библии на русском языке для системы SWORD (виртуальный пакет)

License: GPL
Group: Education

Url: http://www.crosswire.org/sword

Requires: sword-bible-ru-rst
Requires: sword-bible-ru-rusmakarij

BuildArch: noarch

Provides: sword-bibles-russian = 1.1-alt1
Obsoletes: sword-bibles-russian <= 1.1-alt1

%description
A set of freely distributable English Bible for SWORD.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
Набор свободно распроcтраняемых текстов Библии на английском языке
для системы SWORD.

Внимание! Если вы живёте в стране, где христианство преследуется,
будьте осторожны при использовании этого пакета.

%files

%changelog
* Wed Jun 28 2006 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- rename package from sword-bibles-russian to sword-bibles-ru
- remove RusVZH module, license without permission to distribute
- sword-bibles-ru is a virtual package now

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- fix bible name in russian
- fix spec (install and files sections)
- add RusVZH module

* Fri Jul 30 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- first build for Sisyphus

* Fri Sep 05 2003 David Sainty <saint@arklinux.org> 1.0-1ark
- First AL pkg
