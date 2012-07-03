Name: sklad-chkcfg
Version: 0.5.6
Release: alt1

Summary: Collects and records data in a format compatible with CheckCfg
License: GPLv2
Group: System/Kernel and hardware
BuildArch: noarch

Url: http://checkcfg.narod.ru/
Source0: %name-%version.tar.bz2
Source1: %name.sysconfig.conf
Source2: %name.init.conf
Source3: README.ALT

Packager: Timur Batyrshin <erthad@altlinux.org>

Requires: coreutils dmidecode findutils gawk grep hd2u mount net-tools pciutils procps rpm sed smartmontools usbutils

%description
This script collects data about computer config to use it in CheckCfg program.

%prep
%setup -q

%install
cp -ar %SOURCE3 .
mv README.RUS README.RUS.koi8r
iconv -f koi8r -t utf8 README.RUS.koi8r > README.RUS
install -pD -m755 chkcfg.sh %buildroot%_sbindir/%name
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name
install -pD -m755 %SOURCE2 %buildroot%_initdir/%name
mkdir -p %buildroot%_spooldir/%name

%files
%_sbindir/*
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc BUGS ChangeLog CONTRIBUTORS COPYING LICENSE README.RUS README.ALT
%dir %_spooldir/%name

%changelog
* Wed Apr 08 2009 Timur Batyrshin <erthad@altlinux.org> 0.5.6-alt1
- initial build
