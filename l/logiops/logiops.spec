%define _unpackaged_files_terminate_build 1

Name: logiops
Version: 0.3.4
Release: alt1

Summary: An unofficial userspace driver for HID++ Logitech devices
License: GPL-3.0
Group: System/Configuration/Hardware
URL: https://github.com/PixlOne/logiops

Source0: %name-%version.tar
Source1: %name-%version-src-ipcgull.tar

BuildRequires: cmake gcc-c++ gcc systemd-devel
BuildRequires: libevdev-devel libconfig-devel
BuildRequires: libconfig-c++-devel libudev-devel
BuildRequires: libgio-devel libdbus-devel
BuildRequires: libpcre2-devel libstdc++-devel
BuildRequires: zlib-devel libmount-devel
BuildRequires: glib2-devel libffi-devel
BuildRequires: libblkid-devel libselinux-devel

%description
This is an unofficial driver for Logitech mice and keyboard.

%prep
%setup -a1
%ifarch %e2k
# LCC can't decide between "unsigned int" and "const char *"
sed -i "s/remove((int)/remove((unsigned)/" src/logid/config/types.h
%endif

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
mkdir %buildroot%_sysconfdir
mv logid.example.cfg logid.cfg
cp -r logid.cfg %buildroot%_sysconfdir/

%post
%post_service logid.service

%preun
%preun_service logid.service

%files
%doc README.md LICENSE
%_bindir/logid
%_unitdir/logid.service
%config(noreplace) %_sysconfdir/logid.cfg
%_datadir/dbus-1/system.d/pizza.pixl.LogiOps.conf

%changelog
* Tue Jun 04 2024 Obidin Oleg <nofex@altlinux.org> 0.3.4-alt1
- 0.3.2 -> 0.3.4

* Fri May 26 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.3.2-alt1.1
- Fixed build for Elbrus

* Wed Mar 30 2023 Obidin Oleg <nofex@altlinux.org> 0.3.2-alt1
- First build for ALT
