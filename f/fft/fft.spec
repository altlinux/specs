%define sover 0

Name: fft
Version: 1
Release: alt1
Summary: General Purpose FFT (Fast Fourier/Cosine/Sine Transform) Package
License: Free
Group: Sciences/Mathematics
Url: http://www.kurims.kyoto-u.ac.jp/~ooura/fft.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-fortran

%description
This is a package to calculate Discrete Fourier/Cosine/Sine Transforms
of 1-dimensional sequences of length 2^N. This package contains C and
Fortran FFT codes.

%package -n lib%name
Summary: General Purpose FFT (Fast Fourier/Cosine/Sine Transform) Package
Group: System/Libraries

%description -n lib%name
This is a package to calculate Discrete Fourier/Cosine/Sine Transforms
of 1-dimensional sequences of length 2^N. This package contains C and
Fortran FFT codes.

%package -n lib%name-devel
Summary: Development files of lib%name
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
This is a package to calculate Discrete Fourier/Cosine/Sine Transforms
of 1-dimensional sequences of length 2^N. This package contains C and
Fortran FFT codes.

This package contains development files of lib%name.

%prep
%setup

%build
%add_optflags %optflags_shared
mkdir c f
cp *.c c/
cp *.f f/

pushd c
rm -f *_h.c
gcc -c *.c %optflags
for i in *.o; do
	j=$(echo $i |sed 's|\.o$||')
	gcc -shared $i -Wl,-soname=lib$j.so.%sover -lm \
		-o ../lib$j.so.%sover
	ln -s lib$j.so.%sover ../lib$j.so
done
popd

pushd f
rm -f *_h.f
gfortran -c *.f %optflags
for i in *.o; do
	j=$(echo $i |sed 's|\.o$||')_f
	gfortran -shared $i -Wl,-soname=lib$j.so.%sover -lm \
		-o ../lib$j.so.%sover
	ln -s lib$j.so.%sover ../lib$j.so
done
popd

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
%_libdir/*.so

%changelog
* Thu Sep 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1-alt1
- Initial build for Sisyphus

