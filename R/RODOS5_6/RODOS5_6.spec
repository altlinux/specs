Name: RODOS5_6
Version: 1.4
Release: alt1

Summary: Control tool for RODOS-5, 6, 6B controllers
Summary(ru_RU.UTF-8): Инструмент управления для контроллеров RODOS-5, 6, 6B
License: GPL-3.0
Group: System/Configuration/Hardware
Url: https://silines.ru/software/RODOS/RODOS-5_6/RODOS5_6.tar.gz

Packager: Pavel Isopenko <pauli@altlinux.org>
Source: %name-%version.tar
Source1: udev.rules
BuildPreReq: gcc-c++ libstdc++-devel libusb-devel

%description
Control tool for RODOS-5,6,6B controllers

%description -l ru_RU.UTF-8
Программа контроля и управления устройствами семейства RODOS для Linux-систем.
Позволяет передавать команды, сканировать подключенные датчики температуры и получать от них данные, задавать пределы термостатирования.
Реализована на С++ и работает из командной строки.

%prep
%setup
%make_build

%install
install -d -m0755 %buildroot%_bindir
install -m0755 %name %buildroot%_bindir
install -D -m0644 %_sourcedir/udev.rules %buildroot%_udevrulesdir/40-%name.rules


%files
%_udevrulesdir/*
%attr(4711, root, root) %_bindir/%name

%changelog
* Fri Apr 21 2023 Pavel Isopenko <pauli@altlinux.org> 1.4-alt1
- new version 1.04
- change license

* Sun Mar 03 2019 Pavel isopenko <pauli@altlinux.org> 1.1-alt2
- change Group
- change Url

* Sun Jan 06 2019 Pavel isopenko <pauli@altlinux.org> 1.1-alt1
- initial build for Sisyphus

