Name: sword-bible-de-gerelb1871
Version: 1.1
Release: alt1

Summary: German Elberfelder (1871) for SWORD
Summary(ru_RU.UTF-8): German Elberfelder (1871) для системы SWORD
Summary(de_DE.UTF-8): German Elberfelder (1871) für SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.3

Provides: sword-text-gerelb1871 = 1.1-alt1
Obsoletes: sword-text-gerelb1871 < 1.1-alt1

%description
Elberfelder Uebersetzung von 1871. Der Text dieses Modules wurde aus
dem OnlineBible Module extrahiert und fuer das Sword-Projekt
entsprechend aufbereitet.
Wenn Sie Fragen zu diesem Modul haben oder Probleme auftreten, wenden
Sie sich bitte an folgende Adresse:
Joachim Ansorg
junkmail_at_joachim.ansorgs.de

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
Elberfelder Uebersetzung von 1871. Der Text dieses Modules wurde aus
dem OnlineBible Module extrahiert und fuer das Sword-Projekt
entsprechend aufbereitet.
Wenn Sie Fragen zu diesem Modul haben oder Probleme auftreten, wenden
Sie sich bitte an folgende Adresse:
Joachim Ansorg
junkmail_at_joachim.ansorgs.de

Внимание! Если вы живёте в стране, где христианство преследуется,
будьте осторожны при использовании этого пакета.

%description -l de_DE.UTF-8
Elberfelder Übersetzung von 1871. Der Text dieses Modules wurde aus
dem OnlineBible Module extrahiert und für das Sword-Projekt
entsprechend aufbereitet.
Wenn Sie Fragen zu diesem Modul haben oder Probleme auftreten, wenden
Sie sich bitte an folgende Adresse:
Joachim Ansorg
junkmail_at_joachim.ansorgs.de

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
* Mon Jun 19 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.1-alt1
- rename package from sword-text-gerelb1871 to sword-bible-de-gerelb1871
- add dependency on sword

* Sat May 06 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.1-alt1
- initial build for Sisyphus
