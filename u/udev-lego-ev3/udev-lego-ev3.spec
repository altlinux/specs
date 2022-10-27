Name: udev-lego-ev3
Version: 0.1
Release: alt2

Summary(ru_RU.UTF-8): Правило udev для Lego EV3
Summary: Udev rule for Lego EV3

License: GPLv3
Group: System/Configuration/Hardware
Url: http://os.mos.ru
BuildArch: noarch
Source: %name-%version.tar

%description
%summary.

%description -l ru_RU.UTF-8
Правило udev для для использования Lego EV3. Можно работать через Trik Studio

%prep
%setup

%install
install -Dpm0644 99-ev3-usb-hid.rules %buildroot%_udevrulesdir/99-ev3-usb-hid.rules

%files
%_udevrulesdir/99-ev3-usb-hid.rules

%changelog
* Thu Oct 27 2022 Artem Proskurnev <tema@altlinux.org> 0.1-alt2
- Fix mode, add group and correct category

* Thu Oct 27 2022 Artem Proskurnev <tema@altlinux.org> 0.1-alt1
- init

