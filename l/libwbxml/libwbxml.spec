
Name: libwbxml
Url: https://libwbxml.opensync.org
License: LGPLv2.1+
Group: System/Libraries
Summary: WBXML parser and compiler library
Version: 0.11.2
Release: alt1

Source0: libwbxml-%version.tar.bz2

Provides: libwbxml2 = %version-%release
Obsoletes: libwbxml2 <  %version-%release

BuildRequires: gcc-c++ cmake cmake-modules
BuildRequires: libexpat-devel libpopt-devel zlib-devel libxml2-devel libcheck-devel

%description
wbxml2 is a library that includes a WBXML parser and a WBXML compiler.
Unlike wbxml, it does not depend on libxml2 but on expat, making it
faster and more portable. WBXML Library contains a library and its
associated tools to Parse, Encode and Handle WBXML documents. The WBXML
(Wireless Binary XML) format is a binary representation of XML, and it
has been defined by the Wap Forum.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Requires: %name = %version-%release
Provides: libwbxml2-devel = %version-%release
Obsoletes: libwbxml2-devel <  %version-%release

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%package -n wbxml
Summary: Libraries for %name
Group: System/Libraries
Requires: %name = %version-%release
Provides: wbxml2 = %version-%release
Obsoletes: wbxml2 <  %version-%release

%description -n wbxml
This packages contains wbxml2 tools

%prep
%setup -q
sed -i -e  '/Requires: expat >= 2.0/d' libwbxml2.pc.cmake

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
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/CMake/Modules/FindLibWbxml2.cmake

%files -n wbxml
%_bindir/*

%changelog
* Fri Aug 31 2012 Alexey Shabalin <shaba@altlinux.ru> 0.11.2-alt1
- 0.11.2

* Wed May 13 2009 Alexey Shabalin <shaba@altlinux.ru> 0.10.7-alt1
- 0.10.7

* Thu Nov 08 2007 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt3.svn53synce
- update to svn53 + synce patches

* Fri Jun 01 2007 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt2.svn49synce
- update to svn49 for synce

* Mon Oct 09 2006 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt1
- Initial package

