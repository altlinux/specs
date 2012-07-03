Name: sword-bible-en-kjv
Version: 2.2
Release: alt1

Summary: King James Version (1769) with Strongs Numbers and Morphology  for SWORD
Summary(ru_RU.UTF-8): King James Version (1769) with Strongs Numbers and Morphology  для системы SWORD

License: General public license for distribution for any purpose
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.6

%description
This is the King James Version of the Holy Bible (also known as the
Authorized Version) with embedded Strong's Numbers. The rights to the
base text are held by the C
rown of England. The Strong's numbers in the OT were obtained from The
Bible Foundation: http://www.bf.org. The NT Strong's data was obtained
from The KJV2003 Projec
t at CrossWire: http://www.crosswire.org. These mechanisms provide a
useful means for looking up the exact original language word in a
lexicon that is keyed to Stron
g's numbers.
Special thanks to the volunteers at Bible Foundation for keying the
Hebrew/English data and of Project KJV2003 for working toward the
completion of synchronizing the English phrases to the Stephanas
Textus Receptus, and to Dr. Maurice Robinson for providing the base
Greek text with Strong's and Morphology. We are also appreciative of
formatting markup that was provided by Michael Paul Johnson at
http://www.ebible.org. Their time and generosity to contribute such
for the free use of the Body of Christ is a great blessing and this
derivitive work could not have been possible without these efforts of
so many individuals. It is in this spirit that we in turn offer the
KJV2003 Project text freely for any purpose. Any copyright that might
be obtained for this effort is held by CrossWire Bible Society (c)
2003 and CrossWire Bible Society hereby grants a general public
license to use this text for any purpose.
Inquiries and comments may be directed to:
CrossWire Bible Society
kjv2003@crosswire.org
http://www.crosswire.org


WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
This is the King James Version of the Holy Bible (also known as the
Authorized Version) with embedded Strong's Numbers. The rights to the
base text are held by the C
rown of England. The Strong's numbers in the OT were obtained from The
Bible Foundation: http://www.bf.org. The NT Strong's data was obtained
from The KJV2003 Projec
t at CrossWire: http://www.crosswire.org. These mechanisms provide a
useful means for looking up the exact original language word in a
lexicon that is keyed to Stron
g's numbers.
Special thanks to the volunteers at Bible Foundation for keying the
Hebrew/English data and of Project KJV2003 for working toward the
completion of synchronizing the English phrases to the Stephanas
Textus Receptus, and to Dr. Maurice Robinson for providing the base
Greek text with Strong's and Morphology. We are also appreciative of
formatting markup that was provided by Michael Paul Johnson at
http://www.ebible.org. Their time and generosity to contribute such
for the free use of the Body of Christ is a great blessing and this
derivitive work could not have been possible without these efforts of
so many individuals. It is in this spirit that we in turn offer the
KJV2003 Project text freely for any purpose. Any copyright that might
be obtained for this effort is held by CrossWire Bible Society (c)
2003 and CrossWire Bible Society hereby grants a general public
license to use this text for any purpose.
Inquiries and comments may be directed to:
CrossWire Bible Society
kjv2003@crosswire.org
http://www.crosswire.org

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
* Thu Jun 29 2006 Artem Zolochevskiy <azol@altlinux.ru> 2.2-alt1
- initial build for Sisyphus
