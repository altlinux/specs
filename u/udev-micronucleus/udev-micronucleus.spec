Name: udev-micronucleus
Version: 1.0
Release: alt1

License: GNU GPLv3
Group: System/Kernel and hardware
Url: https://digistump.com/wiki/digispark/tutorials/linuxtroubleshooting

Packager: Pavel Isopenko <pauli@altlinux.org>
Summary: UDEV Rules for Micronucleus boards
Summary(ru_RU.UTF-8): Правила udev для устройств с загрузчиком micronucleus
Source: %name-%version.tar
BuildArch: noarch

%description
UDEV Rules for Micronucleus boards including the Digispark and Littlewire

%description -l ru_RU.UTF-8
Правила udev для плат с Micronucleus, включая Digispark и Littlewire.
Разрешают доступ к устройствам от имени обычного пользователя.
%prep
%setup

#%build

%install
install -D -m0644 micronucleus.rules %buildroot%_udevrulesdir/49-micronucleus.rules

%files
%_udevrulesdir/*

%changelog
* Sun Oct 21 2018 Pavel isopenko <pauli@altlinux.org> 1.0-alt1
- initial build for Sisyphus



