Name: sword-bible-de-gerelb1905
Version: 1.4
Release: alt1

Summary: German Darby Unrevidierte Elberfelder (1905) for SWORD
Summary(ru_RU.UTF-8): German Darby Unrevidierte Elberfelder (1905) для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.6

Provides: sword-text-gerelb1905 = 1.4-alt1
Obsoletes: sword-text-gerelb1905 < 1.4-alt1

%description
German Darby Unrevidierte Elberfelder 1905,
Copyright by R. Bockhaus Verlag, Germany

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
German Darby Unrevidierte Elberfelder 1905,
Copyright by R. Bockhaus Verlag, Germany

Внимание! Если вы живёте в стране, где христианство преследуется,
будьте осторожны при использовании этого пакета.

%prep
%setup -q

%install
mkdir -p %buildroot%_datadir/sword
unzip *.zip -d %buildroot%_datadir/sword

%files
%_datadir/sword/

%changelog
* Mon Jun 19 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.4-alt1
- rename package from sword-text-gerelb1905 to sword-bible-de-gerelb1905
- add dependency on sword

* Sat May 06 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.4-alt1
- initial build for Sisyphus
