%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.3.0
Name: BlockSolve95
Version: 3.0
Release: alt10
Summary: Solving large sparse symmetric systems of linear equations
License: MIT
Group: Sciences/Mathematics
Url: http://ftp.mcs.anl.gov/pub/BlockSolve95
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://ftp.mcs.anl.gov/pub/BlockSolve95/BlockSolve95.tar.gz

Requires: lib%name = %version-%release
BuildPreReq: liblapack-devel libX11-devel
BuildPreReq: %mpiimpl-devel

%description
The BlockSolve95 package contains routines for solving large
sparse symmetric systems of linear equations on massively
parallel distributed memory systems and networks of workstations.

%package -n lib%name
Summary: Shared library of BlockSolve95
Group: System/Libraries
Provides: libblocksolve95 = %version-%release

%description -n lib%name
The BlockSolve95 package contains routines for solving large
sparse symmetric systems of linear equations on massively
parallel distributed memory systems and networks of workstations.

This package contains shared library of BlockSolve95.

%package -n lib%name-devel
Summary: Development files of BlockSolve95
Group: Development/Other
Provides: libblocksolve95-devel = %version-%release
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
The BlockSolve95 package contains routines for solving large
sparse symmetric systems of linear equations on massively
parallel distributed memory systems and networks of workstations.

This package contains development files of BlockSolve95.

%package -n lib%name-devel-static
Summary: Static library of BlockSolve95
Group: Development/Other
Provides: libblocksolve95-devel-static = %version-%release
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
The BlockSolve95 package contains routines for solving large
sparse symmetric systems of linear equations on massively
parallel distributed memory systems and networks of workstations.

This package contains static library of BlockSolve95.

%package -n lib%name-devel-doc
Summary: Development documentation for BlockSolve95
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-doc
The BlockSolve95 package contains routines for solving large
sparse symmetric systems of linear equations on massively
parallel distributed memory systems and networks of workstations.

This package contains development documentation for BlockSolve95.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %_sysconfdir/profile.d/mpi-selector.sh
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

for i in lib examples; do
	%make_build OMAKE=make BOPT=O ACTION=$i \
		PETSC_ARCH=linux PETSC_INCLUDE=$PWD/include \
		MPIDIR=%mpidir tree
done

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -d %buildroot%_man3dir
install -d %buildroot%_mandir/manh

install -m755 examples/grid?.linux %buildroot%_bindir
install -m644 lib/libO/linux/*.a %buildroot%_libdir
install -m644 include/* %buildroot%_includedir
install -p -m644 doc/man/man3/* %buildroot%_man3dir
install -p -m644 doc/man/manh/* %buildroot%_mandir/manh

install -d %buildroot%_docdir/lib%name-devel
install -p -m644 doc/manual/manual.ps \
	doc/manual/manual.dvi \
	include/README.include \
	%buildroot%_docdir/lib%name-devel

# shared libraries

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../libBS95.a
mpicc -shared * -llapack -lgoto2 \
	-Wl,-rpath,%mpidir/lib \
	-Wl,-soname,libBS95.so.%somver -o ../libBS95.so.%sover
rm -f *
popd
rmdir tmp
ln -s libBS95.so.%sover libBS95.so.%somver
ln -s libBS95.so.%somver libBS95.so
popd

%files
%doc doc/manual/grid?.ps doc/manual/crs.ps COPYRIGHT examples/README.examples
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%exclude %_includedir/README.include

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/lib%name-devel
%_man3dir/*
%_mandir/manh/*

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt10
- Rebuilt with OpenMPI 1.6

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt9
- Rebuilt with GotoBLAS2 1.13-alt3

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt8
- Built with GotoBLAS2 instead of ATLAS

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt7
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt6
- Rebuilt for debuginfo

* Fri Oct 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt5
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt4
- Fixed overlinking of libraries

* Sun Aug 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt3
- Added shared library
- Extracted development documentation into separate package

* Sat Jun 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt2
- Rebuild with optimization and PIC

* Wed May 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Initial build for Sisyphus

