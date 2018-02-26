%define sonamever 0
%define sover %sonamever.0.0

Name: libitpack
Version: 1998
Release: alt4
Summary: Solving large sparse linear systems by accelerated iterative algorithms
License: Free
Group: Sciences/Mathematics
Url: http://rene.ma.utexas.edu/CNA/ITPACK/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-fortran libgfortran-devel-static /usr/bin/latex

%description
ITPACK, developed at the Center for Numerical Analysis, the University of Texas
at Austin, is a collection of subroutines for solving large sparse linear
systems by adaptive accelerated iterative algorithms.

%package devel
Summary: Developments files for ITPACK
Group: Development/Other
Requires: %name = %version-%release

%description devel
ITPACK, developed at the Center for Numerical Analysis, the University of Texas
at Austin, is a collection of subroutines for solving large sparse linear
systems by adaptive accelerated iterative algorithms.

This package contains developments files for ITPACK.

%package devel-static
Summary: Static libraries of ITPACK
Group: Development/Other

%description devel-static
ITPACK, developed at the Center for Numerical Analysis, the University of Texas
at Austin, is a collection of subroutines for solving large sparse linear
systems by adaptive accelerated iterative algorithms.

This package contains static libraries of ITPACK.

%package devel-doc
Summary: Documentation and test sources for ITPACK
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
ITPACK, developed at the Center for Numerical Analysis, the University of Texas
at Austin, is a collection of subroutines for solving large sparse linear
systems by adaptive accelerated iterative algorithms.

This package contains development documentation for ITPACK and test sources.

%package -n itpack-tests
Summary: Executable files for test ITPACK
Group: Sciences/Mathematics

%description -n itpack-tests
ITPACK, developed at the Center for Numerical Analysis, the University of Texas
at Austin, is a collection of subroutines for solving large sparse linear
systems by adaptive accelerated iterative algorithms.

This package contains executable files for test ITPACK.

%prep
%setup

%build
function buildIt() {
	f77 -g -pipe -O -Wall -c $1.f -o $1.o
	ar r %{name}_$2.a $1.o
	ranlib %{name}_$2.a
	f77 -g -pipe -O -Wall %optflags_shared -c $1.f -o $1-sh.o
	f77 -shared -Wl,-soname,%{name}_$2.so.%sonamever \
		-o %{name}_$2.so.%sover $1-sh.o -lm -lgfortran
}
buildIt src2c 2c
buildIt dsrc2c 2c_d
buildIt srcv2d v2d

function buildTest() {
	f77 -g -pipe -O -Wall -c $1.f -o $1.o
	f77 -o test-itpack_$2 $1.o -L. -litpack_$2 -lm -lgfortran
	./test-itpack_$2
}
buildTest tst2c 2c
buildTest dtst2c 2c_d
buildTest tstv2d v2d

for i in $(ls *.tex); do
	latex $i
done

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_docdir/%name
install -m755 test* %buildroot%_bindir
install -m644 *.so* %buildroot%_libdir
install -m644 *.a %buildroot%_libdir
install -m644 *.dvi *tst*.f %buildroot%_docdir/%name

pushd %buildroot%_libdir
for i in $(ls *.so.%sover|sed -e 's/\.%sover//'); do
	ln -s $i.%sonamever $i
done
popd

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so

%files devel-static
%_libdir/*.a

%files devel-doc
%_docdir/%name

%files -n itpack-tests
%_bindir/*

%changelog
* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1998-alt4
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1998-alt3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1998-alt2
- Rebuilt for soname set-versions

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1998-alt1
- Initial build for Sisyphus
