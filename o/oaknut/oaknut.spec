Name: oaknut
Version: 2.0.2
Release: alt1

Summary: A C++20 assembler for AArch64 (ARMv8.0 to ARMv8.3)
License: MIT
Group: System/Libraries

Url: https://github.com/merryhime/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/merryhime/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: catch-devel
BuildRequires: gcc-c++

%description
Oaknut is a header-only library that allows one to dynamically assemble code in-memory at runtime.

%package -n lib%name-devel
Summary:A C++20 assembler for AArch64 (ARMv8.0 to ARMv8.3)
Group: Development/C++

%description -n lib%name-devel
Oaknut is a header-only library that allows one to dynamically assemble code in-memory at runtime.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name-devel
%doc LICENSE README.md
%_cmakedir/%name
%_includedir/%name

%changelog
* Sat Mar 09 2024 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt1
- Initial build for ALT Linux
