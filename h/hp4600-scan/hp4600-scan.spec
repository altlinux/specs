Name: hp4600-scan
Version: 0.1
Release: alt3

Summary: Scanning utility for HP Scanjet 4600 and 4670 scanners
Summary(ru_RU.UTF-8): Утилитка для оцифровки сканерами HP Scanjet 4600 и 4670
License: GPL
Group: Graphics
Url: http://www.chmil.org/hp4600linux/
Packager: Malo Skryleve <malo@altlinux.org>

Source: %name-%version.tar.bz2
Source1: 74-hp4600-scan.rules

Requires: perl
BuildRequires: libusb-compat-devel

%description
Scanning utilities for HP Scanjet 46xx series scanners. They support
4600 and 4670 models. For now, only a fullpage scan with 600 dpi as
a resolution is available.

%description -l ru_RU.UTF-8
Утилитки для оцифровки сканерами серии HP Scanjet 46xx. Поддерживаются
модели 4600 и 4670. На данное время доступно сканирование только полной
страницы с разрешением 600 тнд (dpi).

%prep
%setup

%build
./make

%install
mkdir -p %buildroot/usr/bin
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/udev/rules.d/74-hp4600-scan.rules
install -p hp4600scanfullfile %buildroot/usr/bin
install -p fixhp4600output %buildroot/usr/bin
install -p hp4600onestep %buildroot/usr/bin
install -p hp4600simplescan %buildroot/usr/bin

%files
%_bindir/*
%_sysconfdir/udev/rules.d/*

%changelog
* Tue Apr 05 2011 Malo Skryleve <malo@altlinux.org> 0.1-alt3
- Fixed spec file

* Thu Mar 31 2011 Malo Skryleve <malo@altlinux.org> 0.1-alt2
- Added udev rules file to the %%files section

* Wed Feb 16 2011 Malo Skryleve <malo@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus

