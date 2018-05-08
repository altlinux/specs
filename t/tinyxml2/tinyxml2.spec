%define soname 6
Name: tinyxml2
Version: 6.2.0
Release: alt1
Summary: Simple, small, efficient, C++ XML parser
License: zlib
Group: File tools
Url: http://www.grinninglizard.com/tinyxml2/

Source: %name-%version.tar

BuildPreReq: cmake gcc-c++
BuildPreReq: doxygen

%description
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be
easily integrating into other programs.

%package -n lib%name.%soname
Summary: Simple, small, efficient, C++ XML parser
Group: System/Libraries

%description -n lib%name.%soname
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be
easily integrating into other programs.

%package -n lib%name-devel
Summary: Development files of TinyXML-2
Group: Development/C++
Requires: lib%name.%soname = %EVR

%description -n lib%name-devel
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be
easily integrating into other programs.

This package contains development files of TinyXML-2.

%package -n lib%name-devel-doc
Summary: Documentation for TinyXML-2
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be
easily integrating into other programs.

This package contains documentation for TinyXML-2.

%prep
%setup

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DBUILD_STATIC_LIBS:BOOL=OFF \
	.
%make_build VERBOSE=1

doxygen dox

%install
%makeinstall_std

%files -n lib%name.%soname
%doc readme.md
%_libdir/*.so.%{soname}*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_libdir/cmake/tinyxml2

%files -n lib%name-devel-doc
%doc docs/*

%changelog
* Fri May 04 2018 Anton Farygin <rider@altlinux.ru> 6.2.0-alt1
- 6.2.0
- package with shared library renamed for policy

* Mon Oct 09 2017 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1
- new version

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus

