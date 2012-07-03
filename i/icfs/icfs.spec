Name: icfs
Version: 1.4
Release: alt8
Summary: An Incomplete Cholesky Factorization with Limited Memory
License: BSD
Group: Sciences/Mathematics
Url: http://www.mcs.anl.gov/~more/icfs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.mcs.anl.gov/~more/icfs/icfs-1.4.tar.gz

Requires: lib%name = %version-%release
BuildPreReq: gcc-fortran liblapack-goto-devel

%description
ICFS  is an incomplete Cholesky factorization for the solution of large-scale
trust region subproblems and positive definite systems of linear equations. This
factorization depends on a parameter p that specifies the amount of additional
memory that is available; there is no need to specify a drop tolerance.

Before use example program `icf', extract data files from archive:
`tar -xzf %_datadir/%name/tprobs.tar.gz'.

%package -n lib%name
Summary: Shared library of ICFS
Group: System/Libraries

%description -n lib%name
ICFS  is an incomplete Cholesky factorization for the solution of large-scale
trust region subproblems and positive definite systems of linear equations. This
factorization depends on a parameter p that specifies the amount of additional
memory that is available; there is no need to specify a drop tolerance.

This package contains shared library of ICFS.

%package -n lib%name-devel
Summary: Development files of ICFS
Group: Development/Other
Requires: libgfortran-devel lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
ICFS  is an incomplete Cholesky factorization for the solution of large-scale
trust region subproblems and positive definite systems of linear equations. This
factorization depends on a parameter p that specifies the amount of additional
memory that is available; there is no need to specify a drop tolerance.

This package contains development files of ICFS.

%package -n lib%name-devel-static
Summary: Static library of ICFS
Group: Development/Other
Requires: libgfortran-devel lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
ICFS  is an incomplete Cholesky factorization for the solution of large-scale
trust region subproblems and positive definite systems of linear equations. This
factorization depends on a parameter p that specifies the amount of additional
memory that is available; there is no need to specify a drop tolerance.

This package contains static library of ICFS.

%prep
%setup

%build
export ARCH=linux
%make install
./icf

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name
install -d %buildroot%_libdir

install -m755 icf src/utils/Fpp %buildroot%_bindir
mv driver.f icf.f
tar -czf tprobs.tar.gz tprobs
install -m644 tprobs.tar.gz icf.dat icf.linux \
	%buildroot%_datadir/%name

mkdir lib
pushd lib
ar x ../src/utils/*.a
cp ../src/icf/lib%name.a ./
ar r lib%name.a *.o
ranlib lib%name.a
rm -f *.o
ar x lib%name.a
install -m644 lib%name.a %buildroot%_libdir
f77 -shared  *.o -Wl,-soname,lib%name.so.0 \
	-o %buildroot%_libdir/lib%name.so.0.0.0 -llapack -lgoto2
ln -s lib%name.so.0.0.0 %buildroot%_libdir/lib%name.so.0
ln -s lib%name.so.0 %buildroot%_libdir/lib%name.so
rm -f *.o
popd

%files
%doc README icf.f
%_bindir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

#files -n lib%name-devel-static
#_libdir/*.a

%changelog
* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt8
- Disabled requirement of libatlas-devel for devel package

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt7
- Built with GotoBLAS instead of ATLAS
- Disable devel-static package

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt6
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt5
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt4
- Rebuilt for soname set-versions

* Wed Sep 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt3
- Added necessary symbols

* Mon Sep 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2
- Added shared library

* Wed Jun 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

