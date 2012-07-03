# original spec by ldv@

%define mpiimpl openmpi
%define mpidir %_libdir/openmpi

Name: libfftw3-mpi
Version: 3.3
Release: alt2
Epoch: 1

Summary: Library for computing Fast Fourier Transforms (with MPI support)
License: GPLv2+
Group: System/Libraries
Url: http://www.fftw.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# ftp://ftp.fftw.org/pub/fftw/fftw-%version.tar.gz
Source: fftw-%version.tar

BuildPreReq: gcc-fortran ghostscript-classic glibc-devel ocaml
BuildPreReq: libgfortran-devel
BuildPreReq: %mpiimpl-devel

%description
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains shared libraries, double and long-double
precision, with MPI support.

%package devel
Summary: Development files for parallel FFTW
Group: Development/Other
Requires: %name = %epoch:%version-%release
Conflicts: libfftw3-devel

%description devel
FFTW is a free collection of fast C routines for computing the Discrete
Fourier Transform in one or more dimensions.  It includes complex, real,
symmetric, and parallel transforms, and can handle arbitrary array sizes
efficiently.  FFTW is typically faster than other publically-available
FFT implementations, and is even competitive with vendor-tuned libraries.
To achieve this performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

This package contains development files for FFTW, double and long-double
precision, with MPI support.

%prep
%setup
mkdir double long-double

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir
%add_optflags %optflags_shared
%autoreconf

function buildIt() {
	ln -s ../configure .
	%configure $1 \
		--enable-portable-binary \
		--enable-shared \
		--disable-static \
		--enable-fma \
		--enable-mpi \
		--enable-threads \
		--with-g77-wrappers
	sed -i 's|^\(STRIP\).*|\1=echo|' libtool
	sed -i 's|^\(old_striplib\).*|\1=echo|' libtool
	sed -i 's|^\(striplib\).*|\1=echo|' libtool
	%make
}

pushd double
#cp ../mpi ./ -fR
buildIt
popd

pushd long-double
buildIt --enable-long-double
popd

%install
for i in double long-double; do
	%makeinstall includedir=%buildroot%_includedir/fftw3-mpi -C $i
done

sed -i 's|lfftw3|lfftw3_mpi|' %buildroot%_pkgconfigdir/fftw3.pc
sed -i 's|lfftw3l|lfftw3l_mpi|' %buildroot%_pkgconfigdir/fftw3l.pc
sed -i 's|^\(includedir\).*|\1=%_includedir/fftw3-mpi|' \
	%buildroot%_pkgconfigdir/fftw3.pc \
	%buildroot%_pkgconfigdir/fftw3l.pc

%files
%_libdir/*.so.*

%files devel
%_bindir/*
%_includedir/fftw3-mpi
%_libdir/*.so
%_pkgconfigdir/*
%_infodir/*
%_man1dir/*

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3-alt2
- Rebuilt with OpenMPI 1.6

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.3-alt1
- Version 3.3

* Tue Mar 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2.2-alt4
- Fixed pkgconfig files

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2.2-alt3
- Created shared libraries instead of static

* Fri Jun 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2.2-alt2
- Created MPI links for libraries

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2.2-alt1
- Version 3.2.2

* Thu Nov 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2r.1-alt3
- Rebuilt without openmpi-devel-static

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2r.1-alt2
- Rebuild with PIC

* Fri May 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2r.1-alt1
- Version 3.2.1

* Wed May 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2alpha3-alt1
- Initial build for Sisyphus

