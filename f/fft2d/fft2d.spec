%define sover 0

Name: fft2d
Version: 1
Release: alt1
Summary: General Purpose 2D,3D FFT (Fast Fourier Transform) Package
License: Free
Group: Sciences/Mathematics
Url: http://www.kurims.kyoto-u.ac.jp/~ooura/fft.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: Makefile

BuildPreReq: gcc-fortran

%description
This is a package to calculate Discrete Fourier/Cosine/Sine Transforms
of 2,3-dimensional sequences of length 2^N.

%package -n lib%name
Summary: General Purpose 2D,3D FFT (Fast Fourier Transform) Package
Group: System/Libraries

%description -n lib%name
This is a package to calculate Discrete Fourier/Cosine/Sine Transforms
of 2,3-dimensional sequences of length 2^N.

%package -n lib%name-devel
Summary: Development files of lib%name
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
This is a package to calculate Discrete Fourier/Cosine/Sine Transforms
of 2,3-dimensional sequences of length 2^N.

This package contains development files of lib%name.

%prep
%setup

install -p -m644 %SOURCE1 ./

%build
%add_optflags %optflags_shared
%make_build

%install
install -d %buildroot%_libdir
for i in lib*.so; do
	install -m644 $i.%sover %buildroot%_libdir/
	ln -s $i.%sover %buildroot%_libdir/$i
done

%files -n lib%name
%doc *.txt
%_libdir/*.so.*

%files -n lib%name-devel
%doc *.f *.c
%_libdir/*.so

%changelog
* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1-alt1
- Initial build for Sisyphus

