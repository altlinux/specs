Name: sword-bible-de-gerlut1545
Version: 1.2
Release: alt1

Summary: German Unrevidierte Luther Uebersetzung von 1545 for SWORD
Summary(ru_RU.UTF-8): German Unrevidierte Luther Uebersetzung von 1545 для системы SWORD
Summary(de_DE.UTF-8): German Unrevidierte Luther Übersetzung von 1545  SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.3

Provides: sword-text-gerlut1545 = 1.2-alt1
Obsoletes: sword-text-gerlut1545 < 1.2-alt1

%description
1545 Luther Bibeluebersetzung
License: Public Domain -- copy freely
Made available in electronic format by Michael Bolsinger
<Michael.Bolsinger@t-online.de> at http://www.luther-bibel-1545.de
(see here for the most recent versions in text and HTML format).
It was converted to SWORD format by Matthias and Joachim Ansorg
<jansorg_at_crosswire.org>
Please report any errors to the following address:
Joachim and Matthias Ansorg
Poststrasse 2
D-56479 Salzburg/WW
Phone +49 (2667) 1480
e-mail joachim_at_ansorgs.de

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
1545 Luther Bibeluebersetzung
License: Public Domain -- copy freely
Made available in electronic format by Michael Bolsinger
<Michael.Bolsinger@t-online.de> at http://www.luther-bibel-1545.de
(see here for the most recent versions in text and HTML format).
It was converted to SWORD format by Matthias and Joachim Ansorg
<jansorg_at_crosswire.org>
Please report any errors to the following address:
Joachim and Matthias Ansorg
Poststrasse 2
D-56479 Salzburg/WW
Phone +49 (2667) 1480
e-mail joachim_at_ansorgs.de

Внимание! Если вы живёте в стране, где христианство преследуется,
будьте осторожны при использовании этого пакета.

%description -l de_DE.UTF-8
1545 Luther Bibelübersetzung
License: Public Domain -- copy freely
Made available in electronic format by Michael Bolsinger
<Michael.Bolsinger@t-online.de> at http://www.luther-bibel-1545.de
(see here for the most recent versions in text and HTML format).
It was converted to SWORD format by Matthias and Joachim Ansorg
<jansorg_at_crosswire.org>
Please report any errors to the following address:
Joachim and Matthias Ansorg
Poststraße 2
D-56479 Salzburg/WW
Phone +49 (2667) 1480
e-mail joachim_at_ansorgs.de

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
* Mon Jun 19 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.2-alt1
- rename package from sword-text-gerlut1545 to sword-bible-de-gerlut1545
- add dependency on sword

* Sat May 06 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.2-alt1
- initial build for Sisyphus
