Name: fast_float
Version: 8.2.9
Release: alt1

Summary: Fast & exact implementation of C++ from_chars for float/double
License: Apache-2.0 or MIT
Group: Development/C++

Url: https://github.com/fastfloat/%name
Vcs: https://github.com/fastfloat/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/fastfloat/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: cmake
BuildRequires: gcc-c++

%description
The %name library provides fast header-only implementations for the C++
from_chars functions for float and double types. These functions convert ASCII
strings representing decimal values (e.g., 1.3e10) into binary types. We
provide exact rounding (including round to even). In our experience, these
%name functions many times faster than comparable number-parsing functions
from existing C++ standard libraries.

%package -n lib%name-devel
Summary: Fast & exact implementation of C++ from_chars for float/double
Group: Development/C++
Requires: libgcc15-devel

%description -n lib%name-devel
The %name library provides fast header-only implementations for the C++
from_chars functions for float and double types. These functions convert ASCII
strings representing decimal values (e.g., 1.3e10) into binary types. We
provide exact rounding (including round to even). In our experience, these
%name functions many times faster than comparable number-parsing functions
from existing C++ standard libraries.

%prep
%setup
# ifarch for noarch
if [ `arch` = e2k ]; then
sed -i '/large_power_of_5\[\] =/s/\[\]/[5]/' \
	include/fast_float/bigint.h
fi

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name-devel
%_includedir/%name
%_datadir/cmake/FastFloat

%changelog
* Sat Jun 13 2026 Nazarov Denis <nenderus@altlinux.org> 8.2.9-alt1
- New version 8.2.9.

* Thu Jun 04 2026 Nazarov Denis <nenderus@altlinux.org> 8.2.6-alt1
- New version 8.2.6.

* Sun May 10 2026 Nazarov Denis <nenderus@altlinux.org> 8.2.5-alt1
- New version 8.2.5.

* Tue Apr 14 2026 Nazarov Denis <nenderus@altlinux.org> 8.2.4-alt1
- New version 8.2.4.

* Tue Feb 03 2026 Nazarov Denis <nenderus@altlinux.org> 8.2.3-alt1
- New version 8.2.3.

* Fri Jan 02 2026 Nazarov Denis <nenderus@altlinux.org> 8.2.2-alt1
- New version 8.2.2.

* Mon Dec 29 2025 Nazarov Denis <nenderus@altlinux.org> 8.2.1-alt1
- New version 8.2.1.

* Thu Sep 18 2025 Nazarov Denis <nenderus@altlinux.org> 8.1.0-alt1
- New version 8.1.0.

* Tue Mar 11 2025 Nazarov Denis <nenderus@altlinux.org> 8.0.2-alt1
- New version 8.0.2.

* Fri Feb 07 2025 Nazarov Denis <nenderus@altlinux.org> 8.0.0-alt1
- New version 8.0.0.

* Sat Jan 11 2025 Nazarov Denis <nenderus@altlinux.org> 7.0.0-alt1
- New version 7.0.0.

* Sun Sep 08 2024 Nazarov Denis <nenderus@altlinux.org> 6.1.6-alt1
- New version 6.1.6.

* Wed Sep 04 2024 Nazarov Denis <nenderus@altlinux.org> 6.1.5-alt1
- New version 6.1.5.

* Sat Aug 31 2024 Nazarov Denis <nenderus@altlinux.org> 6.1.4-alt1
- New version 6.1.4.

* Fri Mar 29 2024 Nazarov Denis <nenderus@altlinux.org> 6.1.1-alt1
- New version 6.1.1.

* Tue Feb 20 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 6.1.0-alt2
- Fixed build for Elbrus.

* Mon Jan 29 2024 Nazarov Denis <nenderus@altlinux.org> 6.1.0-alt1
- New version 6.1.0.

* Fri Dec 15 2023 Nazarov Denis <nenderus@altlinux.org> 6.0.0-alt1
- New version 6.0.0.

* Tue Nov 14 2023 Nazarov Denis <nenderus@altlinux.org> 5.3.0-alt1
- New version 5.3.0.

* Sun Jun 11 2023 Nazarov Denis <nenderus@altlinux.org> 5.2.0-alt1
- New version 5.2.0.

* Fri Jun 09 2023 Nazarov Denis <nenderus@altlinux.org> 5.1.0-alt1
- New version 5.1.0.

* Sat Dec 17 2022 Nazarov Denis <nenderus@altlinux.org> 3.8.1-alt1
- Initial build for ALT Linux
