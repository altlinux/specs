%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: pfft
Version: 1.0.5
Release: alt2.alpha
Summary: Parallel FFT based on FFTW
License: GPLv3+
Group: Sciences/Mathematics
Url: http://www-user.tu-chemnitz.de/~potts/nfft/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libfftw3-mpi-devel %mpiimpl-devel

%description
PFFT is a software library written in C for computing parallel fast
Fourier transformations.

%package -n lib%name
Summary: Shared libraries of PFFT
Group: System/Libraries

%description -n lib%name
PFFT is a software library written in C for computing parallel fast
Fourier transformations.

This package contains shared libraries of PFFT.

%package -n lib%name-devel
Summary: Development files of PFFT
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
PFFT is a software library written in C for computing parallel fast
Fourier transformations.

This package contains development files of PFFT.

%prep
%setup

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export LDFLAGS=-L%mpidir/lib
export MPIDIR=%mpidir

./bootstrap.sh
%add_optflags -I%mpidir/include -I%_includedir/fftw3-mpi
%configure \
	--enable-static=no \
	--with-gfortran-wrappers \
	--with-fftw3-includedir=%_includedir/fftw3-mpi
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

%makeinstall_std

%files -n lib%name
%doc AUTHORS ChangeLog CONVENTIONS NEWS README TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt2.alpha
- Rebuilt with OpenMPI 1.6

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.alpha
- Version 1.0.5-alpha

* Mon Dec 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.alpha
- Initial build for Sisyphus

