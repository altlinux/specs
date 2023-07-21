Name: zswap
Summary: Init and set up zswap
Summary(ru_RU.UTF-8): Служба для инициализации настройки zswap

Version: 0.11
Release: alt1
License: GPLv2
Group: System/Configuration/Hardware

BuildArch: noarch

# Author Author: Vadim A. Illarionov
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar

%description
Init and set up zswap.

%description -l ru_RU.UTF8
Включение/выключение/статистика zswap.

%prep
%setup

%install
install  -Dm 755 %name %buildroot%_bindir/%name
install  -Dm 755 %name.init %buildroot%_initdir/%name
install -pDm 644 %name.service %buildroot%_unitdir/%name.service
install -pDm 644  -t %buildroot%_docdir/%name-%version/ {README.md,README.ru_RU.UTF-8} 

%files
%doc README.md README.ru_RU.UTF-8
%_bindir/%name
%_initdir/%name
%_unitdir/%name.service

%changelog
* Fri Jul 21 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.11-alt1
- initial build to Sisyphus

* Thu Jul 20 2023 Vadim A. Illarionov <gbIMoBou_@_ya.ru> 0.10-alt1
- initial build

