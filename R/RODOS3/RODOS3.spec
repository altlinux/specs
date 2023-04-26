Name: RODOS3

Version: 1.3
Release: alt2

Summary: Control tool for RODOS-3 controllers
Summary(ru_RU.UTF-8): Инструмент управления для контроллеров RODOS-3
License: GPL-3.0
Group: System/Configuration/Hardware
Url: https://silines.ru/rodos-3

Packager: Pavel Isopenko <pauli@altlinux.org>
Source: %name-%version.tar
Source1: udev.rules
BuildPreReq: gcc-c++ libstdc++-devel libusb-devel

%description
Control tool for RODOS-3 controllers

%description -l ru_RU.UTF-8
Программа контроля и управления устройствами семейства RODOS для Linux-систем.
Программа позволяет читать состояние, включать и отключать исполнительные устройства.
Реализована на С++ и работает из командной строки.

RODOS-3 - USB-реле. Блок является улучшенной версией MP709 и позволит радиолюбителю получить коммутатор силовых нагрузок,
подключаемый к персональному компьютеру через USB-порт. Устройство будет полезно для применения в быту, дома, на даче.
С его помощью можно включать свет, водопроводные клапаны и другие нагрузки.

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
* Wed Apr 26 2023 Pavel Isopenko <pauli@altlinux.org> 1.3-alt2
- change Url

* Tue Apr 25 2023 Pavel Isopenko <pauli@altlinux.org> 1.3-alt1
- vew version 1.03
- change license

* Mon Jan 07 2019 Pavel isopenko <pauli@altlinux.org> 1.1-alt1
- initial build for Sisyphus


