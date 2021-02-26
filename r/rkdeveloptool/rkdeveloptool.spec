Name: rkdeveloptool
Version: 1.3
Release: alt3

Summary: rkdeveloptool gives you a simple way to read/write rockusb device

Group: File tools
License: GPLv2
Url: https://github.com/rockchip-linux/rkdeveloptool

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/rockchip-linux/rkdeveloptool/archive/master.zip
Source0: %name-%version.tar
Source1: 99-rkdeveloptool.rules

BuildRequires: gcc-c++ libusb-devel

%description
rkdeveloptool gives you a simple way to read/write rockusb device.

%prep
%setup
subst "s|-Werror||" Makefile.am

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std PREFIX=%_prefix
install -D -m 644 %{SOURCE1} %buildroot%_udevrulesdir/99-rkdeveloptool.rules

%files
%doc Readme.txt
#99-rk-rockusb.rules
%_udevrulesdir/99-rkdeveloptool.rules
%_bindir/%name

%changelog
* Fri Feb 26 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt3
- drop -Werror

* Mon Apr 06 2020 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2
- NMU:
- bumped relase to override autoimports
- added 99-rkdeveloptool.rules from autoimports

* Wed Mar 25 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- initial build for ALT Sisyphus
