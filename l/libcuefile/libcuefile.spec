%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: libcuefile
Version: r471
Release: alt2.svn20110618
Summary: cue and toc file parsers and utilities
License: GPLv2
Group: System/Libraries
Url: https://www.musepack.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.musepack.net/libcuefile/trunk/
Source: %name-%version.tar

BuildPreReq: cmake

%description
This library has been stripped down from cuetools
http://developer.berlios.de/projects/cuetools/

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %EVR

%description devel
This library has been stripped down from cuetools
http://developer.berlios.de/projects/cuetools/

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
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

%install
%makeinstall_std

install -d %buildroot%_includedir
cp -fR include/cuetools %buildroot%_includedir/

%files
%doc AUTHORS README
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> r471-alt2.svn20110618
- NMU: fixed build with LTO

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r471-alt1.svn20110618
- Initial build for Sisyphus

