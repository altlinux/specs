%define pname openastromenace
Name: openastromenace-devel
Version: 1.2.0
Release: alt1
Summary: Script desin guide for Astro Menace game (%pname package)
Summary(ru_RU.KOI8-R): Руководство по созданию сценариев к игре Astro Menace (пакет %pname)

Group: Games/Arcade
License: GPL
Url: http://www.viewizard.com/
Source0: http://www.viewizard.com/astromenace/script_en.doc
Source1: http://www.viewizard.com/astromenace/script_ru.doc
Source2: http://www.viewizard.com/astromenace/script_en.pdf
Source3: http://www.viewizard.com/astromenace/script_ru.pdf
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

%description
Script desin guide for Astro Menace game (%pname package)
 
%description -l ru_RU.KOI8-R
Руководство по созданию сценариев к игре Astro Menace (пакет %pname)

%prep
#setup -cq

%install
mkdir -p %buildroot%_defaultdocdir/%pname-%version
cp %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 %buildroot%_defaultdocdir/%pname-%version

%files
%_defaultdocdir/%pname-%version/*

%changelog
* Thu Oct 25 2007 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Initial build for ALT

