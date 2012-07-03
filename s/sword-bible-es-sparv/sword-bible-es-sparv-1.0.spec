Name: sword-bible-es-sparv
Version: 1.0
Release: alt1

Summary: Spanish Reina-Valera for SWORD
License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword

%description
1909 Spanish RV Bible.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%prep
%setup -q

%install
mkdir -p %buildroot%_datadir/sword
unzip *.zip -d %buildroot%_datadir/sword

%files
%_datadir/sword/

%changelog
* Tue Jun 13 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.0-alt1
- initial build for Sisyphus
