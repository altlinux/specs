%define soversion 4

Name: libhyprgraphics
Version: 0.5.1
Release: alt1
License: BSD-3-Clause

Summary: Hyprland graphics / resource utilities library
Summary(ru_RU.UTF-8): Графические и ресурсные утилиты Hyprland

Group: System/Libraries

Url: https://github.com/hyprwm/hyprgraphics
Vcs: https://github.com/hyprwm/hyprgraphics.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake

BuildRequires: pkgconfig(hyprutils)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libjxl_cms)
BuildRequires: pkgconfig(libjxl_threads)
BuildRequires: pkgconfig(libmagic)
BuildRequires: pkgconfig(libdrm)

BuildRequires: libglvnd-devel

%description
A small C++ library with graphics / resource related
utilities used across the hypr* ecosystem.

%description -l ru_RU.UTF-8
Небольшая библиотека C++ с утилитами, связанными с графикой
и ресурсами, используемыми в экосистеме hypr*.

%package -n %name%soversion
Summary: Hyprland graphics / resource utilities library
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
%_includedir/hyprgraphics/
%_libdir/%name.so
%_pkgconfigdir/hyprgraphics.pc

%changelog
* Wed Apr 15 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.5.1-alt1
- new version 0.5.1

* Sun Jan 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Fri Dec 05 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.4.0-alt1
- new version 0.4.0 (with rpmrb script)

* Sat Nov 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Thu Oct 16 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- new version 0.2.0 (with rpmrb script)

* Tue Sep 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.6-alt1
- new version 0.1.6 (with rpmrb script)

* Thu Jul 17 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.5-alt1
- new version 0.1.5 (with rpmrb script)

* Thu May 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.3-alt1
- new version 0.1.3 (with rpmrb script)

* Fri Feb 07 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- new version 0.1.2 (with rpmrb script)

* Mon Dec 23 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.1-alt1
- Initial build
