%define _unpackaged_files_terminate_build 1

%def_disable check

Name: hyprcursor
Version: 0.1.9
Release: alt1

Summary: Hyprland configuration library
License: BSD-3-Clause and MIT
Group: System/X11
Url: https://github.com/hyprwm/hyprcursor

Source: https://github.com/hyprwm/%name/archive/refs/tags/v%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(hyprlang) >= 0.4.2
BuildRequires: libtomlplusplus-devel
BuildRequires: pkgconfig(libzip)
BuildRequires: librsvg-devel >= 2.0
%{?_enable_check:BuildRequires: ctest}

%description
The hyprland cursor format, library and utilities.

%package -n lib%name
Summary: Hyprlang shared library
Group: System/Libraries

%description -n lib%name
This packaage provides Hyprlang shared library.

%package -n lib%name-devel
Summary: Development files for Hyprlang
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
This packaage provides Hyprlang shared library.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files
%_bindir/%name-util

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Wed Jun 12 2024 Roman Alifanov <ximper@altlinux.org> 0.1.9-alt1
- new version 0.1.9 (with rpmrb script)

* Fri May 24 2024 Roman Alifanov <ximper@altlinux.org> 0.1.8-alt1
- new version 0.1.8 (with rpmrb script)

* Mon Mar 25 2024 Roman Alifanov <ximper@altlinux.org> 0.1.5-alt1
- new version 0.1.5 (with rpmrb script)

* Thu Mar 21 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 0.1.4-alt1
- Initial build for ALT Linux
