Name: fast_float
Version: 3.8.1
Release: alt1

Summary: Fast & exact implementation of C++ from_chars for float/double
License: Apache-2.0 or MIT
Group: Development/C++

Url: https://github.com/fastfloat/%name
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

%description -n lib%name-devel
The %name library provides fast header-only implementations for the C++
from_chars functions for float and double types. These functions convert ASCII
strings representing decimal values (e.g., 1.3e10) into binary types. We
provide exact rounding (including round to even). In our experience, these
%name functions many times faster than comparable number-parsing functions
from existing C++ standard libraries.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name-devel
%_includedir/%name
%_datadir/cmake/FastFloat

%changelog
* Sat Dec 17 2022 Nazarov Denis <nenderus@altlinux.org> 3.8.1-alt1
- Initial build for ALT Linux
