%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: sprng
Version: 4.4
Release: alt3
Summary: The Scalable Parallel Random Number Generators Library
License: GPL v2
Group: Sciences/Mathematics
Url: http://sprng.cs.fsu.edu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://sprng.cs.fsu.edu/Version4.0/sprng4.tar.gz
Patch: sprng-gcc8-fix.patch

BuildPreReq: gcc-fortran gcc-c++ %mpiimpl-devel
BuildPreReq: libgmp-devel libgmp_cxx-devel

%description
Computational stochastic approaches (Monte Carlo methods) based on the random
sampling are becoming extremely important research tools not only in their
"traditional" fields such as physics, chemistry or applied mathematics but also
in social sciences and, recently, in various branches of industry. An indication
of importance is, for example, the fact that Monte Carlo calculations consume
about one half of the supercomputer cycles. One of the indispensable and
important ingredients for reliable and statistically sound calculations is the
source of pseudo random numbers. The goal of our project is to develop,
implement and test a scalable package for parallel pseudo random number
generation.

%package -n lib%name-devel
Summary: Static development files of SPRNG
Group: Development/Other
Requires: %mpiimpl-devel

%description -n lib%name-devel
Computational stochastic approaches (Monte Carlo methods) based on the random
sampling are becoming extremely important research tools not only in their
"traditional" fields such as physics, chemistry or applied mathematics but also
in social sciences and, recently, in various branches of industry. An indication
of importance is, for example, the fact that Monte Carlo calculations consume
about one half of the supercomputer cycles. One of the indispensable and
important ingredients for reliable and statistically sound calculations is the
source of pseudo random numbers. The goal of our project is to develop,
implement and test a scalable package for parallel pseudo random number
generation.

This package contains static development files of SPRNG.

%package examples
Summary: Example source codes for SPRNG
Group: Development/Documentation
BuildArch: noarch

%description examples
Computational stochastic approaches (Monte Carlo methods) based on the random
sampling are becoming extremely important research tools not only in their
"traditional" fields such as physics, chemistry or applied mathematics but also
in social sciences and, recently, in various branches of industry. An indication
of importance is, for example, the fact that Monte Carlo calculations consume
about one half of the supercomputer cycles. One of the indispensable and
important ingredients for reliable and statistically sound calculations is the
source of pseudo random numbers. The goal of our project is to develop,
implement and test a scalable package for parallel pseudo random number
generation.

This package contains example source codes for SPRNG.

%prep
%setup
%patch -p2

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

rm -fR autom4te.cache
sed -i -e 's/(mpiimpl)/%mpiimpl/' configure.ac
%add_optflags %optflags_shared -I%mpidir/include
%autoreconf
%configure
%make MPI_DIR=%mpidir

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

pushd %buildroot%_bindir
mv equidist.tmp equidist.%name
mv perm.tmp perm.%name
mv serial.tmp serial.%name
mv poker.tmp poker.%name
mv collisions.tmp collisions.%name
mv gap.tmp gap.%name
mv maxt.tmp maxt.%name
mv sum.tmp sum.%name
mv coupon.tmp coupon.%name
mv runs.tmp runs.%name
mv random_walk.tmp random_walk.%name
mv wolff.tmp wolff.%name
mv wolffind.tmp wolffind.%name
mv wolfftest.tmp wolfftest.%name
mv metropolis.tmp metropolis.%name
popd
rm -f %buildroot%_bindir/libsprng.a

install -d %buildroot%_includedir
install -p -m644 include/*.h %buildroot%_includedir

install -d %buildroot%_datadir/%name/examples/tests/mpitests
cp -fR EXAMPLES/* \
	%buildroot%_datadir/%name/examples/
install -p -m644 TESTS/*.cpp TESTS/*.h \
	%buildroot%_datadir/%name/examples/tests
install -p -m644 TESTS/mpitests/*.cpp TESTS/mpitests/*.h \
	%buildroot%_datadir/%name/examples/tests/mpitests

%files
%doc DOCS/README AUTHORS ChangeLog COPYING NEWS
%_bindir/*.*
%exclude %_datadir/%name/examples

%files -n lib%name-devel
%_includedir/*
%_libdir/*.a

%files examples
%_datadir/%name/examples

%changelog
* Mon Sep 20 2021 Ivan Razzhivin <underwit@altlinux.org> 4.4-alt3
- LTO fix

* Tue Feb 12 2019 Ivan Razzhivin <underwit@altlinux.org> 4.4-alt2
- GCC8 fix

* Fri Jul 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4-alt1
- Version 4.4

* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt10
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt9
- Fixed RPATH

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt8
- Rebuilt for debuginfo

* Mon Feb 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt7
- Fixed build

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt6
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt5
- Fixed linking

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt4
- Rebuilt without rpm-build-compat

* Mon Oct 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt3
- Disabled requirement on openmpi-devel-static

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt2
- Rebuild with PIC

* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1
- Initial build for Sisyphus
