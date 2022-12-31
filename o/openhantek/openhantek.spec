Name: openhantek
Version: 3.3.1
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
BuildRequires: cmake doxygen libGLU-devel libfftw3-devel libssl-devel libusb-devel qt5-imageformats qt5-tools-devel

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
mv %buildroot/usr/lib %buildroot/lib
ln -s OpenHantek %buildroot%_bindir/%name

%files
%_bindir/%name
%_bindir/OpenHantek
%_udevrulesdir/60-openhantek.rules
%_desktopdir/OpenHantek.desktop
%_docdir/openhantek/
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1:3.3.1-alt1
- new version 3.3.1 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 1:3.3.0.1-alt1
- new version 3.3.0.1 (with rpmrb script)

* Mon Jan 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1:3.2.5-alt1
- new version 3.2.5 (with rpmrb script)

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 1:3.2.4-alt2
- drop BR: binutils-devel

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1:3.2.4-alt1
- new version 3.2.4 (with rpmrb script)

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 1:3.2.3-alt1
- new version 3.2.3 (with rpmrb script)

* Sun Apr 18 2021 Vitaly Lipatov <lav@altlinux.ru> 1:3.2.1-alt1
- new version 3.2.1 (with rpmrb script)

* Mon Mar 29 2021 Vitaly Lipatov <lav@altlinux.ru> 1:3.2-alt1
- new version 3.2 (with rpmrb script)

* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1:3.1.5-alt1
- new version 3.1.5 (with rpmrb script)

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.1.3-alt1
- new version 3.1.3 (with rpmrb script)

* Wed Aug 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.1.2-alt1
- new version 3.1.2 (with rpmrb script)

* Sun Aug 02 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Mon May 11 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

* Wed May 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.0.4b-alt1
- new version 3.0.4b (with rpmrb script)

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.0.3-alt1
- new version 3.0.3 (with rpmrb script)

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
