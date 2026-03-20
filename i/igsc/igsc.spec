%define soversion 1

Name: igsc
Version: 1.0.2
Release: alt1
Summary: Graphics System Controller Firmware Update Library
License: MIT
Group: System/Libraries
URL: https://github.com/intel/igsc

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc gcc-c++ libmetee-devel libudev-devel

ExclusiveArch: x86_64

Requires: lib%name = %EVR

%description
Intel(R) Graphics System Controller Firmware Update Library (IGSC FU)

This package contains CLI for lib%name.

%package -n lib%name%soversion
Summary: Intel(R) Graphics System Controller Firmware Update Library
Group: System/Libraries
Provides: lib%name = %EVR

%description -n lib%name%soversion
Intel(R) Graphics System Controller Firmware Update Library (IGSC FU)

%package -n lib%name-devel
Summary: lib%name devel libs and headers
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
lib%name development libraries and headers.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name

%files -n lib%name%soversion
%_libdir/lib%name.so.%{soversion}*

%files -n lib%name-devel
%_libdir/lib%name.so
%_libdir/cmake/%name
%_includedir/*.h

%changelog
* Tue Jan 27 2026 L.A. Kostis <lakostis@altlinux.ru> 1.0.2-alt1
- 1.0.2.

* Mon Jun 30 2025 L.A. Kostis <lakostis@altlinux.ru> 0.9.6-alt1
- 0.9.6.

* Fri Jan 31 2025 L.A. Kostis <lakostis@altlinux.ru> 0.9.5-alt1
- Initial build for ALTlinux.


