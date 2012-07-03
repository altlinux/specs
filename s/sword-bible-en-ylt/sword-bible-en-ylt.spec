Name: sword-bible-en-ylt
Version: 1.0
Release: alt1

Summary: Young's Literal Translation (1898) for SWORD
Summary(ru_RU.UTF-8): Young's Literal Translation (1898) для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.1a

%description
Young's Literal Translation
of the Holy Bible
by Robert Young, 1862, 1898
(Author of the Young's Analytical Concordance)
Printed copy available from Baker Publishing
Grand Rapids, Mi. 49516

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
Young's Literal Translation
of the Holy Bible
by Robert Young, 1862, 1898
(Author of the Young's Analytical Concordance)
Printed copy available from Baker Publishing
Grand Rapids, Mi. 49516

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
* Thu Jun 29 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.0-alt1
- initial build for Sisyphus
