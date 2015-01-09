Name: libgibsonclient
Version: 1.0.0
Release: alt1.git20140523
Summary: Gibson cache server native client library
License: BSD
Group: System/Libraries
Url: https://github.com/evilsocket/libgibsonclient
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/evilsocket/libgibsonclient.git
Source: %name-%version.tar

BuildPreReq: cmake liblinenoise-devel gcc-c++

%description
Gibson cache server native client library.

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %EVR

%description devel
Gibson cache server native client library.

This package contains development files of %name.

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
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	.

%make_build VERBOSE=1

%install
%makeinstall_std

%files
%doc *.md
%_bindir/*
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140523
- Initial build for Sisyphus

