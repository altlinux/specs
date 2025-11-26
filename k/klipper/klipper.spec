%define _unpackaged_files_terminate_build 1

Name:    klipper
Version: 0.13.0
Release: alt1
Summary: Klipper host software SBC for 3D printer
License: GPL-3.0-or-later
Group:   System/Base
URL:     https://www.klipper3d.org
VCS:     https://github.com/Klipper3d/klipper
Source:  %name-%version.tar
Source2: klipper.sysusers
Patch:   %name-%version-%release.patch
BuildRequires: rpm-build-python3
BuildRequires: python3-module-cffi

AutoProv: nopython3

%package mcu
Summary: Klipper host software SBC for 3D printer
Group: System/Base
Requires: %name = %version-%release
Requires: python3-modules-curses
Requires: arm-none-eabi-gcc
Requires: avr-gcc

BuildArch: noarch

%description
The Klipper firmware controls 3d-Printers. It combines the power of a general
purpose computer with one or more micro-controllers.

%description mcu
Klipper assembly toolkit for your 3D printer's microcontrollers.

%pre
%sysusers_create_package %name %SOURCE2

%prep
%setup
%autopatch -p1
%add_python3_path %_libexecdir/klipper

%build
pushd klippy/chelper
python3 -u __init__.py
popd

%install
install -D -m 0644 %SOURCE2 %buildroot%_sysusersdir/klipper.conf
install -D -m 0644 klipper.service %buildroot/%_unitdir/klipper.service
install -D -m 0644 klipper.socket %buildroot/%_unitdir/klipper.socket
install -D -m 0755 Makefile %buildroot/%_usrsrc/klipper/Makefile
mkdir -p %buildroot/%_sysconfdir/klipper/
mkdir -p %buildroot/%_logdir/klipper/
mkdir -p %buildroot/%_libexecdir/klipper
cp -r klippy %buildroot/%_libexecdir/klipper/klippy
cp -r config %buildroot/%_libexecdir/klipper/config
cp -r scripts %buildroot/%_libexecdir/klipper/scripts
cp -r lib %buildroot/%_usrsrc/klipper/lib
cp -r src %buildroot/%_usrsrc/klipper/src
ln -s %_libexecdir/klipper/klippy %buildroot/%_usrsrc/klipper/klippy
ln -s %_libexecdir/klipper/scripts %buildroot/%_usrsrc/klipper/scripts
ln -s %_defaultdocdir/%name-%version/docs %buildroot/%_libexecdir/klipper/docs
echo %version > %buildroot/%_libexecdir/klipper/klippy/.version

%files
%attr(755,klipper,klipper) %dir %_sysconfdir/klipper
%_unitdir/klipper.service
%_unitdir/klipper.socket
%_sysusersdir/klipper.conf
%attr(755,klipper,klipper) %dir %_libexecdir/klipper
%_libexecdir/klipper/config
%_libexecdir/klipper/klippy
%_libexecdir/klipper/scripts
%attr(755,klipper,klipper) %dir %_logdir/klipper
%exclude %_libexecdir/klipper/scripts/avrsim.py
%_libexecdir/klipper/docs
%doc docs
%doc COPYING README.md

%files mcu
%dir %_usrsrc/klipper
%_usrsrc/klipper/lib
%_usrsrc/klipper/src
%_usrsrc/klipper/Makefile
%_usrsrc/klipper/klippy
%_usrsrc/klipper/scripts
%doc lib/README

%changelog
* Tue Oct 21 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.13.0-alt1
- Initial build.
