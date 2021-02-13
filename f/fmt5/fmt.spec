Name: fmt5
Version: 5.3.0
Release: alt2

Summary: An open-source formatting library for C++
License: BSD
Group: System/Legacy libraries
Url: http://fmtlib.net/

Source: libfmt-%version.tar

BuildRequires: cmake ctest gcc-c++

%package -n lib%name
Summary: An open-source formatting library for C++
Group: System/Legacy libraries

%define desc fmt (formerly cppformat) is an open-source formatting library. \
It can be used as a fast and safe alternative to printf and IOStreams.

%description
%desc

%description -n lib%name
%desc

%prep
%setup -n libfmt-%version

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

%files -n lib%name
%doc LICENSE* README*
%_libdir/libfmt.so.*

%changelog
* Sat Feb 13 2021 Nazarov Denis <nenderus@altlinux.org> 5.3.0-alt2
- Build as legacy library

* Wed Jan 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.0-alt1
- initial
