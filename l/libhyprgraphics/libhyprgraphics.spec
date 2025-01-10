%define soversion 0

Name: libhyprgraphics
Version: 0.1.1
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
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libjxl_cms)
BuildRequires: pkgconfig(libjxl_threads)
BuildRequires: pkgconfig(libmagic)

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
* Mon Dec 23 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.1-alt1
- Initial build
