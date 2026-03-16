Name: uni-algo
Version: 1.2.0
Release: alt1

Summary: Unicode Algorithms Implementation for C/C++

License: MIT
Group: System/Libraries
Url: https://github.com/uni-algo/uni-algo

# Source-url: https://github.com/uni-algo/uni-algo/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.12
BuildRequires: gcc-c++

%description
uni-algo is a Unicode Library for C/C++ that implements the latest
Unicode standard. It provides Unicode case mapping, normalization,
segmentation, collation, and code point properties.

%package -n lib%name
Summary: Unicode Algorithms shared library
Group: System/Libraries

%description -n lib%name
Shared library for uni-algo Unicode Algorithms Implementation.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Header files and CMake configuration for developing with %name.

%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files -n lib%name
%doc README.md LICENSE.md
%_libdir/libuni-algo.so.*

%files -n lib%name-devel
%_libdir/libuni-algo.so
%_includedir/uni_algo/
%_datadir/uni-algo/

%changelog
* Mon Mar 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Sisyphus

