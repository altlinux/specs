%define soversion 11

Name: libhyprutils
Version: 0.12.0
Release: alt1
License: BSD-3-Clause

Summary: Hyprland utilities library
Summary(ru_RU.UTF-8): Библиотека утилит Hyprland

Group: System/Libraries

Url: https://github.com/hyprwm/hyprutils
Vcs: https://github.com/hyprwm/hyprutils.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(pixman-1)

%description
Hyprland utilities library used across the ecosystem.

%description -l ru_RU.UTF-8
Библиотека утилит Hyprland, используемая во всей экосистеме.

%package -n %name%soversion
Summary: Hyprland utilities library
Group: System/Libraries

%description -n %name%soversion
%summary.

%package -n %name-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name%soversion = %EVR

%description -n %name-devel
This package provides development files for %name library.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n %name%soversion
%doc README.md
%_libdir/%name.so.%soversion
%_libdir/%name.so.%version

%files -n %name-devel
%_includedir/hyprutils/
%_libdir/%name.so
%_pkgconfigdir/hyprutils.pc

%changelog
* Wed Apr 15 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.12.0-alt1
- new version 0.12.0

* Fri Mar 20 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.11.1-alt1
- new version 0.11.1

* Sat Dec 06 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Thu Oct 16 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.10.0-alt1
- new version 0.10.0 (with rpmrb script)

* Sun Aug 31 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)

* Thu Jul 31 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Thu Jul 17 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Thu May 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script) (ALT bug 54198)

* Tue Mar 25 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Thu Jan 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Mon Jan 20 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.3.3-alt1
- new version 0.3.3 (with rpmrb script)

* Mon Dec 23 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Tue Nov 19 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.2.6-alt1
- new version 0.2.6 (with rpmrb script)

* Thu Nov 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.2.5-alt1
- new version 0.2.5 (with rpmrb script)

* Mon Sep 30 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.2.3-alt1
- new version 0.2.3 (with rpmrb script)

* Mon Sep 23 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.2.2-alt1
- new version 0.2.2 (with rpmrb script)

* Sat Aug 03 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.2.1-alt1
- new version 0.2.1 (with rpmrb script) (ALT bug 50960)

* Thu Jul 04 2024 Roman Alifanov <ximper@altlinux.org> 0.1.5-alt1
- NMU: new version 0.1.5 (with rpmrb script)

* Thu Jun 13 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- Initial build
