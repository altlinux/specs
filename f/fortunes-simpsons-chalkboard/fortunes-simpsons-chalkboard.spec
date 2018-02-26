# Spec file for Bart Simpon's chalkboard writings.

%define version 1.1
%define release alt1

%define real_name simpsons-chalkboard

Name: fortunes-simpsons-chalkboard
Version: %version
Release: %release

Summary: collection of Bart Simpson's chalkboard-writings
Summary(ru_RU.UTF-8): коллекция письменных упражнений Барта Симпсона на школьной доске

License: distributable
Group: Games/Other
#URL: http://www.splitbrain.org/Fortunes/simpsons/
URL: http://en.wikipedia.org/wiki/List_of_The_Simpsons_chalkboard_gags

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

BuildArch: noarch

Source: %real_name.tar.bz2
# http://www.splitbrain.org/Fortunes/simpsons/fortune-simpsons-chalkboard.tgz

BuildPreReq: fortune-mod >= 1.0-ipl33mdk
PreReq: fortune-mod >= 1.0-ipl33mdk

%description
This is a a collection of Bart Simpson's  chalkboard-writings
from the opening credits  of episodes  of the television show 
"The Simpsons", packaged up for use with the fortune program.

%description -l ru_RU.UTF-8
Коллекция  письменных  упражнений  Барта Симпсона  на  школьной
доске из заставок к эпизодам телевизионного шоу "The Simpsons",
подготовленная для использования с программой fortune.

%prep
%setup -n %real_name
mv -- chalkboard %real_name

%build
strfile %real_name

%install
mkdir -p -- %buildroot%_gamesdatadir/fortune
%__install -p -m 644 -- %real_name %real_name.dat %buildroot%_gamesdatadir/fortune

%files
%_gamesdatadir/fortune/%{real_name}*

%changelog
* Fri May 16 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.1-alt1
- Updating to the present set of episodes
 
* Mon Sep 05 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.0-alt1
- Initial build for ALTLinux Sisyphus

* Sun Sep 04 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.0-alt0
- Initial build
