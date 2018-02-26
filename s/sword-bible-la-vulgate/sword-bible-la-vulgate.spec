Name: sword-bible-la-vulgate
Version: 1.0
Release: alt1

Summary: Latin Vulgate for SWORD
Summary(ru_RU.UTF-8): Latin Vulgate для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.1a

%description
Jerome's A.D. 405 Biblia Sacra Vulgata Latina (Latin Vulgate)

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
Jerome's A.D. 405 Biblia Sacra Vulgata Latina (Latin Vulgate)

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
* Mon Jun 19 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.0-alt1
- initial build for Sisyphus
