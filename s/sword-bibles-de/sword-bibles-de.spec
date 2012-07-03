Name: sword-bibles-de
Version: 0.1
Release: alt1

Summary: A set of freely distributable German Bible for SWORD (virtual package)
Summary(ru_RU.UTF-8): Тексты Библии на немецком языке для системы SWORD (виртуальный пакет)

License: GPL
Group: Education
URL: http://www.crosswire.org/sword

Requires: sword-bible-de-gerlut
Requires: sword-bible-de-gerlut1545
Requires: sword-bible-de-gerelb1871
Requires: sword-bible-de-gerelb1905

BuildArch: noarch

Provides: sword-texts-de = 0.1-alt1
Obsoletes: sword-texts-de <= 0.1-alt1

%description
A set of freely distributable German Bible for SWORD.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
Тексты Библии на немецком языке для системы SWORD.

Внимание! Если вы живёте в стране, где христианство преследуется,
будьте осторожны при использовании этого пакета.

%files

%changelog
* Mon Jun 19 2006 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- rename package from sword-texts-de to sword-bibles-de

* Sat May 06 2006 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
