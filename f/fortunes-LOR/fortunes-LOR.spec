# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define snapshot 20110508
%define quotes 653

Name: fortunes-LOR
Version: %snapshot
Release: alt1

Summary: Quotes from linux.org.ru site visitors
Summary(ru_RU.UTF-8): Цитаты посетителей сайта linux.org.ru

License: distributable
Group: Games/Other
Url: http://linux.org.ru
Packager: Slava Semushin <php-coder@altlinux.ru>

BuildArch: noarch

Source: %name.bz2

BuildRequires: fortune-mod >= 1.0-ipl33mdk
PreReq: fortune-mod >= 1.0-ipl33mdk

%description
This package contains various quotes from a famous russian resource
devoted to OS Linux - linux.org.ru, also known as LOR. Total number of
quotes: %quotes.

%description -l ru_RU.UTF-8
В этом пакете содержатся различные высказывания, взятые с известного
русскоязычного сайта об ОС Linux -- linux.org.ru, который также иногда
называют ЛОР. Всего цитат в базе: %quotes.

%install
mkdir -p %buildroot%_gamesdatadir/fortune
bzcat %SOURCE0 > %buildroot%_gamesdatadir/fortune/LOR
strfile %buildroot%_gamesdatadir/fortune/LOR %buildroot%_gamesdatadir/fortune/LOR.dat

%files
%_gamesdatadir/fortune/LOR*

%changelog
* Sun May 08 2011 Slava Semushin <php-coder@altlinux.ru> 20110508-alt1
- Added new quotes (62)
- Converted Summary and %%description to UTF-8
- I not maintain this package anymore

* Sat Oct 06 2007 Slava Semushin <php-coder@altlinux.ru> 20071006-alt1
- Added new quotes (10)
- Imported into git and built with gear
- Enable _unpackaged_files_terminate_build

* Tue May 01 2007 Slava Semushin <php-coder@altlinux.ru> 20070501-alt1
- Added new quotes (49)
- Change my name in Packager tag
- Formatted and correct %%description

* Sat Jun 17 2006 php-coder <php-coder@altlinux.ru> 20060617-alt1
- Added new quotes (29)

* Fri Mar 03 2006 php-coder <php-coder@altlinux.ru> 20060303-alt1
- Added new quotes (27)
- More strict name in %%files section
- Dont use macros for bzip2 and mkdir -p commands
- Removed Summary and %%description in koi8-r and utf8 charsets

* Wed Nov 23 2005 php-coder <php-coder@altlinux.ru> 20051123-alt1
- Added new quotes (120)
- Added quotes from http://lorquotes.servak.biz/fortunes.php (29)
- Generate dat-file on the build-time
- Removed one not interesting quote
- Added Packager, Url and BuildRequires tags

* Wed May 11 2005 php-coder <php-coder@altlinux.ru> 20050511-alt1
- First build for Sisyphus
  (thnx gns@ and algor@ for helps and quotes)

