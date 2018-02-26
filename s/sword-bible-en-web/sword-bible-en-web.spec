Name: sword-bible-en-web
Version: 1.4
Release: alt1

Summary: World English Bible for SWORD
Summary(ru_RU.UTF-8): World English Bible для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.1a

%description
The World English Bible (WEB)
Public Domain
The World English Bible is a 1997 revision of the American Standard
Version of the Holy Bible, first published in 1901. It is in the
Public Domain. Please feel free to copy and distribute it freely.
Thank you to Michael Paul Johnson for making this work available. For
the latest information, to report corrections, or for other
correspondence:
Michael Paul Johnson
http://www.ebible.org/bible
mpj@ebible.org

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
The World English Bible (WEB)
Public Domain
The World English Bible is a 1997 revision of the American Standard
Version of the Holy Bible, first published in 1901. It is in the
Public Domain. Please feel free to copy and distribute it freely.
Thank you to Michael Paul Johnson for making this work available. For
the latest information, to report corrections, or for other
correspondence:
Michael Paul Johnson
http://www.ebible.org/bible
mpj@ebible.org

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
* Thu Jun 29 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.4-alt1
- initial build for Sisyphus
