Name: nfft
Version: 3.2.2
Release: alt1
Summary: Nonequispaced FFT, generalisations, inversion, and applications
License: GPLv2+
Group: Sciences/Mathematics
Url: http://www-user.tu-chemnitz.de/~potts/nfft/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libfftw3-devel

Requires: lib%name = %version-%release

%description
NFFT3 is a software library written in C for computing nonequispaced
fast Fourier  and related transformations. In detail, NFFT3 implements

 1) The nonequispaced fast Fourier transform (NFFT)
    - the forward transform (NFFT)
    - the adjoint transform (adjoint NFFT)
 2) Generalisations of the NFFT
    - to arbitrary knots in time and frequency domain (NNFFT)
    - to the sphere S^2 (NFSFT)
    - to the hyperbolic cross (NSFFT)
    - to real-valued data, i.e. (co)sine transforms, (NFCT, NFST)
    - to the rotation group (NFSOFT)
 3) Generalised inverses based on iterative methods, e.g. CGNR, CGNE
 4) Applications in
    - medical imaging
         (i) magnetic resonance imaging
        (ii) computerised tomography
    - summation schemes
          (i) fast Gauss transform (FGT)
         (ii) singular kernels
        (iii) zonal kernels
    - polar FFT, discrete Radon transform, ridgelet transform

%package -n lib%name
Summary: Shared libraries of NFFT3
Group: System/Libraries

%description -n lib%name
NFFT3 is a software library written in C for computing nonequispaced
fast Fourier  and related transformations.

This package contains shared libraries of NFFT3.

%package -n lib%name-devel
Summary: Development files of NFFT3
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
NFFT3 is a software library written in C for computing nonequispaced
fast Fourier  and related transformations.

This package contains development files of NFFT3.

%package -n lib%name-devel-doc
Summary: Development documentation for NFFT3
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
NFFT3 is a software library written in C for computing nonequispaced
fast Fourier  and related transformations.

This package contains development documentation for NFFT3.

%prep
%setup

%build
./bootstrap.sh
%configure \
	--enable-static=no \
	--enable-all \
	--enable-matlab-argchecks=no \
	--with-fftw3=%prefix
%make_build

%install
%makeinstall_std pkgdatadir=%buildroot%_datadir

install -d %buildroot%_bindir

for i in $(find applications/ -name .libs); do
	rm -f $i/*.*
	install -m755 $i/* %buildroot%_bindir
done

%make -C applications clean
%make -C examples clean

install -d %buildroot%_docdir/%name/api
cp -fR doc/api/html %buildroot%_docdir/%name/api/
cp -fR doc/logo %buildroot%_docdir/%name/
cp -fR examples %buildroot%_docdir/%name/

mv %buildroot%_bindir/reconstruct_data_gridding \
	%buildroot%_bindir/reconstruct_data_gridding_3d

%files
%doc AUTHORS ChangeLog NEWS README
%doc applications
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc %_docdir/%name

%changelog
* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.2-alt1
- Version 3.2.2

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt2
- Fixed build

* Mon Dec 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1
- Initial build for Sisyphus

