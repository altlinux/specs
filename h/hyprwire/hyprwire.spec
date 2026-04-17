%define soversion 3

Name: hyprwire
Version: 0.3.0
Release: alt1
License: BSD-3-Clause

Summary: A fast and consistent wire protocol for IPC

Group: System/Libraries

Url: https://github.com/hyprwm/hyprwire
Vcs: https://github.com/hyprwm/hyprwire.git

ExcludeArch: %ix86
Source: %name-%version.tar

Patch1: clang.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprutils)

BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(pugixml)

%description
%summary.

%package -n lib%name%soversion
Summary: A fast and consistent wire protocol for IPC
Group: System/Libraries

%description -n lib%name%soversion
%summary.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name%soversion = %EVR

%description -n lib%name-devel
This package provides development files for %name library.

%prep
%setup
%autopatch -p1

%build
%cmake -DCMAKE_CXX_COMPILER=clang++
%cmake_build 

%install
%cmake_install

cat %buildroot%_pkgconfigdir/%name-scanner.pc
subst "s|Version:|Version: %version|" \
    %buildroot%_pkgconfigdir/%name-scanner.pc

%files -n lib%name%soversion
%_libdir/lib%name.so.%soversion
%_libdir/lib%name.so.%version

%files -n lib%name-devel
%_bindir/%name-scanner
%_includedir/%name/
%_libdir/lib%name.so
%_libdir/cmake/%name-scanner/
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-scanner.pc

%changelog
* Sat Feb 07 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Fri Dec 05 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.1-alt1
- new version 0.2.1 (with rpmrb script)

* Wed Oct 29 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.1-alt1
- Initial build
