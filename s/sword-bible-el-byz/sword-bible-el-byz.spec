Name: sword-bible-el-byz
Version: 1.9
Release: alt1

Summary: Byzantine/Majority Text (2000) for SWORD
Summary(ru_RU.UTF-8): Byzantine/Majority Text (2000) для системы SWORD

License: Public Domain
Group: Education

Url: http://www.crosswire.org/sword
Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip

Requires: sword >= 1.5.3

%description
The Greek New Testament according to the Byzantine Textform, edited by
Maurice A. Robinson and William G. Pierpont, 2000 editioni
This is the edition by Pierpont and Robinson of a Majority, or
Byzantine, text of the NT. It is similar to an earlier production of
Hodges and Farstad in being based on von Soden's apparatus, but
without their stemmatic reconstruction of the Apocalypse and the
Pericope Adulterae.

WARNING: If you live in a persecuted country and
do not wish to risk detection you should NOT use this package!

%description -l ru_RU.UTF-8
The Greek New Testament according to the Byzantine Textform, edited by
Maurice A. Robinson and William G. Pierpont, 2000 editioni
This is the edition by Pierpont and Robinson of a Majority, or
Byzantine, text of the NT. It is similar to an earlier production of
Hodges and Farstad in being based on von Soden's apparatus, but
without their stemmatic reconstruction of the Apocalypse and the
Pericope Adulterae.

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
* Thu Jun 22 2006 Artem Zolochevskiy <azol@altlinux.ru> 1.9-alt1
- initial build for Sisyphus
