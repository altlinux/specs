Name: sword-bible-el-whnu
Version: 1.9
Release: alt1

Summary: Westcott-Hort with NA27/UBS4 variants (1881) for SWORD
Summary(ru_RU.UTF-8): Westcott-Hort with NA27/UBS4 variants (1881) для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.3

%description
The Westcott-Hort edition of 1881 with complete parsing information
for all Greek words. Readings of Nestle27/UBS4 shown, also with
complete parsing information attached

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
The Westcott-Hort edition of 1881 with complete parsing information
for all Greek words. Readings of Nestle27/UBS4 shown, also with
complete parsing information attached

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
* Thu Jun 22 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.9-alt1
- initial build for Sisyphus
