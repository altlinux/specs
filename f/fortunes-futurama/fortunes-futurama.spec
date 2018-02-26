# Spec file for Futurama citates

%define version 0.2
%define release alt1

%define real_name futurama

Name: fortunes-futurama
Version: %version
Release: %release

Summary: collection of quotes from "Futurama" 
Summary(ru_RU.UTF-8): коллекция цитат из "Futurama"

License: distributable
Group: Games/Other
URL: http://www.netmeister.org/misc.html

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: http://www.netmeister.org/apps/fortune-mod-futurama-0.2.tar.bz2

BuildPreReq: fortune-mod >= 1.0-ipl33mdk
PreReq: fortune-mod >= 1.0-ipl33mdk

%description
Fortune file with a compilation of quotes from the TV-Series 
"Futurama" by Matt Groeining.

%description -l ru_RU.UTF-8
Файл для fortune  с коллекцией  цитат из сериала Matt Groeining'а
"Futurama".

%prep
%setup -q -n fortune-mod-futurama-%version

%build
rm -f -- futurama.dat
strfile futurama

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune
%__install -m 0644 futurama* %buildroot%_gamesdatadir/fortune/

%files
%_gamesdatadir/fortune/%{real_name}*

%changelog
* Sat Apr 22 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.2-alt1
- Initial build for ALTLinux Sisyphus


