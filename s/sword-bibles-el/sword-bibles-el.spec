Name: sword-bibles-el
Version: 0.1
Release: alt2

Summary: A set of freely distributable Greek Bible for SWORD (virtual package)
Summary(ru_RU.UTF-8): Тексты Библии на греческом языке для системы SWORD (виртуальный пакет)

License: GPL
Group: Education

Url: http://www.crosswire.org/sword

Requires: sword-bible-el-byz
Requires: sword-bible-el-tr
Requires: sword-bible-el-tisch
Requires: sword-bible-el-whnu
Requires: sword-bible-el-ignt
Requires: sword-bible-el-lxx

BuildArch: noarch

Provides: sword-bibles-greek = 1.1-alt1
Obsoletes: sword-bibles-greek <= 1.1-alt1

%description
A set of freely distributable Greek Bible for SWORD.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
Набор свободно распроcтраняемых текстов Библии на греческом языке
для системы SWORD.

Внимание! Если вы живёте в стране, где христианство преследуется,
будьте осторожны при использовании этого пакета.

%files

%changelog
* Fri Jul 14 2006 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- fix typo in Requires: sword-bible-el-tisch

* Wed Jun 28 2006 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- rename package from sword-bibles-greek to sword-bibles-el
- remove UMGreek module, unknown copyright status
- remove ERen_grc module, unknown copyright status
- add LXX module
- sword-bibles-el is a virtual package now

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- fix bible name in russian
- fix spec (install and files sections)
- add UMGreek module

* Fri Jul 30 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- first build for Sisyphus

* Fri Sep 05 2003 David Sainty <saint@arklinux.org> 1.0-1ark
- First AL pkg
