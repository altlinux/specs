Name: sword-bible-en-webster
Version: 1.2
Release: alt1

Summary: Webster Bible for SWORD
Summary(ru_RU.UTF-8): Webster Bible для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.1a

%description
THE HOLY BIBLE,
CONTAINING THE OLD AND NEW TESTAMENTS,
IN THE COMMON VERSION.
WITH AMENDMENTS OF THE LANGUAGE,
BY NOAH WEBSTER, LL. D.
-------------
NEW HAVEN:
PUBLISHED BY DURRIE & PECK.
Sold by HEZEKIAH HOWE & CO., and A. H. MALTBY, New Haven;
and by N.&J. WHITE, New York.
------
1833
Webster Bible Electronic Format.
PUBLIC DOMAIN
February 1992
Beginning in July of 1991 the task of placing the Webster Bible text
in electronic format began. The original purpose was to provide Larry
Pierce, who produces the On-Line Bible program, with a more modern
*public domain* text, similar in content and style to the AV but with
a grammar that would provide better comprehension in todays English.
I plan on maintaining an accurate copy of the Webster text. Anyone
finding an error should contact me; Anyone desiring to obtain the
latest, most correct text, can find it on the Bible Foundation BBS, or
can contact me in the following methods:
Internet acus10@waccvm.corp.mot.com
Home phone 602-829-8542
Address Mark Fuller
1129 East Loyola Drive
Tempe Arizona, 85282
Bible Foundation http://www.bf.org
I would like to thank the Bible Foundation not only for scanning
nearly the entire Webster Bible but for encouraging me to undertake
this monumental work; particularly around page 20 when I realized what
I had gotten myself into. Special thanks to Jerry Kingery of the Bible
Foundation for scanning, and Jerry Hastings for doing some preliminary
scan cleaning and making the texts available on the BBS.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
THE HOLY BIBLE,
CONTAINING THE OLD AND NEW TESTAMENTS,
IN THE COMMON VERSION.
WITH AMENDMENTS OF THE LANGUAGE,
BY NOAH WEBSTER, LL. D.
-------------
NEW HAVEN:
PUBLISHED BY DURRIE & PECK.
Sold by HEZEKIAH HOWE & CO., and A. H. MALTBY, New Haven;
and by N.&J. WHITE, New York.
------
1833
Webster Bible Electronic Format.
PUBLIC DOMAIN
February 1992
Beginning in July of 1991 the task of placing the Webster Bible text
in electronic format began. The original purpose was to provide Larry
Pierce, who produces the On-Line Bible program, with a more modern
*public domain* text, similar in content and style to the AV but with
a grammar that would provide better comprehension in todays English.
I plan on maintaining an accurate copy of the Webster text. Anyone
finding an error should contact me; Anyone desiring to obtain the
latest, most correct text, can find it on the Bible Foundation BBS, or
can contact me in the following methods:
Internet acus10@waccvm.corp.mot.com
Home phone 602-829-8542
Address Mark Fuller
1129 East Loyola Drive
Tempe Arizona, 85282
Bible Foundation http://www.bf.org
I would like to thank the Bible Foundation not only for scanning
nearly the entire Webster Bible but for encouraging me to undertake
this monumental work; particularly around page 20 when I realized what
I had gotten myself into. Special thanks to Jerry Kingery of the Bible
Foundation for scanning, and Jerry Hastings for doing some preliminary
scan cleaning and making the texts available on the BBS.

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
