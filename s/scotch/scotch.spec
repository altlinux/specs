%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define sover 0
Name: scotch
Version: 5.1.12b
Release: alt3.svn20110910
Summary: Package and libraries for sequential and parallel graph partitioning
License: CeCILL-C
Group: Sciences/Mathematics
Url: http://www.labri.fr/perso/pelegrin/scotch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://scm.gforge.inria.fr/svn/scotch
Source: %{name}_%version.tar.gz
Source1: %{name}_%{version}_esmumps.tar.gz
Source2: Makefile.inc
Source3: Makefile.inc.esmumps
Source4: %name.pc

BuildPreReq: gcc-fortran libgfortran-devel bison flex chrpath
BUildPreReq: libibverbs-devel libibumad-devel zlib-devel
BuildPreReq: glibc-devel %mpiimpl-devel

%description
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

%package -n lib%name
Summary: Shared libraries of Scotch
Group: System/Libraries

%description -n lib%name
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains shared libraries of Scotch.

%package -n lib%name-devel
Summary: Development files of Scotch
Group: Development/Other
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains development files of Scotch.

%package -n lib%name-devel-static
Summary: Static libraries of Scotch
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains static libraries of Scotch.

%package -n lib%name-devel-doc
Summary: Development documentation and example source code for Scotch
Group: Development/Other
BuildArch: noarch

%description -n lib%name-devel-doc
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains development documentation and example source code
for Scotch.

%package data
Summary: grf files for Scotch
Group: Development/Other
BuildArch: noarch

%description data
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains GRF and TGT files for Scotch.

%prep
%setup
tar -xzf %SOURCE1
install -m644 %SOURCE2 %SOURCE3 %SOURCE4 .

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" %name.pc

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

pushd src
export MPIDIR=%mpidir
export datarootdir=%_datadir
ln -s ../Makefile.inc .
%make_build
%make_build ptscotch
popd

pushd esmumps/src
ln -s ../../Makefile.inc.esmumps Makefile.inc
%make_build
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

pushd src
install -d %buildroot%_bindir
install -d %buildroot%_includedir
install -d %buildroot%_libdir
install -d %buildroot%_pkgconfigdir
install -d %buildroot%_man1dir
install -d %buildroot%_docdir/%name
install -d %buildroot%_datadir/%name/grf
install -d %buildroot%_datadir/%name/tgt
%makeinstall
popd
install esmumps/src/esmumps/main_esmumps %buildroot%_bindir
install esmumps/lib/libesmumps.a %buildroot%_libdir

pushd examples
mpif77 -g -I../src/libscotch -c scotch_example_1.f -o scotch_example_1.o
mpif77 -o scotch_example_1 scotch_example_1.o -Wl,-R%_libdir/%mpiimpl/lib \
	-L../lib -lscotchmetis -lscotcherrexit -lscotch -lscotcherr
install -m755 scotch_example_1 %buildroot%_bindir
install -p -m644 ../doc/ptscotch_user5.1.pdf ../doc/scotch_user5.1.pdf \
	scotch_example_1.f \
	%buildroot%_docdir/%name
popd

install -p -m644 grf/* %buildroot%_datadir/%name/grf
install -p -m644 esmumps/tgt/* %buildroot%_datadir/%name/tgt
install -p -m644 esmumps/src/esmumps/esmumps.h %buildroot%_includedir

%ifarch x86_64
install -m644 lib/* %buildroot%_libdir
%endif

sed -i 's|@VERSION@|%version|' %name.pc
install -m644 %name.pc %buildroot%_pkgconfigdir

# shared libraries

pushd %buildroot%_libdir
for i in $(ls *.a|sed 's|\.a||'); do
	case $i in
		libscotcherr)
			ADDLIB=
			;;
		libscotch)
			ADDLIB="-lscotcherr -lpthread"
			;;
		libptscotchparmetis)
			ADDLIB="-lptscotch -lscotch -lscotcherr"
			;;
		libptscotch)
			ADDLIB="-lscotch -lscotcherr -lpthread"
			;;
		*)
			ADDLIB="-lscotch -lscotcherr"
			;;
	esac
	ar x $i.a
	mpicc -shared *.o -L. $ADDLIB -lz -lm -lrt \
		-Wl,-R%mpidir/lib \
		-Wl,-soname,$i.so.%sover -o $i.so.%sover
	ln -s $i.so.%sover $i.so
	chrpath -r %mpidir/lib $i.so
	rm -f *.o
done
popd

%files
%doc LICENSE_en.txt doc/CeCILL-C_V1-en.txt
%_bindir/*
%_man1dir/*
%dir %_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/%name

%files data
%dir %_datadir/%name
%_datadir/%name/grf
%_datadir/%name/tgt

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.12b-alt3.svn20110910
- Rebuilt with OpenMPI 1.6

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.12b-alt2.svn20110910
- Fixed build (thnx glebfm@)

* Sun Dec 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.12b-alt1.svn20110910
- Version 5.1.12b

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt2.svn20101209
- Fixed RPATH

* Fri May 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt1.svn20101209
- New snapshot
- Disabled devel-static package

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt1.svn20101007.2
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt1.svn20101007.1
- Rebuilt for debuginfo

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt1.svn20101007
- Version 5.1.10

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.6-alt1.svn20090513.1
- Fixed linking of libraries

* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.6-alt1.svn20090513
- New snapshot

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.6-alt1
- Version 5.1.6

* Fri Aug 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt5.svn20090828
- New snapshot
- Fixed manpages
- Added shared libraries

* Tue Aug 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt4.2
- Removed scotch-metis libraries from pkg-config file

* Mon Aug 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt4.1
- Fixed pkg-config file for esmumps

* Sun Aug 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt4
- Added pkg-config file
- Fixed:
    + breaking strict-aliasing rules
    + format not a string literal and no format arguments

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt3
- Rebuild with PIC

* Wed May 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt2
- Rebuild with gcc 4.4 and OpenMPI
- Disable static build for executables
- Fix for x86_64

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt1
- Initial build for Sisyphus

