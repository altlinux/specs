Name: sword-bible-he-aleppo
Version: 1.0
Release: alt1

Summary: Aleppo Codex for SWORD
Summary(ru_RU.UTF-8): Aleppo Codex для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.2

%description
The Aleppo Codex without Vowel Points or Punctuation
Based on the electronic edition at http://www.mechon-mamre.org

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
The Aleppo Codex without Vowel Points or Punctuation
Based on the electronic edition at http://www.mechon-mamre.org

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
* Thu Jun 29 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.0-alt1
- initial build for Sisyphus
