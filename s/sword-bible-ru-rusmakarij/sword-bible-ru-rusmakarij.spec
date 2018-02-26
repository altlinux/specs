Name: sword-bible-ru-rusmakarij
Version: 1.1
Release: alt1

Summary: The Pentateuch of Moses in Russian for SWORD
Summary(ru_RU.UTF-8): The Pentateuch of Moses in Russian для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.2

%description
The Pentateuch of Moses in Russian (archimandrite Makarij translation)
or 1825
The electronic edition comes from Sergej A. Fedosov's Slavic Bible for
Windows (http://come.to/sbible)

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
The Pentateuch of Moses in Russian (archimandrite Makarij translation)
or 1825
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
* Thu Jun 29 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.1-alt1
- initial build for Sisyphus
