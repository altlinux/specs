%def_disable snapshot
%def_disable check

%define _name cpprestsdk
%define ver_major 2.10

Name: cpprest
Version: %ver_major.2
Release: alt1

Summary: C++ REST library
Group: System/Libraries
License: MIT
Url: https://github.com/Microsoft/%_name

Source: https://github.com/Microsoft/%_name/archive/v%version.tar.gz#/%_name-%version.tar.gz

BuildRequires: gcc-c++ cmake
BuildRequires: boost-devel >= 1.55 boost-interprocess-devel boost-filesystem-devel
BuildRequires: boost-asio-devel boost-locale-devel
BuildRequires: libssl-devel >= 1.0
BuildRequires: websocketpp-devel >= 0.4
BuildRequires: zlib-devel

%description
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

Also known as Casablanca.

%package -n lib%name
Summary: %summary
Group: System/Libraries

%description -n lib%name
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

This package provides shared %name library.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release
Requires: libssl-devel

%description -n lib%name-devel
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

This package provides development files for %name library.

%prep
%setup -n %_name-%version
# Remove bundled sources of websocketpp
rm -r Release/libs
# Remove file ThirdPartyNotices.txt, which is associated to websocketpp
rm -f ThirdPartyNotices.txt
# fix libdir
subst 's|\(DESTINATION \)lib|\1%_lib|' Release/src/CMakeLists.txt

%build
cd Release
export CXXFLAGS="%optflags -Wl,--as-needed"
%cmake .. -DCMAKE_BUILD_TYPE=Release \
	  -DCPPREST_EXPORT_DIR=%_lib/%_name \
	  -DCMAKE_INSTALL_DO_STRIP=false \
	  -DCMAKE_INCLUDE_PATH=%_datadir/cmake/websocketpp/
%cmake_build

%install
cd Release
%cmakeinstall_std

%check
cd Release
LD_LIBRARY_PATH=%buildroot/%_libdir %make -C BUILD test

%files -n lib%name
%_libdir/libcpprest.so.*
%doc README.md license.txt

%files -n lib%name-devel
%_includedir/%name
%_includedir/pplx
%_libdir/libcpprest.so
%_libdir/%_name/
%doc README.md

%changelog
* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.2-alt1
- 2.10.2

* Fri Jan 19 2018 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- first build for Sisyphus

