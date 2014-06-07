%define origname yaml-cpp
%define soversion 0

Name: lib%origname%soversion
Version: 0.5.1
Release: alt2

Summary: A YAML parser and emitter for C++
License: MIT
Group: Development/Other

Url: https://code.google.com/p/yaml-cpp/
Packager: Andrew Clark <andyc@altlinux.org>
Source: %origname-%version.tar.gz

# Automatically added by buildreq on Thu May 29 2014 (-ba)
# optimized out: cmake-modules elfutils libcloog-isl4 libstdc++-devel pkg-config python-base
BuildRequires: boost-devel-headers cmake gcc-c++

Provides: %name = %version-%release

%description
A YAML parser and emitter for C++

%package -n lib%origname-devel
Summary: YAML Development libraries
Group: Development/Other
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release

%description -n lib%origname-devel
Development libraries for YAML.
This package contains static development files for YAML.

%prep
%setup -n %origname-%version

%build
cmake --debug-output -D CMAKE_INSTALL_PREFIX="/usr" -D CMAKE_CXX_FLAGS="%optflags" -D CMAKE_C_FLAGS="%optflags" -D LIB_INSTALL_DIR="%_libdir" -DBUILD_SHARED_LIBS=ON CMakeLists.txt

%install
%make
mkdir -p %buildroot{%_libdir/pkgconfig,%_includedir}
mv include/* %buildroot%_includedir
install -pm 644 lib%origname.so* %buildroot%_libdir
install -pm 644 %origname.pc %buildroot%_libdir/pkgconfig

%files
%doc license.txt install.txt
%_libdir/*.so.*

%files -n lib%origname-devel
%_includedir/%origname/*
%_libdir/pkgconfig/*.pc
%_libdir/*.so


%changelog
* Sat Jun 7 2014 Andrew Clark <andyc@altlinux.ru> 0.5.1-alt2
- spec file has been changed

* Thu May 29 2014 Andrew Clark <andyc@altlinux.ru> 0.5.1-alt1
- initial build for ALT Linux
