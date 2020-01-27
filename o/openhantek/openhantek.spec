Name: openhantek
Version: 3.0.1
Release: alt1
Epoch: 1

Summary: OpenHantek is a DSO software for Hantek (Voltcraft/Darkwire/Protek/Acetech) USB digital signal oscilloscopes

License: GPLv3
Group: Engineering
Url: http://openhantek.org/

# Source-url: https://github.com/OpenHantek/OpenHantek6022/archive/%version.tar.gz
Source: %name-%version.tar


# Automatically added by buildreq on Thu Dec 28 2017
# optimized out: cmake cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-opengl libqt5-printsupport libqt5-widgets libstdc++-devel lsb-release python-base python-modules python3 python3-base qt5-base-devel qt5-tools sssd-client
BuildRequires: binutils-devel cmake doxygen libGLU-devel libfftw3-devel libssl-devel libusb-devel qt5-imageformats qt5-tools-devel

Requires: xkeyboard-config

Requires: qt5-imageformats

%description
OpenHantek is a free software for Hantek and compatible (Voltcraft/Darkwire/Protek/Acetech)
USB digital signal oscilloscopes.

It has started as an alternative to the official Hantek DSO software for Linux users.

Supported devices: DSO2xxx Series, DSO52xx Series, 6022BE/BL

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
ln -s OpenHantek %buildroot%_bindir/%name

%files
%_bindir/%name
%_bindir/OpenHantek
%_udevrulesdir/60-hantek.rules

%changelog
* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.0.1-alt1
- new version (3.0.1) with rpmgs script

* Tue Oct 29 2019 Vitaly Lipatov <lav@altlinux.ru> 1:2.16-alt1
- new version 2.16 (with rpmrb script)

* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 1:2.15-alt1
- new version 2.15 (with rpmrb script)

* Mon Jul 29 2019 Vitaly Lipatov <lav@altlinux.ru> 1:2.12-alt1
- new version 2.12 (with rpmrb script)

* Fri Jun 28 2019 Vitaly Lipatov <lav@altlinux.ru> 1:2.10-alt1
- new version 2.10 (with rpmrb script)

* Thu May 30 2019 Vitaly Lipatov <lav@altlinux.ru> 1:2.09-alt1
- new version 2.09 (with rpmrb script)

* Fri May 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1:2.04-alt1
- new version 2.04 (with rpmrb script)

* Tue May 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1:2.03-alt1
- switch to tarball from OpenHantek6022 repo (ALT bug 36725)

* Thu Dec 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.12-alt1
- initial build for ALT Sisyphus
