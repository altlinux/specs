%define _unpackaged_files_terminate_build 1

Name: woeusb
Version: 5.2.4
Release: alt1
Summary: Windows USB installation media creator
Summary(ru_RU.UTF-8): Утилита для создания установочного USB накопителя с Windows
Group: Archiving/Cd burning
License: GPLv3+
Url: https://github.com/WoeUSB/WoeUSB

Source0: %name-%version.tar

Requires: bash4
Requires: dosfstools
Requires: gawk
Requires: grep
Requires: grub
Requires: ntfs-3g
Requires: parted
Requires: wget

ExclusiveArch: %ix86 x86_64

%description
A utility that enables you to create your own bootable Windows installation
USB storage device from an existing Windows Installation disc or disk image.

Attention! For using WoeUSB with graphical interfase, please, install woeusb-ng package.

%description -l ru_RU.UTF-8
Утилита, которая поможет создать загрузочный носитель с ОС Windows из образа
или реального диска.

Внимание! Для использования WoeUSB с графическим интерфейсом, пожалуйста,
установите пакет woeusb-ng.

%prep
%setup -n %name-%version

%build

find ./* -type f -exec sed -i "s/@@WOEUSB_VERSION@@/%{version}/g" {} \+

for shell in ./sbin/woeusb
do
  sed -i '1s|!/usr/bin/env bash|!/bin/bash|' $shell
done

%install
install -d -m 777 %buildroot%_bindir
install -m 755 sbin/woeusb %buildroot%_bindir/woeusb
mkdir -p -m 777 %buildroot%_man1dir
install -m 444 ./share/man/man1/woeusb.1 %buildroot%_man1dir/woeusb.1

%files
%doc LICENSES/GPL-3.0-or-later.txt
%_bindir/woeusb
%_man1dir/woeusb.1.xz

%changelog
* Wed Dec 10 2022 Artyom Bystrov <arbars@altlinux.org> 5.2.4-alt1
- Update to new version (ALT#43791)

* Sun Sep 26 2021 Artyom Bystrov <arbars@altlinux.org> 5.1.2-alt1
- Update to new version after rework of project

* Mon Aug 26 2019 Artyom Bystrov <arbars@altlinux.org> 3.3.0-alt1
- initial build for ALT Sisyphus from Open Mandriva
