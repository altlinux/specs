Name: zswap
Summary: Init and set up zswap
Summary(ru_RU.UTF-8): Служба для инициализации настройки zswap
Url: https://github.com/Smoque/zswap

Version: 0.52
Release: alt1
License: GPLv2
Group: System/Configuration/Hardware
Patch:  zswap-0.52-systemd.patch

BuildArch: noarch

# Author Author: Vadim A. Illarionov
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar

%description
zswap init and set up.

%description -l ru_RU.UTF8
Включение/выключение/статистика zswap.

%prep
%setup
%patch -p1
%__subst s\\'$version'\\"%version"\\ %name.service

%install
install  -Dm 755 %name         %buildroot%_sbindir/%name
install  -Dm 755 %name.init    %buildroot%_initdir/%name
install -pDm 644 %name.service %buildroot%_unitdir/%name.service
install -pDm 644 %name.syscfg  %buildroot%_sysconfdir/sysconfig/%name
install -pDm 644 ru_RU.UTF-8   %buildroot%_datadir/%name/ru_RU.UTF-8
install -pDm 644 -t            %buildroot%_docdir/%name-%version/ README.*

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc README.ru_RU.UTF-8 README.md
%_datadir/%name/ru_RU.UTF-8
%_unitdir/%name.service
%_initdir/%name
%_sbindir/%name

%changelog
* Thu Aug 24 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.52-alt1
- Version 0.52

* Tue Aug 15 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.51-alt1
- Version 0.51

* Fri Aug 11 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.50-alt1
- Version 0.5

* Wed Jul 26 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.20-alt1
- Added Russian localization

* Fri Jul 21 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.11-alt1
- initial build to Sisyphus

* Thu Jul 20 2023 Vadim A. Illarionov <gbIMoBou_@_ya.ru> 0.10-alt1
- initial build
