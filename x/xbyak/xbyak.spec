Name: xbyak
Version: 7.37.4
Release: alt1

Summary: A C++ JIT assembler for x86 (IA32), x64 (AMD64, x86-64)
License: BSD-3-Clause
Group: Development/C++

Url: https://github.com/herumi/%name
Vcs: https://github.com/herumi/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/herumi/%name/archive/refs/tags/v%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch0: alt-no-strict-register-size-check.patch

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
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name-devel
%_includedir/%name
%_libdir/cmake/%name

%changelog
* Sun Jun 28 2026 Nazarov Denis <nenderus@altlinux.org> 7.37.4-alt1
- New version 7.37.4.

* Sun May 31 2026 Nazarov Denis <nenderus@altlinux.org> 7.37.3-alt1
- New version 7.37.3.

* Tue May 19 2026 Nazarov Denis <nenderus@altlinux.org> 7.37.1-alt1
- New version 7.37.1.

* Wed May 13 2026 Nazarov Denis <nenderus@altlinux.org> 7.37-alt1
- New version 7.37.

* Sat Sep 06 2025 Nazarov Denis <nenderus@altlinux.org> 7.30-alt1
- New version 7.30.

* Tue Aug 26 2025 Nazarov Denis <nenderus@altlinux.org> 7.29.2-alt1
- New version 7.29.2.

* Sun Aug 17 2025 Nazarov Denis <nenderus@altlinux.org> 7.29.1-alt1
- New version 7.29.1.

* Mon Aug 04 2025 Nazarov Denis <nenderus@altlinux.org> 7.28-alt2
- Add no strict register size check patch (ALT #55476), thx zerg@

* Tue Jul 22 2025 Nazarov Denis <nenderus@altlinux.org> 7.28-alt1
- New version 7.28.

* Sat Jul 12 2025 Nazarov Denis <nenderus@altlinux.org> 7.27-alt1
- New version 7.27.

* Sun Mar 23 2025 Nazarov Denis <nenderus@altlinux.org> 7.24.2-alt1
- New version 7.24.2.

* Sun Dec 29 2024 Nazarov Denis <nenderus@altlinux.org> 7.22-alt1
- New version 7.22.

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
