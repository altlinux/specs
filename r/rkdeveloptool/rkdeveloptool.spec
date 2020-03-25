Name: rkdeveloptool
Version: 1.3
Release: alt1

Summary: rkdeveloptool gives you a simple way to read/write rockusb device

Group: File tools
License: GPLv2
Url: https://github.com/rockchip-linux/rkdeveloptool

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/rockchip-linux/rkdeveloptool/archive/master.zip
Source: %name-%version.tar

BuildRequires: gcc-c++ libusb-devel

%description
rkdeveloptool gives you a simple way to read/write rockusb device.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc Readme.txt
#99-rk-rockusb.rules
%_bindir/%name

%changelog
* Wed Mar 25 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- initial build for ALT Sisyphus
