%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: libsc
Version: 1.6.0
Release: alt1.git20140702
Summary: The SC Library provides support for parallel scientific applications
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.p4est.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel liblapack-devel splint zlib-devel
BuildPreReq: pkgconfig(lua) doxygen graphviz libtrilinos10-devel
BuildPreReq: libepetra10-devel libteuchos10-devel libml10-devel

%description
The SC Library provides support for parallel scientific applications.

%package devel
Summary: Development files of the SC Library
Group: Development/Other
Requires: %name = %EVR

%description devel
The SC Library provides support for parallel scientific applications.

This package contains development files of the SC Library.

%package tools
Summary: Tools for the SC Library
Group: Sciences/Mathematics
Requires: %name = %EVR

%description tools
The SC Library provides support for parallel scientific applications.

This package contains tools for the SC Library.

%package devel-docs
Summary: Documentation for the SC Library
Group: Development/Documentation
BuildArch: noarch

%description devel-docs
The SC Library provides support for parallel scientific applications.

This package contains development documentation for the SC Library.

%prep
%setup

sed -i 's|@VERSION@|%version|' configure.ac
%ifarch x86_64
LIB_SUFFIX=64
%endif
sed -i "s|@64@|$LIB_SUFFIX|" config/sc_package.m4

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

./bootstrap
%configure \
	--enable-mpi \
	--enable-mpiio \
	--enable-static=no \
	--enable-pthread \
	--with-blas=-lopenblas \
	--with-trilinos=%prefix
%make_build

doxygen

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -m644 config/sc_pthread.m4 %buildroot%_datadir/aclocal/

mv doxygen/html doxygen/doxygen

%files
%doc AUTHORS NEWS README
%_libdir/libsc-*.so

%files devel
%_sysconfdir/*
%_includedir/*
%_libdir/*.so
%exclude %_libdir/libsc-*.so
%_datadir/aclocal/*

%files tools
%_bindir/*

%files devel-docs
%doc doc/*.txt doc/*.pdf
%doc doxygen/doxygen

%changelog
* Tue Jul 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20140702
- Initial build for Sisyphus

