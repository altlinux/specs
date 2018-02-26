%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: sprng
Version: 4.0
Release: alt10
Summary: The Scalable Parallel Random Number Generators Library
License: GPL v2
Group: Sciences/Mathematics
Url: http://sprng.cs.fsu.edu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://sprng.cs.fsu.edu/Version4.0/sprng4.tar.gz

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
Requires: lib%name-devel = %version-%release
Requires: %name = %version-%release
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

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

rm -fR autom4te.cache
sed -i -e 's/(mpiimpl)/%mpiimpl/' configure.ac
%add_optflags %optflags_shared
%autoreconf
%configure
%make

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

pushd %buildroot%_bindir
mv sprng-simple.tmp sprng-simple_mpi.%name
mv pi-simple.tmp pi-simple_mpi.%name
mv seedf.tmp seedf_mpi.%name
mv seedf-simple.tmp seedf-simple_mpi.%name
mv seed.tmp seed_mpi.%name
mv seed-simple.tmp seed-simple_mpi.%name
mv sprngf.tmp sprngf_mpi.%name
mv sprngf-simple.tmp sprngf-simple_mpi.%name
mv sprng.tmp sprng_mpi.%name
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
mv metropolis.tmp metropolis.%name
mv convert.tmp convert.%name
mv convertf.tmp convertf.%name
mv pif-simple.tmp pif-simple.%name
mv simple-simple.tmp simple-simple.%name
mv simplef-simple.tmp simplef-simple.%name
mv spawn.tmp spawn.%name
mv spawnf.tmp spawnf.%name
mv subroutinef.tmp subroutinef.%name
popd
rm -f %buildroot%_bindir/libsprng.a

install -d %buildroot%_includedir
install -p -m644 include/*.h %buildroot%_includedir

install -d %buildroot%_datadir/%name/examples/mpisprng
install -d %buildroot%_datadir/%name/examples/tests/mpitests
install -p -m644 EXAMPLES/*.F EXAMPLES/*.cpp EXAMPLES/*.h \
	%buildroot%_datadir/%name/examples
install -p -m644 EXAMPLES/mpisprng/*.F EXAMPLES/mpisprng/*.cpp \
	EXAMPLES/mpisprng/*.h \
	%buildroot%_datadir/%name/examples/mpisprng
install -p -m644 TESTS/*.cpp TESTS/*.h \
	%buildroot%_datadir/%name/examples/tests
install -p -m644 TESTS/mpitests/*.cpp TESTS/mpitests/*.h \
	%buildroot%_datadir/%name/examples/tests/mpitests
install -p -m644 check/*/*.data %buildroot%_datadir/%name

%files
%doc DOCS/README AUTHORS ChangeLog COPYING
%_bindir/*.*
%_datadir/%name
%exclude %_datadir/%name/examples

%files -n lib%name-devel
%_includedir/*
%_libdir/*.a

%files examples
%_datadir/%name/examples

%changelog
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
