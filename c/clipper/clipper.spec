Name: clipper
Version: 6.2.1
Release: alt1
Summary: Open source freeware library for clipping and offsetting lines and polygons
License: Boost Software License
Group: Graphics
Url: http://www.angusj.com/delphi/clipper.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake

%description
The Clipper library performs line & polygon clipping - intersection,
union, difference & exclusive-or, and line & polygon offsetting. The
library is based on Vatti's clipping algorithm.

%package -n lib%name
Summary: Open source freeware library for clipping and offsetting lines and polygons
Group: System/Libraries

%description -n lib%name
The Clipper library performs line & polygon clipping - intersection,
union, difference & exclusive-or, and line & polygon offsetting. The
library is based on Vatti's clipping algorithm.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
The Clipper library performs line & polygon clipping - intersection,
union, difference & exclusive-or, and line & polygon offsetting. The
library is based on Vatti's clipping algorithm.

This package contains development files of %name.

%package -n lib%name-devel-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
The Clipper library performs line & polygon clipping - intersection,
union, difference & exclusive-or, and line & polygon offsetting. The
library is based on Vatti's clipping algorithm.

This package contains development documentation for %name.

%prep
%setup

sed -i 's|@VERSION@|%version|' cpp/polyclipping.pc.cmakein

%build
pushd cpp
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1
popd

%install
%makeinstall_std -C cpp

%files -n lib%name
%doc README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-docs
%doc Documentation/*

%changelog
* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2.1-alt1
- Initial build for Sisyphus

