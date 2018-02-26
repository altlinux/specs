Name: unicode-data
Version: 4.0.0
Release: alt1

Summary: Unicode Character Database
Summary(ru_RU.UTF-8): База данных о символах Unicode
License: distributable
Group: Development/Other
URL: http://www.unicode.org/
BuildArch: noarch

# Archive with all files from ftp://www.unicode.org/Public/4.0-Update/,
# renamed without '-4.0.0', in subdirectory %name-%version.
# (After such renaming it is the same as ftp://www.unicode.org/Public/UNIDATA/
# without Unihan.txt, but should not change with time.)
Source0: %name-%version.tar.bz2

# http://www.unicode.org/Public/UNIDATA/Unihan.zip, repacked with tar/bzip2
# Note: This file contains restrictive distribution conditions; however,
# UCD.html in the main distribution explicitly overrides them.
Source1: Unihan.tar.bz2

Requires: %name-minimal = %version-%release


%package minimal
Summary: Unicode Character Database -- main data file only
Summary(ru_RU.UTF-8): База данных о символах Unicode -- только основной файл
Group: Development/Other


%package unihan
Summary: Unicode Character Database -- Unihan.txt
Summary(ru_RU.UTF-8): База данных о символах Unicode -- Unihan.txt
Group: Development/Other
Requires: %name = %version-%release


# convert version x.y.z to xyyzz (priority for update-alternatives)
%define numeric_version %(echo %version |awk -F . '{print ($1*100+$2)*100+$3}')


%description
The Unicode Character Database (UCD) is a set of files that define the
Unicode character properties and internal mappings.

This package contains all files from the Unicode Character Database,
except the Unihan database (Unihan.txt).  Unihan.txt is very large (25M)
and is contained in the separate package (%name-unihan).

%description -l ru_RU.UTF-8
База данных о символах Unicode (Unicode Character Database, UCD)
содержит файлы, определяющие свойства и правила преобразования символов
Unicode.

Этот пакет содержит все файлы UCD, кроме Unihan.txt. Файл Unihan.txt
находится в отдельном пакете (%name-unihan) из-за большого
размера (25M).

%description minimal
The Unicode Character Database (UCD) is a set of files that define the
Unicode character properties and internal mappings.

This package contains UnicodeData.txt, which is the main file of the
Unicode Character Database.  The remaining UCD files are in the
%name and %name-unihan packages.

%description minimal -l ru_RU.UTF-8
База данных о символах Unicode (Unicode Character Database, UCD)
содержит файлы, определяющие свойства и правила преобразования символов
Unicode.

Этот пакет содержит файл UnicodeData.txt - основной файл базы данных о
символах Unicode. Остальные файлы UCD находятся в пакете %name и
%name-unihan.

%description unihan
The Unicode Character Database (UCD) is a set of files that define the
Unicode character properties and internal mappings.

This package contains the Unihan database.

%description unihan -l ru_RU.UTF-8
База данных о символах Unicode (Unicode Character Database, UCD)
содержит файлы, определяющие свойства и правила преобразования символов
Unicode.

Этот пакет содержит базу данных Unihan.


%prep
%setup -q -a 1


%install
%__install -d	%buildroot%_datadir/%name/%version
%__cp -a *	%buildroot%_datadir/%name/%version

%__install -d	%buildroot%_docdir/%name-%version
%__ln_s ../../%name/%version/UCD.html \
		%buildroot%_docdir/%name-%version/UCD.html
%__ln_s ../../%name/%version/ReadMe.txt \
		%buildroot%_docdir/%name-%version/ReadMe.txt


%files
%dir %_datadir/%name
%dir %_datadir/%name/%version
%_datadir/%name/%version/*
%exclude %_datadir/%name/%version/ReadMe.txt
%exclude %_datadir/%name/%version/UCD.html
%exclude %_datadir/%name/%version/UnicodeData.*
%exclude %_datadir/%name/%version/Unihan.*

%files minimal
%dir %_datadir/%name
%dir %_datadir/%name/%version
%_datadir/%name/%version/ReadMe.txt
%_datadir/%name/%version/UCD.html
%_datadir/%name/%version/UnicodeData.*
%_docdir/%name-%version

%files unihan
%dir %_datadir/%name
%dir %_datadir/%name/%version
%_datadir/%name/%version/Unihan.*


%changelog
* Fri Jun 06 2003 Sergey Vlasov <vsu@altlinux.ru> 4.0.0-alt1
- Version 4.0.0.
- Added %%exclude instead of manual filelist generation (now the spec is
  much shorter and simpler).
- Added Unihan.txt as a new subpackage - new license in UCD.html
  explicitly overrides the copying conditions in Unihan.txt.
- Dropped alternatives support.

* Fri Jan 24 2003 Sergey Vlasov <vsu@altlinux.ru> 3.2.0-alt2
- %%install cleanup.
- Fixed update-alternatives handling.

* Thu Apr 04 2002 Servey Vlasov <vsu@altlinux.ru> 3.2.0-alt1
- Version 3.2.0

* Sat Nov 24 2001 Sergey Vlasov <vsu@altlinux.ru> 3.1.1-alt1
- First build for ALT Linux
