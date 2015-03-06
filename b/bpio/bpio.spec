%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: bpio
Version: 1.0
Release: alt1.git20141106
Summary: Balanced placement I/O library and utils
License: Free
Group: Development/Tools
Url: https://github.com/ORNL-TechInt/bpio
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ORNL-TechInt/bpio.git
Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel liblustre-devel python-devel

Requires: lib%name = %EVR

%description
The Balanced Placement I/O project (BPIO) composes of two interconnected
components:

* A user-space library for optimized data placement
* A synthetic benchmarking tool

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
The Balanced Placement I/O project (BPIO) composes of two interconnected
components:

* A user-space library for optimized data placement
* A synthetic benchmarking tool

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
The Balanced Placement I/O project (BPIO) composes of two interconnected
components:

* A user-space library for optimized data placement
* A synthetic benchmarking tool

This package contains development files of %name.

%package -n python-module-%name
Summary: Python module of of %name
Group: Development/Python
Requires: lib%name = %EVR

%description -n python-module-%name
The Balanced Placement I/O project (BPIO) composes of two interconnected
components:

* A user-space library for optimized data placement
* A synthetic benchmarking tool

This package contains Python module of %name.

%prep
%setup

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--datarootdir=%_datadir/%name \
	--datadir=%_datadir/%name \
	--enable-python
%make_build V=1

%python_build_debug

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

%python_install

%files
%doc ChangeLog *.md
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_datadir/%name

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141106
- Initial build for Sisyphus

