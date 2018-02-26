Name: bmcontrol
Version: 1.1
Release: alt3

License: GNU GPLv3
Group: System/Kernel and hardware
Url: https://code.google.com/p/bmcontrol/

Packager: Pavel Isopenko <pauli@altlinux.org>
Summary: Control tool for MP707x, BM1707 controllers
Summary(ru_RU.UTF-8): Инструмент управления для контроллеров MP707x, BM1707
Source: %name-%version.tar
BuildRequires: gcc-c++ libstdc++-devel libhid-devel

%description
Control tool for MP707x controllers

%description -l ru_RU.UTF-8
Программа контроля и управления управляющим устройством MP707 для Linux-систем.
Позволяет передавать основные команды, сканировать подключенные датчики температуры и получать от них данные. Программа реализована на С++ и работает из командной строки.

%prep
%setup

%build
%make_build

%install
install -d -m0755 %buildroot%_bindir
install -m0755 bmcontrol %buildroot%_bindir
install -D -m0644 bmcontrol.rules %buildroot%_udevrulesdir/40-bmcontrol.rules


%files
%_udevrulesdir/*
%attr(4711, root, root) %_bindir/bmcontrol

%changelog
* Wed Jan 10 2018 Pavel Isopenko <pauli@altlinux.org> 1.1-alt3
- add udev rule for BM1707 - MP707, RODOS-5(6) devices

* Thu Jun 04 2015 Pavel Isopenko <pauli@altlinux.org> 1.1-alt2
- change executable destination to %_bindir

* Tue Jun 02 2015 Pavel Isopenko <pauli@altlinux.org> 1.1-alt1
 -initial build for Sisyphus


