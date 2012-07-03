Name: sword-bible-el-tisch
Version: 1.3
Release: alt1

Summary: Tischendorf's Eighth Edition GNT for SWORD
Summary(ru_RU.UTF-8): Tischendorf's Eighth Edition GNT для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.2

%description
The Greek Text corresponds to the printed text found in:
Tischendorf, Constantinus, Novum Testamentum Graece, editio octava
critica major Vol. I, 1869; Vol. II 1872, Leipzig:Giesecke and
Devrient. Vol 3, Prolegomena, ed. by Caspar Rene' Gregory, Leipzig:
Hinrichs, 1894.
The text contains no accents or diacritical marks. This text was
prepared from the Westcott-Hort-Nestle Aland text found in the Greek
text prepared by Dr. Maurice Robinson. Available FTP:
ftp://:@archimedes.nosc.mil:21/pub/gnt/ File whn26.zip. The text was
compared to the printed edition of Tischendorf's. Changes were made in
the text to make it correspond to the printed edition. The text was
proofed against the Tischendorf text.
The present plan is to scan in, key in corrections and proof the
complete critical apparatus of Tischendorf's. The apparatus will then
be in text format available to any one who would like to use it for
research or incorporate it into a Bible software program. I have been
informed that this is not an easy task. I am very aware of the
complexity of the text and the pitfalls of such a colossal
undertaking. The apparatus will be released as each book is completed.
According to J. Harold Greenlee "His 'eighth major edition' (1869-72)
contains a critical apparatus which has never been equaled in
comprehensiveness of citation of Greek mss., versions, and patristic
evidence. A century later it is still indispensable for serious work
in the text of the N.T."
The Greek and Hebrew words are being tagged using the scheme found in
the Online Bible program. The transliteration scheme will allow it to
be read by the Online Bible program.
The Greek text is released as a public domain text.
If any errors are found in this text please let me know as soon as
possible.
Clint Yale
1014 West Smith Road #26
Bellingham, WA 98226
360-384-1015
ccr3yale@telcomplus.com

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
The Greek Text corresponds to the printed text found in:
Tischendorf, Constantinus, Novum Testamentum Graece, editio octava
critica major Vol. I, 1869; Vol. II 1872, Leipzig:Giesecke and
Devrient. Vol 3, Prolegomena, ed. by Caspar Rene' Gregory, Leipzig:
Hinrichs, 1894.
The text contains no accents or diacritical marks. This text was
prepared from the Westcott-Hort-Nestle Aland text found in the Greek
text prepared by Dr. Maurice Robinson. Available FTP:
ftp://:@archimedes.nosc.mil:21/pub/gnt/ File whn26.zip. The text was
compared to the printed edition of Tischendorf's. Changes were made in
the text to make it correspond to the printed edition. The text was
proofed against the Tischendorf text.
The present plan is to scan in, key in corrections and proof the
complete critical apparatus of Tischendorf's. The apparatus will then
be in text format available to any one who would like to use it for
research or incorporate it into a Bible software program. I have been
informed that this is not an easy task. I am very aware of the
complexity of the text and the pitfalls of such a colossal
undertaking. The apparatus will be released as each book is completed.
According to J. Harold Greenlee "His 'eighth major edition' (1869-72)
contains a critical apparatus which has never been equaled in
comprehensiveness of citation of Greek mss., versions, and patristic
evidence. A century later it is still indispensable for serious work
in the text of the N.T."
The Greek and Hebrew words are being tagged using the scheme found in
the Online Bible program. The transliteration scheme will allow it to
be read by the Online Bible program.
The Greek text is released as a public domain text.
If any errors are found in this text please let me know as soon as
possible.
Clint Yale
1014 West Smith Road #26
Bellingham, WA 98226
360-384-1015
ccr3yale@telcomplus.com

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
* Thu Jun 22 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.3-alt1
- initial build for Sisyphus
