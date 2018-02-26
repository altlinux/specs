
Name: wbxml2
Url: http://libwbxml.aymerick.com
License: LGPLv2.1+
Group: System/Libraries
Provides: wbxml2
Summary: WBXML parser and compiler library
Version: 0.10.7
Release: alt1

Source0: %name-%version.tar
Source1: cmake.tar
Source2: tests.tar
Patch0: %name-%version-%release.patch

Requires: libexpat
Requires: lib%name = %version-%release

BuildRequires: gcc-c++ cmake cmake-modules
BuildRequires: libexpat-devel libpopt-devel zlib-devel libxml2-devel libcheck-devel

%description
wbxml2 is a library that includes a WBXML parser and a WBXML compiler.
Unlike wbxml, it does not depend on libxml2 but on expat, making it
faster and more portable. WBXML Library contains a library and its
associated tools to Parse, Encode and Handle WBXML documents. The WBXML
(Wireless Binary XML) format is a binary representation of XML, and it
has been defined by the Wap Forum.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name
This packages contains some library needed for %name

%package -n lib%name-devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%prep
%setup -q
%patch0 -p1
mkdir cmake tests
tar -xf %SOURCE1
tar -xf %SOURCE2

%build
mkdir build
cd build
cmake \
	-D CMAKE_INSTALL_PREFIX:PATH=%_prefix \
%if %{_lib} == lib64
	-D LIB_SUFFIX=64 \
%endif
	-D CMAKE_CXX_FLAGS:STRING="%optflags" \
	-D CMAKE_BUILD_TYPE="Release" \
	-D CMAKE_SKIP_RPATH:BOOL=TRUE ..

%make_build VERBOSE=1

%install
pushd build
%make_install install DESTDIR=%buildroot
popd

%files
%doc AUTHORS INSTALL ChangeLog NEWS README References THANKS TODO
%_bindir/*

%files -n lib%name 
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed May 13 2009 Alexey Shabalin <shaba@altlinux.ru> 0.10.7-alt1
- 0.10.7

* Thu Nov 08 2007 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt3.svn53synce
- update to svn53 + synce patches

* Fri Jun 01 2007 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt2.svn49synce
- update to svn49 for synce

* Mon Oct 09 2006 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt1
- Initial package

