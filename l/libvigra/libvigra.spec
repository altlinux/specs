%define _name vigra
%def_disable static
%def_with hdf5

Name: lib%_name
Version: 1.11.1
Release: alt1

Summary: Generic Programming for Computer Vision
License: MIT
Group: System/Libraries
Url: http://ukoethe.github.io/%_name

# VCS https://github.com/ukoethe/%name/
Source: https://github.com/ukoethe/%_name/releases/download/Version-1-11-1/%_name-%version-src.tar.gz
# partially deimproved FindOpenEXR
Patch: vigra-1.11.0-alt-findexr.patch

# Automatically added by buildreq on Wed Jun 13 2007
BuildRequires: gcc-c++ cmake libfftw3-devel libjpeg-devel libpng-devel libtiff-devel
BuildRequires: openexr-devel doxygen
%{?_with_hdf5:BuildRequires: libhdf5-devel}
%ifnarch e2k
BuildRequires: libgomp-devel
%endif

Provides: %_name
Obsoletes: %_name

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel
computer vision library that puts its main emphasize on customizable
algorithms and data structures.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %version-%release
Provides: %_name-devel
Obsoletes: %_name-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package devel-doc
Summary: Development documentation for vigra library
Group: Development/C++
Requires: %name-devel = %version-%release
Provides: %_name-devel-doc
Obsoletes: %_name-devel-doc
BuildArch: noarch

%description devel-doc
Development documentation for vigra library.

%prep
%setup -n %_name-%version
%patch
%ifarch e2k
# unsupported as of lcc 1.21.20
sed -i 's,-ftemplate-depth=900,,' CMakeLists.txt
%endif

%build
%cmake -DWITH_VIGRANUMPY:BOOL=OFF \
%if_with hdf5
	-DWITH_HDF5:BOOL=ON \
%endif
%ifarch e2k
	-DSUFFICIENT_TEMPLATE_DEPTH:BOOL=TRUE \
%endif
	-DWITH_OPENEXR:BOOL=ON \
	-DDOCINSTALL:STRING=share/doc
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/%{name}impex.so.*

%files devel
%_bindir/%_name-config
%_includedir/%_name/
%_libdir/*.so
%_libdir/%_name/

%files devel-doc
%_datadir/doc/%_name/

%exclude %_datadir/doc/%{_name}numpy


%changelog
* Thu Apr 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- 1.11.1

* Sat Aug 26 2017 Michael Shigorin <mike@altlinux.org> 1.11.0-alt2
- introduce hdf5 knob (on by default)
- E2K: avoid libgomp and lcc-unsupported -ftemplate-depth

* Sun Apr 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0

* Sun Jul 12 2015 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt2
- updated to 1.10.0_72b8210c
- enabled OpenEXR support (required by hugin)

* Wed Jan 29 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.10.0-alt1
- 1.10.0
- build system changed to CMAKE
- patch removed
- devel-docs package removed

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2.2
- Rebuilt with libpng15

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2.1
- rebuild for set:provides by request of mithraen

* Fri Jan 09 2009 Victor Forsyuk <force@altlinux.org> 1.6.0-alt2
- Remove obsolete ldconfig calls.

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 1.6.0-alt1
- 1.6.0

* Tue Jul 10 2007 Victor Forsyuk <force@altlinux.org> 1.5.0-alt2
- Fix 64 bit build.

* Mon Jul 09 2007 Victor Forsyuk <force@altlinux.org> 1.5.0-alt1
- Initial build.
