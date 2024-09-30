%define _unpackaged_files_terminate_build 1

Name: hardinfo2
Version: 2.1.14
Release: alt2

Summary: System Information and Benchmark for Linux Systems
License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://www.hardinfo2.org
Vcs: https://github.com/hardinfo2/hardinfo2

Source: %name-%version.tar
Patch: hardinfo2-2.1.14-alt-cmake-deps-qgears.patch

# addition tools according to upstream
Requires: lm_sensors3
Requires: sysbench
Requires: udisks2
Requires: dmidecode
Requires: lsscsi
Requires: xdg-utils
Requires: iperf3
Requires: fwupd
Requires: xrandr
Requires: vulkan-tools
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: libgtk+3-devel
BuildRequires: libcairo-devel
BuildRequires: glib2-devel
BuildRequires: libsoup3.0-devel
BuildRequires: libjson-glib-devel

%description
Hardinfo2 is based on hardinfo, which has not been released >10 years.
Hardinfo2 is the reboot that was needed.

Hardinfo2 offers System Information and Benchmark for Linux Systems.
It is able to obtain information from both hardware and basic software.
It can benchmark your system and compare to other machines online.

%prep
%setup
%patch

%build
%cmake -DHARDINFO2_SERVICE=0
%cmake_build

%install
%cmake_install
%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/%{name}*
%_datadir/metainfo/org.hardinfo2.hardinfo2.metainfo.xml
%_libdir/%name

%changelog
* Mon Sep 30 2024 Vladislav Glinkin <smasher@altlinux.org> 2.1.14-alt2
- Add find_lang to spec file

* Thu Sep 26 2024 Vladislav Glinkin <smasher@altlinux.org> 2.1.14-alt1
- Initial build for ALT

