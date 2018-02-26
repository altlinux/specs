Name: sword-bible-de-gerlut
Version: 1.1
Release: alt1

Summary: German Luther Bibel (1912) for SWORD
Summary(ru_RU.UTF-8): German Luther Bibel (1912) для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.1a

Provides: sword-text-gerlut = 1.1-alt1
Obsoletes: sword-text-gerlut < 1.1-alt1

%description
1912 Lutherbibel

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
1912 Lutherbibel

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
* Mon Jun 19 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.1-alt1
- rename package from sword-text-gerlut to sword-bible-de-gerlut
- add dependency on sword

* Sat May 06 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.1-alt1
- initial build for Sisyphus
