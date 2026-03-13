%define _unpackaged_files_terminate_build 1

Name: hardinfo2
Version: 2.2.16
Release: alt1

Summary: System Information and Benchmark for Linux Systems
License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://www.hardinfo2.org
Vcs: https://github.com/hardinfo2/hardinfo2

Source: %name-%version.tar

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
BuildRequires: libgtk+3-devel
BuildRequires: libcairo-devel
BuildRequires: glib2-devel
BuildRequires: libsoup3.0-devel
BuildRequires: libjson-glib-devel
BuildRequires: glslang-devel
BuildRequires: libdecor-devel
BuildRequires: libvulkan-devel

%description
Hardinfo2 is based on hardinfo, which has not been released >10 years.
Hardinfo2 is the reboot that was needed.

Hardinfo2 offers System Information and Benchmark for Linux Systems.
It is able to obtain information from both hardware and basic software.
It can benchmark your system and compare to other machines online.

%prep
%setup

%build
%cmake -DHARDINFO2_QT5=0
%cmake_build

%install
%cmake_install
install -D %_builddir/%{name}-%{version}/tools/hardinfo2 %buildroot/%_initdir/%name
%find_lang %name

%post
%post_service %name

%preun
%preun_service %name

%files -f %name.lang
%doc README.md
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.svg
%_man1dir/%{name}*
%_datadir/metainfo/org.hardinfo2.hardinfo2.metainfo.xml
%_libdir/%name
%_unitdir/%name.service
%_initdir/%name

%changelog
* Fri Mar 13 2026 Vladislav Glinkin <smasher@altlinux.org> 2.2.16-alt1
- New version (2.2.16)
- Built without Qt5 benchmarks (Closes: #57631)

* Mon Aug 18 2025 Vladislav Glinkin <smasher@altlinux.org> 2.2.13-alt1
- 2.2.10 -> 2.2.13

* Sun May 04 2025 Vladislav Glinkin <smasher@altlinux.org> 2.2.10-alt1.gitda7f31d
- 2.2.7 -> 2.2.10
- Fixed output of operating system information for ALT (Closes: #54105)
- Built with systemd/SysV service
- Commit hash: da7f31d

* Tue Mar 11 2025 Vladislav Glinkin <smasher@altlinux.org> 2.2.7-alt1
- 2.2.4 -> 2.2.7

* Wed Nov 20 2024 Ilya Sorochan <k0tran@altlinux.org> 2.2.4-alt1
- 2.2.1 -> 2.2.4

* Wed Oct 30 2024 Vladislav Glinkin <smasher@altlinux.org> 2.2.1-alt1
- 2.1.17 -> 2.2.1

* Tue Oct 01 2024 Vladislav Glinkin <smasher@altlinux.org> 2.1.17-alt1
- Update to 2.1.17

* Mon Sep 30 2024 Vladislav Glinkin <smasher@altlinux.org> 2.1.14-alt2
- Add find_lang to spec file

* Thu Sep 26 2024 Vladislav Glinkin <smasher@altlinux.org> 2.1.14-alt1
- Initial build for ALT

