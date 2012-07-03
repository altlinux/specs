%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.3.2
Name: plapack
Version: 3.2
Release: alt12
Summary: Parallel Linear Algebra Package (PLAPACK)
License: LGPL
Group: Sciences/Mathematics
Url: http://www.cs.utexas.edu/users/plapack/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.cs.utexas.edu/users/plapack/Downloads/PLAPACKR32.tar.gz
Source1: http://www.cs.utexas.edu/users/plapack/tutorial/tutorial_C.ps
Source2: http://www.cs.utexas.edu/users/plapack/tutorial/tutorial_FORTRAN.ps
Source3: LGPL

BuildPreReq: libsuperlu-devel %mpiimpl-devel
BuildPreReq: gcc-fortran liblapack-devel
BuildPreReq: libibumad-devel libibverbs-devel chrpath

%description
PLAPACK: High Performance through High Level Abstraction.

Coding parallel algorithms is generally regarded as a formidable task. To make
this task manageable in the arena of linear algebra algorithms, we have
developed the Parallel Linear Algebra Package (PLAPACK), an infrastructure for
coding such algorithms at a high level of abstraction. It is often believed that
by raising the level of abstraction in this fashion, performance is sacrificed.
Throughout, we have maintained that indeed there is a performance penalty, but
that by coding at a higher level of abstraction, more sophisticated algorithms
can be implemented, which allows high levels of performance to be regained.

This package contains also testing executables. Run this by executing the
command (by example):

  mpirun -np 4 NAME_OF_EXEC_FILE

%package -n lib%name
Summary: Shared library of PLAPACK
Group: System/Libraries

%description -n lib%name
PLAPACK: High Performance through High Level Abstraction.

Coding parallel algorithms is generally regarded as a formidable task. To make
this task manageable in the arena of linear algebra algorithms, we have
developed the Parallel Linear Algebra Package (PLAPACK), an infrastructure for
coding such algorithms at a high level of abstraction. It is often believed that
by raising the level of abstraction in this fashion, performance is sacrificed.
Throughout, we have maintained that indeed there is a performance penalty, but
that by coding at a higher level of abstraction, more sophisticated algorithms
can be implemented, which allows high levels of performance to be regained.

This package contains shared library of PLAPACK.

%package -n lib%name-devel
Summary: Development files for PLAPACK
Group: Development/Other
Requires: gcc-fortran
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
PLAPACK: High Performance through High Level Abstraction.

Coding parallel algorithms is generally regarded as a formidable task. To make
this task manageable in the arena of linear algebra algorithms, we have
developed the Parallel Linear Algebra Package (PLAPACK), an infrastructure for
coding such algorithms at a high level of abstraction. It is often believed that
by raising the level of abstraction in this fashion, performance is sacrificed.
Throughout, we have maintained that indeed there is a performance penalty, but
that by coding at a higher level of abstraction, more sophisticated algorithms
can be implemented, which allows high levels of performance to be regained.

This package contains development files of PLAPACK.

%package -n lib%name-devel-static
Summary: Static library of PLAPACK
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
PLAPACK: High Performance through High Level Abstraction.

Coding parallel algorithms is generally regarded as a formidable task. To make
this task manageable in the arena of linear algebra algorithms, we have
developed the Parallel Linear Algebra Package (PLAPACK), an infrastructure for
coding such algorithms at a high level of abstraction. It is often believed that
by raising the level of abstraction in this fashion, performance is sacrificed.
Throughout, we have maintained that indeed there is a performance penalty, but
that by coding at a higher level of abstraction, more sophisticated algorithms
can be implemented, which allows high levels of performance to be regained.

This package contains static library of PLAPACK.

%package doc
Summary: Documentation and examples for PLAPACK
Group: Development/Documentation
BuildArch: noarch

%description doc
PLAPACK: High Performance through High Level Abstraction.

Coding parallel algorithms is generally regarded as a formidable task. To make
this task manageable in the arena of linear algebra algorithms, we have
developed the Parallel Linear Algebra Package (PLAPACK), an infrastructure for
coding such algorithms at a high level of abstraction. It is often believed that
by raising the level of abstraction in this fashion, performance is sacrificed.
Throughout, we have maintained that indeed there is a performance penalty, but
that by coding at a higher level of abstraction, more sophisticated algorithms
can be implemented, which allows high levels of performance to be regained.

This package contains development documentation and examples for PLAPACK.

%prep
%setup
install %SOURCE3 .

sed -i 's|\(\-O3\)|\1 -g|' \
	$(find ./ -name 'Make.include*' -type f)

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

rm -f $(find ./ -name '*.o')
export LIBDIR=%_libdir
export HOME=$(pwd)
export MPIDIR=%mpidir
%make_build

# examples

for dir in Cholesky FORTRAN LINPACK LU QR; do
	pushd EXAMPLES/$dir
	%make_build
	popd
done

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

rm -f $(find ./ -name '*.o') EXAMPLES/Makefile
mv EXAMPLES/FORTRAN/LU_driver.x EXAMPLES/FORTRAN/LU_driver_FORTRAN.x
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name
install -d %buildroot%_docdir/%name/examples
install -m644 *.a %buildroot%_libdir
install -m755 $(find EXAMPLES -name '*.x') %buildroot%_bindir
rm -f $(find EXAMPLES -name '*.x')
cp -fR EXAMPLES/* %buildroot%_docdir/%name/examples/
install -p -m644 $(find ./ -name '*.h') %buildroot%_includedir/%name
install -m644 %SOURCE1 %SOURCE2 %buildroot%_docdir/%name

#for i in %buildroot%_bindir/*
#do
#	chrpath -r %mpidir/lib $i ||:
#done

# shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../libPLAPACK.a
mpif77 -shared * -llapack -lgoto2 \
	-Wl,-R%mpidir/lib \
	-Wl,-soname,libPLAPACK.so.%somver -o ../libPLAPACK.so.%sover
rm -f *
popd
rmdir tmp
ln -s libPLAPACK.so.%sover libPLAPACK.so.%somver
ln -s libPLAPACK.so.%somver libPLAPACK.so
#chrpath -r %mpidir/lib libPLAPACK.so
popd

%files
%doc header GNU_license LGPL
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files doc
%_docdir/%name

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt12
- Rebuilt with OpenMPI 1.6

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt11
- Minimized runtime requirements for devel package

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt10
- Rebuilt with GotoBLAS2 1.13-alt3

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt9
- Built with GotoBLAS2 instead of ATLAS
- Disabled static package

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt8
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt7
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt6
- Rebuilt for soname set-versions

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt5
- Fixed overlinking

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt4
- Rebuilt with SuperLU 4.0

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt3
- Removed requirement on static libraries of OpenMPI

* Wed Sep 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt2
- Set doc package as noarch

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1
- Added shared library

* Tue Jun 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt4
- Rebuild with PIC

* Sat Jun 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt3
- Resolved declaration conflict with stdlib.h
- Added declarations in headers for client software

* Thu May 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt2
- Rebuild with OpenMPI

* Thu Apr 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Initial build for Sisyphus

