%define soname 9
Name: tinyxml2
Version: 9.0.0
Release: alt1
Summary: Simple, small, efficient, C++ XML parser
License: Zlib
Group: File tools
Url: http://www.grinninglizard.com/tinyxml2/

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildPreReq: cmake gcc-c++ ctest
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
%patch0 -p1

%build
%cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
        -DBUILD_SHARED_LIBS=ON \
	-DCMAKE_BUILD_TYPE=Release \
	.
%cmake_build

doxygen dox
%check
%make test

%install
%cmakeinstall_std

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
* Fri Dec 31 2021 Anton Farygin <rider@altlinux.ru> 9.0.0-alt1
- 8.1.0 -> 9.0.0

* Thu Jun 10 2021 Anton Farygin <rider@altlinux.ru> 8.1.0-alt1
- 8.1.0

* Fri Oct 09 2020 Anton Farygin <rider@altlinux.ru> 8.0.0-alt1
- 8.0.0

* Fri Oct 09 2020 Anton Farygin <rider@altlinux.ru> 7.1.0-alt1
- 7.1.0

* Mon Dec 03 2018 Anton Farygin <rider@altlinux.ru> 7.0.1-alt1
- 7.0.1

* Fri May 04 2018 Anton Farygin <rider@altlinux.ru> 6.2.0-alt1
- 6.2.0
- package with shared library renamed for policy

* Mon Oct 09 2017 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1
- new version

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus

