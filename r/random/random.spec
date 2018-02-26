%define somver 0
%define sover %somver.0.0

Name: random
Version: 20080825
Release: alt3
Summary: Fortran-90 pseudo-random number generator
License: BSD
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~dhbailey/mpdist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://crd.lbl.gov/~dhbailey/mpdist/random-20080825.tar.gz
Source1: http://crd.lbl.gov/~dhbailey/mpdist/BSD-LBNL-License.doc

BuildPreReq: gcc-fortran libgfortran-devel-static

%description
RANDOM (Fortran-90 pseudo-random number generator based on provably normal
number theory), based on the recently discovered class of provably normal
numbers -- see paper "Random Generators and Normal Numbers", by DHB and Richard
Crandall, in the papers directory. In particular, subroutine bcnrand generates a
sequence of IEEE 64-bit floating-point numbers uniformly in (0,1), with period
(if parameters are properly selected) = 2x3^32 = 3.7060404e15. It is completely
self-contained -- the required double-double arithmetic subroutines are included
in the Fortran-90 source file. The bcnrand routine is designed for simple
parallelization, yielding the same overall sequence as with a one-processor
program. Also included here is a memory-testing program based on the bcnrand
generator. 

%package -n lib%name
Summary: Shared libraries of RANDOM
Group: System/Libraries

%description -n lib%name
RANDOM (Fortran-90 pseudo-random number generator based on provably normal
number theory), based on the recently discovered class of provably normal
numbers -- see paper "Random Generators and Normal Numbers", by DHB and Richard
Crandall, in the papers directory. In particular, subroutine bcnrand generates a
sequence of IEEE 64-bit floating-point numbers uniformly in (0,1), with period
(if parameters are properly selected) = 2x3^32 = 3.7060404e15. It is completely
self-contained -- the required double-double arithmetic subroutines are included
in the Fortran-90 source file. The bcnrand routine is designed for simple
parallelization, yielding the same overall sequence as with a one-processor
program. Also included here is a memory-testing program based on the bcnrand
generator. 

This package contains shared libraries of RANDOM.

%package -n lib%name-devel
Summary: Development files of RANDOM
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
RANDOM (Fortran-90 pseudo-random number generator based on provably normal
number theory), based on the recently discovered class of provably normal
numbers -- see paper "Random Generators and Normal Numbers", by DHB and Richard
Crandall, in the papers directory. In particular, subroutine bcnrand generates a
sequence of IEEE 64-bit floating-point numbers uniformly in (0,1), with period
(if parameters are properly selected) = 2x3^32 = 3.7060404e15. It is completely
self-contained -- the required double-double arithmetic subroutines are included
in the Fortran-90 source file. The bcnrand routine is designed for simple
parallelization, yielding the same overall sequence as with a one-processor
program. Also included here is a memory-testing program based on the bcnrand
generator. 

This package contains development files of RANDOM.

%package -n lib%name-devel-static
Summary: Static libraries of RANDOM
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
RANDOM (Fortran-90 pseudo-random number generator based on provably normal
number theory), based on the recently discovered class of provably normal
numbers -- see paper "Random Generators and Normal Numbers", by DHB and Richard
Crandall, in the papers directory. In particular, subroutine bcnrand generates a
sequence of IEEE 64-bit floating-point numbers uniformly in (0,1), with period
(if parameters are properly selected) = 2x3^32 = 3.7060404e15. It is completely
self-contained -- the required double-double arithmetic subroutines are included
in the Fortran-90 source file. The bcnrand routine is designed for simple
parallelization, yielding the same overall sequence as with a one-processor
program. Also included here is a memory-testing program based on the bcnrand
generator. 

This package contains static libraries of RANDOM.

%prep
%setup
install -m644 %SOURCE1 .

%build
mkdir orig
cp *.f90 orig/
mv memtest.f90 bcn_memtest.f90
cp bcnrand.f90 lbcnrand.f90
cp bcnrandx.f90 lbcnrandx.f90
sed -i -e '56,$d' bcnrand.f90
sed -i -e '89,$d' bcnrandx.f90
sed -i -e '123,$d' lbcnrandx.f90
sed -i -e '1,93d' lbcnrandx.f90
sed -i -e '123rlbcnrandx.f90' lbcnrand.f90
rm -f lbcnrandx.f90
sed -i -e '1,61d' lbcnrand.f90
sed -i -e '50,$d' bcn_memtest.f90

f95 %optflags %optflags %optflags_shared -c *.f90
ar r libbcnrand.a lbcnrand.o
ranlib libbcnrand.a

for i in libbcnrand; do
	f95 -shared -Wl,--whole-archive $i.a -Wl,--no-whole-archive \
		-o $i.so.%sover -Wl,-soname=$i.so.%somver -Wl,-z,defs
	ln -s $i.so.%sover $i.so.%somver
	ln -s $i.so.%somver $i.so
done

export LD_LIBRARY_PATH=$PWD
for i in bcnrand bcnrandx bcn_memtest
do
	f95 $i.o -o $i -L. -lbcnrand
done

./bcnrand
echo
./bcnrandx

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir

install -m755 bcnrand bcnrandx bcn_memtest %buildroot%_bindir
cp -P *.a *.so* %buildroot%_libdir

%files
%doc *.doc
%_bindir/*

%files -n lib%name
%doc orig/*.f90
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20080825-alt3
- Rebuilt for debuginfo

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20080825-alt2
- Added shared libraries

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20080825-alt1
- Initial build for Sisyphus

