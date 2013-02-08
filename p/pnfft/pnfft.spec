%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: pnfft
Version: 1.0.5
Release: alt1.alpha
Summary: Parallel software library for the calculation of three-dimensional nonequispaced FFTs
License: GPLv3+
Group: Sciences/Mathematics
Url: http://www-user.tu-chemnitz.de/~potts/nfft/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel libpfft-devel libfftw3-mpi-devel

%description
PNFFT is a software library written in C for computing parallel
nonequispaced fast Fourier transformations.

%package -n lib%name
Summary: Shared libraries of PNFFT
Group: System/Libraries

%description -n lib%name
PNFFT is a software library written in C for computing parallel
nonequispaced fast Fourier transformations.

This package contains shared libraries of PNFFT.

%package -n lib%name-devel
Summary: Development files of PNFFT
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
PNFFT is a software library written in C for computing parallel
nonequispaced fast Fourier transformations.

This package contains development files of PNFFT.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

./bootstrap.sh
%add_optflags -I%mpidir/include
%configure \
	--enable-static=no \
	--enable-mpi \
	--enable-threads \
	--with-fftw3=%prefix \
	--with-fftw3-includedir=%_includedir/fftw3-mpi \
	--with-pfft=%prefix
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -d %buildroot%_pkgconfigdir
install -m644 *.pc %buildroot%_pkgconfigdir

%files -n lib%name
%doc AUTHORS CONVENTIONS ChangeLog README TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.alpha
- Version 1.0.5-alpha

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.alpha
- Initial build for Sisyphus

