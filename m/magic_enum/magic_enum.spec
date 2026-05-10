Name: magic_enum
Version: 0.9.8
Release: alt1

Summary: Magic Enum C++
License: MIT
Group: Development/C++

Url: https://github.com/Neargye/%name
Packager: Nazarov Denis <nenderus@altlinux.org> 

# https://github.com/Neargye/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: ctest
BuildRequires: gcc-c++

%description
Header-only C++17 library provides static reflection for enums, work with
anyenum type without any macro or boilerplate code.

%package -n lib%name-devel
Summary: Magic Enum C++
Group: Development/C++

%description -n lib%name-devel
Header-only C++17 library provides static reflection for enums, work with
anyenum type without any macro or boilerplate code.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n lib%name-devel
%doc LICENSE README.md
%_includedir/%name
%_datadir/cmake/%name
%_datadir/pkgconfig/%name.pc
%_datadir/%name

%changelog
* Sun May 10 2026 Nazarov Denis <nenderus@altlinux.org> 0.9.8-alt1
- New version 0.9.8.

* Fri Jul 11 2025 Nazarov Denis <nenderus@altlinux.org> 0.9.7-alt1
- Initial build for ALT Linux
