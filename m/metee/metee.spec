%define soversion 4

Name: metee
Version: 4.3.1
Release: alt1
Summary: ME TEE Interface Library
License: MIT
Group: System/Libraries
URL: https://github.com/intel/metee

Source: %name-%version.tar
Patch: %name-alt-fix-cflags.patch

BuildRequires(pre): cmake
BuildRequires: gcc gcc-c++

ExclusiveArch: x86_64

%description
ME TEE Library is a C library to access CSE/CSME/GSC firmware via a mei
interface.

%package -n lib%name%soversion
Summary: ME TEE Interface Library
Group: System/Libraries
Provides: lib%name = %EVR

%description -n lib%name%soversion
ME TEE Library is a C library to access CSE/CSME/GSC firmware via a mei
interface.

%package -n lib%name-devel
Summary: ME TEE Interface Library devel libs and headers
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
lib%name development libraries and headers.

%prep
%setup
%patch -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files -n lib%name%soversion
%_libdir/lib%name.so.%{soversion}*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name.h

%changelog
* Fri Jan 31 2025 L.A. Kostis <lakostis@altlinux.ru> 4.3.1-alt1
- Initial build for ALTLinux.

