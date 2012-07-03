Name: sword-bible-uk-ukrainian
Version: 1.2
Release: alt2

Summary: Ukrainian Bible for SWORD
Summary(ru_RU.UTF-8): Библия на украинском языке для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.2

Provides: sword-bibles-ukrainian = 1.0-alt2
Obsoletes: sword-bibles-ukrainian <= 1.0-alt2

%description
Ivan Ogienko Ukrainian Bible, 1930
Courtesy the Unbound Bible (http://unbound.biola.edu/)

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
Ivan Ogienko Ukrainian Bible, 1930
Courtesy the Unbound Bible (http://unbound.biola.edu/)

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
* Fri Jul 14 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.2-alt2
- fix Obsoletes:

* Sun Jun 18 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.2-alt1
- rename package from sword-bibles-ukrainian to sword-bible-uk-ukrainian 
- fix package version
- add dependency on sword
- change Summary and description
- fix spec (install and files sections)

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- fix bible name in russian
- fix spec (install and files sections)

* Fri Jul 30 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- first build for Sisyphus

* Fri Sep 05 2003 David Sainty <saint@arklinux.org> 1.0-1ark
- First AL pk
