Name: xbyak
Version: 7.07.1
Release: alt1

Summary: A C++ JIT assembler for x86 (IA32), x64 (AMD64, x86-64)
License: BSD-3-Clause
Group: Development/C++

Url: https://github.com/herumi/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/herumi/%name/archive/refs/tags/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++

%description
Xbyak is a C++ header library that enables dynamically to assemble x86(IA32), x64(AMD64, x86-64) mnemonic.

%package -n lib%name-devel
Summary: A C++ JIT assembler for x86 (IA32), x64 (AMD64, x86-64)
Group: Development/C++

%description -n lib%name-devel
Xbyak is a C++ header library that enables dynamically to assemble x86(IA32), x64(AMD64, x86-64) mnemonic.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name-devel
%_includedir/%name
%_libdir/cmake/%name

%changelog
* Wed Sep 04 2024 Nazarov Denis <nenderus@altlinux.org> 7.07.1-alt1
- New version 7.07.1.

* Tue Feb 13 2024 Nazarov Denis <nenderus@altlinux.org> 7.05.1-alt1
- New version 7.05.1.

* Fri Jan 05 2024 Nazarov Denis <nenderus@altlinux.org> 7.05-alt1
- New version 7.05.

* Wed Sep 06 2023 Nazarov Denis <nenderus@altlinux.org> 6.73-alt1
- New version 6.73.

* Sat Jul 29 2023 Nazarov Denis <nenderus@altlinux.org> 6.71-alt1
- New version 6.71.

* Tue Jul 25 2023 Nazarov Denis <nenderus@altlinux.org> 6.70-alt1
- New version 6.70.

* Sun May 28 2023 Nazarov Denis <nenderus@altlinux.org> 6.69.1-alt1
- Initial build for ALT Linux
