%define sover 0

Name: intcc
Version: 1
Release: alt1
Summary: Clenshaw-Curtis-Quadrature (Numerical Automatic Integrator) Package
License: Distributable
Group: Sciences/Mathematics
Url: http://www.kurims.kyoto-u.ac.jp/~ooura/intcc.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-fortran

%description
Numerical Automatic Integrator
  method    : Chebyshev Series Expansion
  dimension : one
routines
  intcc    : integrator of f(x) over [a,b].
  chebexp  : function f(x) -> Chebyshev series
  chebeval : Chebyshev series -> evaluation of the f(x)

%package -n lib%name
Summary: Clenshaw-Curtis-Quadrature (Numerical Automatic Integrator) Package
Group: System/Libraries

%description -n lib%name
Numerical Automatic Integrator
  method    : Chebyshev Series Expansion
  dimension : one
routines
  intcc    : integrator of f(x) over [a,b].
  chebexp  : function f(x) -> Chebyshev series
  chebeval : Chebyshev series -> evaluation of the f(x)

%package -n lib%name-devel
Summary: Development files of lib%name
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
Numerical Automatic Integrator
  method    : Chebyshev Series Expansion
  dimension : one
routines
  intcc    : integrator of f(x) over [a,b].
  chebexp  : function f(x) -> Chebyshev series
  chebeval : Chebyshev series -> evaluation of the f(x)

This package contains development files of lib%name.

%prep
%setup


%build
mkdir f tc tf ../src
mv *t.c tc/
mv *t.f tf/
cp *.c *.f *.txt *.doc ../src/
mv *.f f/

%add_optflags %optflags_shared

gcc -c %optflags -I$PWD *.c
pushd f
gfortran -c %optflags *.f
popd
pushd tc
gcc -c %optflags -I$PWD/.. *.c
popd
pushd tf
gfortran -c %optflags -I$PWD/../f *.f
popd

for i in fft2f.o *.o; do
	j=$(echo $i |sed 's|\.o$||')
	rm -f lib$j.so*
	if [ "$i" == 'fft2f.o' ]; then
		LIBS=
	fi
	gcc -shared $i -Wl,-soname=lib$j.so.%sover $LIBS -lm \
		-o lib$j.so.%sover
	ln -s lib$j.so.%sover lib$j.so
	if [ "$i" == 'fft2f.o' ]; then
		LIBS="-L. -lfft2f"
	fi
done

LIBS=
pushd f
for i in fft2f.o *.o; do
	j=$(echo $i |sed 's|\.o$||')_f
	rm -f ../lib$j.so*
	if [ "$i" == 'fft2f.o' ]; then
		LIBS=
	fi
	gfortran -shared $i -Wl,-soname=lib$j.so.%sover $LIBS -lm \
		-o ../lib$j.so.%sover
	ln -s lib$j.so.%sover ../lib$j.so
	if [ "$i" == 'fft2f.o' ]; then
		LIBS="-L.. -lfft2f_f"
	fi
done
popd

for i in $(ls tc/*.o tf/*.o); do
	gcc $i -o $i.out -lm -lgfortran
	echo test ./$i.out
	./$i.out
done

%install
install -d %buildroot%_libdir
for i in *.so; do
	install -m644 $i.%sover %buildroot%_libdir/
	ln -s $i.%sover %buildroot%_libdir/$i
done

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc ../src/*
%_libdir/*.so

%changelog
* Thu Sep 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1-alt1
- Initial build for Sisyphus

