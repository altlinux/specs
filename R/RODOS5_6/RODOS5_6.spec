Name: RODOS5_6
Version: 1.1
Release: alt1

Summary: Control tool for RODOS-5, 6, 6B controllers
Summary(ru_RU.UTF-8): Инструмент управления для контроллеров RODOS-5, 6, 6B
License: GPL
Group: System/Kernel and hardware
Url: https://www.olimp-z.ru/products/RODOS-5/RODOS5_6.tar.gz

Packager: Pavel Isopenko <pauli@altlinux.org>
Source: %name-%version.tar
Source1: udev.rules
BuildPreReq: gcc-c++ libstdc++-devel libusb-devel

%description
Control tool for RODOS-5,6,6B controllers

%description -l ru_RU.UTF-8
Программа контроля и управления устройствами семйества RODOS для Linux-систем.
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
* Sun Jan 06 2019 Pavel isopenko <pauli@altlinux.org> 1.1-alt1
- initial build for Sisyphus

