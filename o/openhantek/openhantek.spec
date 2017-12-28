Name: openhantek
Version: 2017.12
Release: alt1

Summary: OpenHantek is a DSO software for Hantek (Voltcraft/Darkwire/Protek/Acetech) USB digital signal oscilloscopes

License: GPLv3
Group: Engineering
Url: http://openhantek.org/

# Source-git: https://github.com/OpenHantek/openhantek
Source: %name-%version.tar


# Automatically added by buildreq on Thu Dec 28 2017
# optimized out: cmake cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-opengl libqt5-printsupport libqt5-widgets libstdc++-devel lsb-release python-base python-modules python3 python3-base qt5-base-devel qt5-tools sssd-client
BuildRequires: binutils-devel cmake-gui doxygen libGLU-devel libfftw3-devel libssl-devel libusb-devel qt5-imageformats qt5-tools-devel

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
* Thu Dec 28 2017 Vitaly Lipatov <lav@altlinux.ru> 2017.12-alt1
- initial build for ALT Sisyphus
