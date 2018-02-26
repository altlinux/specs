Name: y12m
Version: 1.0
Release: alt5
Summary: Solution of Large and Sparse Systems of Linear Algebraic Equations
License: Free
Group: Sciences/Mathematics
Url: http://www.netlib.org/y12m/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-fortran libgfortran-devel

%description
Y12m Solution of Large and Sparse Systems of Linear Algebraic Equations.

%package -n lib%name
Summary: Shared library of Y12m
Group: System/Libraries

%description -n lib%name
Y12m Solution of Large and Sparse Systems of Linear Algebraic Equations.

This package contains shared library of Y12m.

%package -n lib%name-devel
Summary: Development file of Y12m
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Y12m Solution of Large and Sparse Systems of Linear Algebraic Equations.

This package contains development file of Y12m.

%package -n lib%name-devel-static
Summary: Static library of Y12m
Group: Development/Other

%description -n lib%name-devel-static
Y12m Solution of Large and Sparse Systems of Linear Algebraic Equations.

This package contains static library of Y12m.

%prep
%setup

%build
%make_build
%make_build lib%name.so
pushd ex
f77 %optflags -c *.f
for i in maind maine mainf mainf2 test1 test2; do
	f77 -o %name-test-$i $i.o matr*.o -lgfortran -L.. -l%name
done
popd

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir

install -m755 ex/%name-test-* %buildroot%_bindir
install -m644 *.a *.so* %buildroot%_libdir
ln -s lib%name.so.1 %buildroot%_libdir/lib%name.so

rm -f ex/*.o ex/%name-test-*
mv ex examples

%files
%doc doc examples
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

#files -n lib%name-devel-static
#_libdir/*.a

%changelog
* Wed Mar 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5
- Added -g into compiler flags
- Disabled static library

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Rebuilt for debuginfo

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Rebuilt for soname set-versions

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Rebuild with PIC

* Thu May 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

