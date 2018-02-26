Name: sword-bible-el-tr
Version: 1.1
Release: alt1

Summary: Textus Receptus (1550/1894) for SWORD
Summary(ru_RU.UTF-8): Textus Receptus (1550/1894) для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.3

%description
The Textus Receptus with complete parsing information for all Greek
words; base text is Stephens 1550, with variants of Scrivener 1894.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
The Textus Receptus with complete parsing information for all Greek
words; base text is Stephens 1550, with variants of Scrivener 1894.

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
* Thu Jun 22 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.1-alt1
- initial build for Sisyphus
