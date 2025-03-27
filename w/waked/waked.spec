Name: waked
Version: 0.1.1
Release: alt3

Summary: Waked Daemon
Group: System/Servers
License: GPL-2.0-or-later
Url: https://gitlab.com/seath1/waked.git

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: waked-0.1.1-alt-sdbus-cpp-2.0.patch

# https://aur.archlinux.org/cgit/aur.git/tree/0002-Include-typedef-for-uint64_t-fixes-compilation.patch?h=waked-git
Patch10: 0002-Include-typedef-for-uint64_t-fixes-compilation.patch
# https://aur.archlinux.org/cgit/aur.git/tree/0003-use-relative-times-for-broken-RTCs.patch?h=waked-git
Patch11: 0003-use-relative-times-for-broken-RTCs.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ pkgconfig(sdbus-c++) >= 2.0.0

%description
Waked is a daemon which lets Apps wake the system from suspend at requested times.

%prep
%setup
%patch0 -p1
%patch10 -p1
%patch11 -p1
%patch1 -p1 -b .sdbus-cpp-2.0

%build
cd src
%cmake
%cmake_build

%install
install -pD -m0755 src/%_target_platform/%name %buildroot%_bindir/%name
install -pD -m0644 de.seath.Waked.conf %buildroot%_datadir/dbus-1/system.d/de.seath.Waked.conf
install -pD -m0644 %name.service %buildroot%systemd_unitdir/%name.service

%files
%_bindir/%name
%systemd_unitdir/%name.service
%_datadir/dbus-1/system.d/de.seath.Waked.conf

%changelog
* Thu Mar 27 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt3
- fixed for sdbus-cpp-2.0 (ALT #53137)

* Tue Nov 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt2
- applied aur/alpine patches to fix build with gcc-14 and
  to fix using RTC on some devices
- built against sdbus-cpp-1.6

* Fri Oct 20 2023 Valery Inozemtsev <shrek@altlinux.ru> 0.1.1-alt1
- initial release

