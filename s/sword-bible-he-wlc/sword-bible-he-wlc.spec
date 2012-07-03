Name: sword-bible-he-wlc
Version: 1.2
Release: alt1

Summary: Westminster Leningrad Codex for SWORD
Summary(ru_RU.UTF-8): Westminster Leningrad Codex для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.6

%description
This text began as an electronic transcription by Whitaker and Parunak
of the 1983 printed edition of Biblia Hebraica Stuttgartensia (BHS).
The transcription is called the Michigan-Claremont electronic text and
was archived at the Oxford Text Archive (OTA) in 1987. Since that
time, the text has been modified to conform to the photo-facsimile of
the Leningrad Codex, Firkovich B19A, residing at the Russian National
Library, St. Petersberg; hence the change of name. This version
contains all 6 of the textual elements of the OTA document:
consonants, vowels, cantillation marks, "paragraph" (pe, samekh)
markers, and ketib-qere variants. Morphological divisions have been
added.
The BHS so-called "paragraph" markers (pe and samekh) do not actually
occur in the Leningrad Codex. The editors of BHS use them to indicate
open space deliberately left blank by the scribe. Pe ("open"
paragraph) represents a space between verses, where the new verse
begins on a new column line. This represents a major section of the
text. Samekh ("closed" paragraph) represents a space of less than a
line between verses. This is understood to be a subdivision of the
corresponding "open" section. Since these markers represent an actual
physical feature of the text, they have been retained.
The WLC source is maintained by the Westminster Hebrew Institute,
Philadelphia, PA (http://whi.wts.edu/WHI).
The Sword module is maintained by Martin Gruner (mg dot pub at gmx dot
net). Please identify this as the source of derived works.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
This text began as an electronic transcription by Whitaker and Parunak
of the 1983 printed edition of Biblia Hebraica Stuttgartensia (BHS).
The transcription is called the Michigan-Claremont electronic text and
was archived at the Oxford Text Archive (OTA) in 1987. Since that
time, the text has been modified to conform to the photo-facsimile of
the Leningrad Codex, Firkovich B19A, residing at the Russian National
Library, St. Petersberg; hence the change of name. This version
contains all 6 of the textual elements of the OTA document:
consonants, vowels, cantillation marks, "paragraph" (pe, samekh)
markers, and ketib-qere variants. Morphological divisions have been
added.
The BHS so-called "paragraph" markers (pe and samekh) do not actually
occur in the Leningrad Codex. The editors of BHS use them to indicate
open space deliberately left blank by the scribe. Pe ("open"
paragraph) represents a space between verses, where the new verse
begins on a new column line. This represents a major section of the
text. Samekh ("closed" paragraph) represents a space of less than a
line between verses. This is understood to be a subdivision of the
corresponding "open" section. Since these markers represent an actual
physical feature of the text, they have been retained.
The WLC source is maintained by the Westminster Hebrew Institute,
Philadelphia, PA (http://whi.wts.edu/WHI).
The Sword module is maintained by Martin Gruner (mg dot pub at gmx dot
net). Please identify this as the source of derived works.

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
* Thu Jun 29 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.2-alt1
- initial build for Sisyphus
