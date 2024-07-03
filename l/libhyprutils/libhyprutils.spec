%define soversion 0

Name: libhyprutils
Version: 0.1.5
Release: alt1
License: BSD-3-Clause

Summary: Hyprland utilities library
Summary(ru_RU.UTF-8): Библиотека утилит Hyprland

Group: System/Libraries

Url: https://github.com/hyprwm/hyprutils
Vcs: https://github.com/hyprwm/hyprutils.git

Source0: %name-%version.tar

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
%_libdir/%name.so.%soversion.*

%files -n %name-devel
%_includedir/hyprutils/
%_libdir/%name.so
%_pkgconfigdir/hyprutils.pc

%changelog
* Thu Jul 04 2024 Roman Alifanov <ximper@altlinux.org> 0.1.5-alt1
- NMU: new version 0.1.5 (with rpmrb script)

* Thu Jun 13 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- Initial build
