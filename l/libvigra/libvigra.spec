%def_disable snapshot
%define _name vigra
%def_disable static
%def_with hdf5
# required https://github.com/hmeine/vigraqt
%def_disable python
%if_enabled python
%define modname %{_name}numpy
%endif

Name: lib%_name
Version: 1.12.1
Release: alt1

Summary: Generic Programming for Computer Vision
License: MIT
Group: System/Libraries
Url: http://ukoethe.github.io/%_name

Vcs: https://github.com/ukoethe/vigra.git

%define git_ver %(echo %version|tr . -)

%if_disabled snapshot
Source: https://github.com/ukoethe/%_name/archive/Version-%git_ver/%_name-%version-src.tar.gz
%else

Source: %_name-%version.tar
%endif

# for vigra-config
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ cmake libfftw3-devel libjpeg-devel libpng-devel libtiff-devel
BuildRequires: openexr-devel >= 3
BuildRequires: doxygen
%{?_with_hdf5:BuildRequires: libhdf5-devel}
%{?_enable_python:BuildRequires: boost-python3-devel libnumpy-devel}
BuildRequires: libgomp-devel

Provides: %_name
Obsoletes: %_name

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel
computer vision library that puts its main emphasize on customizable
algorithms and data structures.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %EVR
Provides: %_name-devel
Obsoletes: %_name-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package devel-doc
Summary: Development documentation for vigra library
Group: Development/C++
Requires: %name-devel = %EVR
Provides: %_name-devel-doc
Obsoletes: %_name-devel-doc
BuildArch: noarch

%description devel-doc
Development documentation for VIGRA library.

%if_enabled python
%package -n python3-module-%modname
Summary: Python3 bindings for VIGRA
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%modname
This package provides Python3 bindings for VIGRA library.
%endif

%prep
%setup -n %_name-%{?_enable_snapshot:%version}%{?_disable_snapshot:Version-%git_ver}
# fix shebang
sed -i 's|\(#!\/usr\/bin\/\)env \(python\)|\1\23|' config/vigra-config.in

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
%{?_disable_python:-DWITH_VIGRANUMPY:BOOL=OFF} \
%{?_enable_python:-DWITH_VIGRANUMPY:BOOL=ON -DPYTHON_VERSION=3} \
%if_with hdf5
	-DWITH_HDF5:BOOL=ON \
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

%if_enabled python
%files -n python3-module-%modname
%python3_sitelibdir/%_name/
%_libdir/%modname/VigranumpyConfig.cmake
%endif


%changelog
* Tue Sep 03 2024 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Mon May 06 2024 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt2
- updated to 1-11-2-23-gd4250a02
- removed obsolete E2K stuff

* Mon Feb 12 2024 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt1
- updated to 1-11-2-22-g502d5bc7
- removed upstreamed patch from previous release
- built against HDF5-1.14.3

* Sat Dec 02 2023 Ivan A. Melnikov <iv@altlinux.org> 1.11.1-alt3
- fix build with OpenEXR 3+ with patch from fedora

* Tue Dec 31 2019 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt2
- updated to 1-11-1-45-g8acd73a5

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
