Name: MP707
Version: 1.1
Release: alt1

Summary: Control tool for BM1707, MP707, MP707R
Summary(ru_RU.UTF-8): Утилита управления для контроллеров BM1707, MP707, MP707R
License: GPL
Group: System/Configuration/Hardware
Url: https://silines.ru/software/RODOS/RODOS-5_6/RODOS5_6.tar.gz

Packager: Pavel Isopenko <pauli@altlinux.org>
Source: %name-%version.tar
Source1: udev.rules
BuildPreReq: gcc-c++ libstdc++-devel libusb-devel

%description
Control tool for BM1707, MP707, MP707R controllers
Based on https://www.olimp-z.ru/products/RODOS-5/RODOS5_6.tar.gz

%description -l ru_RU.UTF-8
Программа управления контроллерами семейства BM1707/MP707 (снятыми с производства) для Linux-систем.
Позволяет передавать команды, сканировать подключенные датчики температуры и получать от них данные, задавать пределы термостатирования.
Основана на программе управления для контроллеров RODOS //silines.ru/software/RODOS/RODOS-5_6/RODOS5_6.tar.gz
Для актуальных версий контроллеров предназначен пакет RODOS5_6

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

