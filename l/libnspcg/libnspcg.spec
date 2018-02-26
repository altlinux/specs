%define sonamever 0
%define sover %sonamever.0.0

Name: libnspcg
Version: 2008
Release: alt4
Summary: NonSymmetric Preconditioned Conjugate Gradient
License: Free
Group: Sciences/Mathematics
Url: http://rene.ma.utexas.edu/CNA/NSPCG/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-fortran libgfortran-devel-static /usr/bin/latex

%description
NSPCG (for NonSymmetric Preconditioned Conjugate Gradient) is a wide collection
of subroutines for solving large sparse linear systems using iterative
algorithms. with a selection of many more preconditioners, accelerators, and
data formats. It contains all of the ITPACK subroutines.

%package devel
Summary: Developments files for NSPCG
Group: Development/Other
Requires: %name = %version-%release

%description devel
NSPCG (for NonSymmetric Preconditioned Conjugate Gradient) is a wide collection
of subroutines for solving large sparse linear systems using iterative
algorithms. with a selection of many more preconditioners, accelerators, and
data formats. It contains all of the ITPACK subroutines.

This package contains developments files for NSPCG.

%package devel-static
Summary: Static library of NSPCG
Group: Development/Other

%description devel-static
NSPCG (for NonSymmetric Preconditioned Conjugate Gradient) is a wide collection
of subroutines for solving large sparse linear systems using iterative
algorithms. with a selection of many more preconditioners, accelerators, and
data formats. It contains all of the ITPACK subroutines.

This package contains static library of NSPCG.

%package devel-doc
Summary: Documentation and test sources for NSPGC
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
NSPCG (for NonSymmetric Preconditioned Conjugate Gradient) is a wide collection
of subroutines for solving large sparse linear systems using iterative
algorithms. with a selection of many more preconditioners, accelerators, and
data formats. It contains all of the ITPACK subroutines.

This package contains development documentation for NSPCG and test sources.

%package -n nspcg-tests
Summary: Executable files for test NSPCG
Group: Sciences/Mathematics

%description -n nspcg-tests
NSPCG (for NonSymmetric Preconditioned Conjugate Gradient) is a wide collection
of subroutines for solving large sparse linear systems using iterative
algorithms. with a selection of many more preconditioners, accelerators, and
data formats. It contains all of the ITPACK subroutines.

This package contains executable files for test NSPCG.

%prep
%setup

%build
f77 -pipe -g -O -Wall -c nspcg*.f
ar rcv %name.a nspcg*.o
ranlib %name.a
rm -f *.o

f77 -pipe -g -O -Wall %optflags_shared -c nspcg*.f
f77 -shared -Wl,-soname,%name.so.%sonamever \
	-o %name.so.%sover *.o -lm -lgfortran
rm -f *.o

for i in 1 2 3 4; do
	f77 -g -O tstnsp$i.f -L. -lnspcg -o test${i}_nspcg
	./test${i}_nspcg
done

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
install -m644 *.dvi tst*.f %buildroot%_docdir/%name

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

%files -n nspcg-tests
%doc tst*.f
%_bindir/*

%changelog
* Sat Mar 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2008-alt4
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2008-alt3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2008-alt2
- Rebuilt for soname set-versions

* Sun Apr 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2008-alt1
- Initial build for Sisyphus
