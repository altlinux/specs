Name: libBatch
Version: 1.6.0
Release: alt2.git20130114
Summary: Generic batch management library
License: LGPLv2.1
Group: System/Libraries
Url: http://www.salome-platform.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.salome-platform.org/LIBBATCH_SRC.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake python-devel libtorque-devel swig
BuildPreReq: %_bindir/ssh

%description
libBatch: generic batch management library. This is a part of SALOME
project.

%package devel
Summary: Development files of generic batch management library
Group: Development/C++
Requires: %name = %version-%release
Requires: libtorque-devel

%description devel
libBatch: generic batch management library. This is a part of SALOME
project.

This package contains development files of libBatch.

%package -n python-module-%name
Summary: Python wrapper for generic batch management library
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%name
libBatch: generic batch management library. This is a part of SALOME
project.

This package contains python wrapper for libBatch.

%package devel-doc-fr
Summary: Documentation for generic batch management library
Group: Development/Documentation
BuildArch: noarch

%description devel-doc-fr
libBatch: generic batch management library. This is a part of SALOME
project.

This package contains development documentation for libBatch in French.

%prep
%setup

%build
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
%ifarch x86_64
	-DLIB_SUFFIX:STRING=64 \
%endif
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	.
%make_build VERBOSE=1

%install
%makeinstall_std VERBOSE=1

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_datadir/Batch
%_libdir/cmake

%files -n python-module-%name
%python_sitelibdir/*

%files devel-doc-fr
%_docdir/Batch

%changelog
* Tue Feb 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2.git20130114
- Version 1.6.0

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.git20120606
- Fixed build with new glibc

* Thu Aug 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20120606
- Initial build for Sisyphus

