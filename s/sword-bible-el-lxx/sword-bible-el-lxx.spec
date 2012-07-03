Name: sword-bible-el-lxx
Version: 2.0
Release: alt1

Summary: Septuagint, Morphologically Tagged Rahlfs' for SWORD
Summary(ru_RU.UTF-8): Septuagint, Morphologically Tagged Rahlfs' для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.2

%description
The Analytic Septuagint was prepared by Steve Amato of the
Boston Christian Bible Study Resources
http://www.bcbsr.com
Morphology was included from the LXXM (see below)
The The Analytic Septuagint is not to be used,
either directly or indirectly, for commercial purposes
without prior written consent of Steve Amato
and the legal authors and developers of the morphology
of the LXXM identified below.
The LXXM = The morphologically analyzed text of CATSS LXX
prepared by CATSS under the direction of R. Kraft (Philadelphia team)
The CATSS LXX = The computer form prepared by the TLG
(Thesaurus  Linguae Graecae) Project directed by T. Brunner
at the University of California, Irvine, with further verification
and adaptation (in process) by CATSS towards conformity with
the individual Gttingen editions that have appeared since 1935.
The LXX = Septuaginta, ed. A. Rahlfs
(Stuttgart: Wrttembergische Bibelanstalt, 1935; repr. in 9th ed.,
1971).
Greek Septuagint Version 270 BC

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
The Analytic Septuagint was prepared by Steve Amato of the
Boston Christian Bible Study Resources
http://www.bcbsr.com
Morphology was included from the LXXM (see below)
The The Analytic Septuagint is not to be used,
either directly or indirectly, for commercial purposes
without prior written consent of Steve Amato
and the legal authors and developers of the morphology
of the LXXM identified below.
The LXXM = The morphologically analyzed text of CATSS LXX
prepared by CATSS under the direction of R. Kraft (Philadelphia team)
The CATSS LXX = The computer form prepared by the TLG
(Thesaurus  Linguae Graecae) Project directed by T. Brunner
at the University of California, Irvine, with further verification
and adaptation (in process) by CATSS towards conformity with
the individual Gttingen editions that have appeared since 1935.
The LXX = Septuaginta, ed. A. Rahlfs
(Stuttgart: Wrttembergische Bibelanstalt, 1935; repr. in 9th ed.,
1971).
Greek Septuagint Version 270 BC

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
* Thu Jun 22 2006 Artem Zolochevskiy <azol@altlinux.ru> 2.0-alt1
- initial build for Sisyphus
