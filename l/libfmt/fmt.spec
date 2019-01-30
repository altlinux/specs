Name: libfmt
Version: 5.3.0
Release: alt1

Summary: An open-source formatting library for C++
License: BSD
Group: System/Libraries
Url: http://fmtlib.net/

Source: %name-%version.tar

BuildRequires: cmake ctest gcc-c++

%package devel
Summary: An open-source formatting library for C++
Group: Development/C++

%define desc fmt (formerly cppformat) is an open-source formatting library. \
It can be used as a fast and safe alternative to printf and IOStreams.

%description
%desc

%description devel
%desc
This package contains development part of fmt.

%prep
%setup

%build
cmake  	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DFMT_PKGCONFIG_DIR=%_pkgconfigdir \
	-DBUILD_SHARED_LIBS=ON \
	.

%make_build

%check
make test

%install
%makeinstall_std

%files
%doc LICENSE* README*
%_libdir/libfmt.so.*

%files devel
%_includedir/fmt
%_libdir/cmake/fmt
%_pkgconfigdir/fmt.pc
%_libdir/libfmt.so

%changelog
* Wed Jan 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.0-alt1
- initial
