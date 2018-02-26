Name: sword-bible-el-ignt
Version: 1.4
Release: alt1

Summary: Interlinear Greek New Testament for SWORD
Summary(ru_RU.UTF-8): Interlinear Greek New Testament для системы SWORD

License: Copyrighted; Free distribution
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.1a

%description
With Acknowledgements to Online Bible with which this public domain
version is supplied. The description given in OLB is as
follows:Interlinear Greek New Testament
Prepared from 1894 Scrivener Textus Receptus
I always wanted a very literal translation to study from that was
closely tied to the Greek and Strong's numbers. This summer I had the
text prepared for this project, and now you have the results. Enjoy.
The footnotes contain the word-for-word english text.
Prepared by Larry Pierce & Maurice A. Robinson, Ph.D.
Copyright (c) 1997, Winterbourne, Ont.
Please make copies for your friends.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
With Acknowledgements to Online Bible with which this public domain
version is supplied. The description given in OLB is as
follows:Interlinear Greek New Testament
Prepared from 1894 Scrivener Textus Receptus
I always wanted a very literal translation to study from that was
closely tied to the Greek and Strong's numbers. This summer I had the
text prepared for this project, and now you have the results. Enjoy.
The footnotes contain the word-for-word english text.
Prepared by Larry Pierce & Maurice A. Robinson, Ph.D.
Copyright (c) 1997, Winterbourne, Ont.
Please make copies for your friends.

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
* Wed Jun 28 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.4-alt1
- initial build for Sisyphus
