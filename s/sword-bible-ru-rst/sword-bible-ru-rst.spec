Name: sword-bible-ru-rst
Version: 1.6
Release: alt1

Summary: Russian Synodal Translation for SWORD
Summary(ru_RU.UTF-8): Russian Synodal Translation для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.2

%description
1876 Russian Synodal Translation
The electronic edition comes from Sergej A. Fedosov's Slavic Bible for
Windows (http://come.to/sbible)

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
1876 Russian Synodal Translation
The electronic edition comes from Sergej A. Fedosov's Slavic Bible for
Windows (http://come.to/sbible)

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
* Thu Jun 29 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.6-alt1
- initial build for Sisyphus
