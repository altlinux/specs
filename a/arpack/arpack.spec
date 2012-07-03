%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: arpack
Version: 96
Release: alt10
Summary: Fortran77 subroutines designed to solve large scale eigenvalue problems
License: BSD
Group: Sciences/Mathematics
Url: http://www.caam.rice.edu/software/ARPACK/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.caam.rice.edu/software/ARPACK/SRC/arpack96.tar.gz
Source1: http://www.caam.rice.edu/software/ARPACK/SRC/patch.tar.gz
Source2: http://www.caam.rice.edu/software/ARPACK/SRC/parpack96.tar.gz
Source3: http://www.caam.rice.edu/software/ARPACK/SRC/ppatch.tar.gz
Source4: http://www.caam.rice.edu/software/ARPACK/SRC/readme.arpack
Source5: http://www.caam.rice.edu/software/ARPACK/SRC/readme.parpack
Source6: ARmake.inc
Source7: dnaupc.f
Source8: dneupc.f
Source9: http://www.caam.rice.edu/software/ARPACK/CONTRIBUTED/chkpnt.tar.gz

Requires: %name-doc = %version-%release

BuildPreReq: gcc-fortran libblacs-devel %mpiimpl-devel libscalapack-devel
BuildPreReq: libarpack-devel chrpath

%description
ARPACK is a collection of Fortran77 subroutines designed to solve large
scale eigenvalue problems.

PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

In addition this package contains executable file for periodicly save the state
during an ARPACK run.

%package doc
Summary: Documentation for ARPACK
Group: Development/Documentation
BuildArch: noarch

%description doc
ARPACK is a collection of Fortran77 subroutines designed to solve large
scale eigenvalue problems.

This package contains a documentation for ARPACK.

%package -n lib%name
Summary: Shared libraries of ARPACK
Group: System/Libraries

%description -n lib%name
ARPACK is a collection of Fortran77 subroutines designed to solve large
scale eigenvalue problems.

This package contains shared libraries of ARPACK.

%package -n lib%name-devel
Summary: Development files of ARPACK
Group: Development/Other
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
ARPACK is a collection of Fortran77 subroutines designed to solve large
scale eigenvalue problems.

This package contains development files of ARPACK.

%package -n lib%name-devel-static
Summary: Static libraries of ARPACK
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
ARPACK is a collection of Fortran77 subroutines designed to solve large
scale eigenvalue problems.

This package contains static libraries of ARPACK.

%package examples
Summary: Example executables of ARPACK
Group: Sciences/Mathematics

%description examples
ARPACK is a collection of Fortran77 subroutines designed to solve large
scale eigenvalue problems.

This package contains example executables of ARPACK.

%package examples-sources
Summary: Example sources of ARPACK
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release

%description examples-sources
ARPACK is a collection of Fortran77 subroutines designed to solve large
scale eigenvalue problems.

This package contains example sources of ARPACK.

%package -n p%name-blacs-examples
Summary: Example executables of PARPACK using BLACS
Group: Sciences/Mathematics

%description -n p%name-blacs-examples
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains example executables of PARPACK using BLACS.

%package -n p%name-blacs-examples-sources
Summary: Example sources of PARPACK using BLACS
Group: Development/Other
BuildArch: noarch
Requires: libp%name-blacs-devel = %version-%release

%description -n p%name-blacs-examples-sources
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains example sources of PARPACK using BLACS.

%package -n p%name-mpi-examples
Summary: Example executables of PARPACK using MPI
Group: Sciences/Mathematics

%description -n p%name-mpi-examples
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains example executables of PARPACK using MPI.

%package -n p%name-mpi-examples-sources
Summary: Example sources of PARPACK using MPI
Group: Development/Other
BuildArch: noarch
Requires: libp%name-mpi-devel = %version-%release

%description -n p%name-mpi-examples-sources
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains example sources of PARPACK using MPI.

%package -n libp%name-blacs
Summary: Shared libraries of Parallel ARPACK with BLACS support
Group: System/Libraries

%description -n libp%name-blacs
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains shared libraries of PARPACK with BLACS support.

%package -n libp%name-blacs-devel
Summary: Parallel ARPACK package with development files with BLACS support
Group: Development/Other
Requires: libp%name-blacs = %version-%release
Conflicts: libp%name-blacs-devel < %version-%release
Obsoletes: libp%name-blacs-devel < %version-%release

%description -n libp%name-blacs-devel
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains development files of PARPACK with BLACS support.

%package -n libp%name-blacs-devel-static
Summary: Static libraries of Parallel ARPACK package with BLACS support
Group: Development/Other
Requires: libp%name-blacs-devel = %version-%release
Requires: lib%name-devel = %version-%release
Conflicts: libp%name-blacs-devel < %version-%release

%description -n libp%name-blacs-devel-static
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains development files of PARPACK with BLACS support.

%package -n libp%name-mpi
Summary: Shared libraries of Parallel ARPACK package with MPI support
Group: System/Libraries

%description -n libp%name-mpi
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains shared libraries of PARPACK with MPI support.

%package -n libp%name-mpi-devel
Summary: Parallel ARPACK package with development files with MPI support
Group: Development/Other
Requires: libp%name-mpi = %version-%release
Conflicts: libp%name-mpi-devel < %version-%release
Obsoletes: libp%name-mpi-devel < %version-%release

%description -n libp%name-mpi-devel
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains development files of PARPACK with MPI support.

%package -n libp%name-mpi-devel-static
Summary: Static libraries of Parallel ARPACK package with MPI support
Group: Development/Other
Requires: libp%name-mpi-devel = %version-%release
Requires: lib%name-devel = %version-%release
Conflicts: libp%name-mpi-devel < %version-%release

%description -n libp%name-mpi-devel-static
PARPACK (Parallel ARPACK) is an extension of the ARPACK software package
used for solving large scale eigenvalue problems on distributed memory
parallel architectures.  The message passing layers currently supported
are BLACS and MPI.

This package contains static libraries of PARPACK with MPI support.

%prep
%setup -c ARPACK
tar -xzf %SOURCE1
tar -xzf %SOURCE2
tar -xzf %SOURCE3
tar -xzf %SOURCE9
install -m644 %SOURCE4 %SOURCE5 %SOURCE6 ARPACK
install -m644 %SOURCE7 %SOURCE8 ARPACK/SRC

sed -i -e 's/(OPTFLAGS)/%optflags %optflags_shared/' ARPACK/ARmake.inc

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

mkdir -p Carley
cp -fR ARPACK/* Carley/
mv Checkpoint ARPACK/

sed -i "s|\$(HOME)|$PWD/ARPACK|" ARPACK/ARmake.inc
sed -i "s|\$(HOME)|$PWD/Carley|" Carley/ARmake.inc

cd ARPACK
pushd EXAMPLES
find ./ -type f >> ../%name.examples
popd
pushd PARPACK/EXAMPLES
find ./ -type f >> ../../p%name.examples
popd

export bindir=%_bindir
export libdir=%_libdir
export libexecdir=%_libdir
export mpidir=%mpidir
%make all
pushd EXAMPLES
%make all
popd
pushd PARPACK/EXAMPLES/BLACS
%make all
popd
mv lib%{name}_LINUX.a lib%{name}_LINUX.a.bak
%make clean
sed -i \
	-e '40s/BLACS/MPI/' \
	ARmake.inc
%make all
pushd PARPACK/EXAMPLES/MPI
%make all
popd

# Checkpoint
pushd Checkpoint
%make dssave
popd

# for Cayley transformation mode
cd ../Carley
sed -i -e 's/dnaupd/dnaupc/' -e 's/dneupd/dneupc/' SRC/Makefile
%make all
mv lib%{name}_LINUX.a lib%{name}_LINUX.a.bak
%make clean
sed -i \
	-e '40s/BLACS/MPI/' \
	ARmake.inc
%make all
mv lib%{name}_LINUX.a lib%{name}_LINUX_Carley.a
mv p%{name}_BLACS-LINUX.a p%{name}_BLACS-LINUX_Carley.a
mv p%{name}_MPI-LINUX.a p%{name}_MPI-LINUX_Carley.a

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

cd ARPACK

install -d %buildroot%_bindir
install -m755 Checkpoint/dssave %buildroot%_bindir

# libraries

install -d %buildroot%_libdir
install -m644 *.a ../Carley/*.a %buildroot%_libdir
pushd %buildroot%_libdir
for i in $(ls p*.a); do
	ln -s $i lib$i
done

function makeShared() {
	ar x $2.a
	$1 -shared -Wl,-R$3 *.o -lscalapack -lblacs \
		-Wl,-soname,$2.so.%version -o $2.so.%version $4 $5
	ln -s $2.so.%version $2.so
	rm -f *.o
}

for i in $(ls libarpack_LINUX*.a|sed 's|\.a||')
do
	makeShared f77 $i %_libdir
	chrpath -d $i.so
done
for i in $(ls libparpack_*-LINUX*.a|sed 's|\.a||')
do
	makeShared mpif77 $i %mpidir/lib -L%buildroot%_libdir -larpack_LINUX
	chrpath -r %mpidir/lib $i.so
done
popd
install -d %buildroot%_bindir

# headers

install -d %buildroot%_includedir/%name/MPI
install -d %buildroot%_includedir/%name/BLACS
install -m644 SRC/*.h %buildroot%_includedir/%name
install -m644 PARPACK/SRC/MPI/*.h %buildroot%_includedir/%name/MPI
install -m644 PARPACK/SRC/BLACS/*.h %buildroot%_includedir/%name/BLACS

# ARPACK examples

pushd EXAMPLES/BAND
for i in $(ls ??bdr?); do
	install -m755 $i %buildroot%_bindir/%{name}_$i
done
popd
pushd EXAMPLES/SIMPLE
for i in $(ls ??simp); do
	install -m755 $i %buildroot%_bindir/%{name}_$i
done
popd
pushd EXAMPLES/SVD
for i in $(ls ?svd); do
	install -m755 $i %buildroot%_bindir/%{name}_$i
done
popd
for dir in EXAMPLES/COMPLEX EXAMPLES/NONSYM EXAMPLES/SYM
do
	pushd $dir
	for i in $(ls ??drv?); do
		install -m755 $i %buildroot%_bindir/%{name}_$i
	done
	popd
done

# P-ARPACK examples

for dir in BLACS MPI; do
	pushd PARPACK/EXAMPLES/$dir
	for i in $(ls p??drv?_LINUX); do
		install -m755 $i %buildroot%_bindir/p%{name}_${dir}_$i
	done
	popd
done

# ARPACK example sources

for dir in BAND COMPLEX NONSYM SIMPLE SVD SYM
do
	install -d %buildroot%_datadir/%name/examples/$dir
done
pushd EXAMPLES
for i in $(cat ../%name.examples); do
	if [ $i != Makefile ]; then
		install -m644 $i %buildroot%_datadir/%name/examples/$i
	fi
done
popd

# PARPACK example sources

install -d %buildroot%_datadir/%name/examples/BLACS
install -d %buildroot%_datadir/%name/examples/MPI
pushd PARPACK/EXAMPLES
for i in $(cat ../../p%name.examples); do
	install -m644 $i %buildroot%_datadir/%name/examples/$i
done
popd

for i in %buildroot%_bindir/*
do
	chrpath -r %mpidir/lib $i ||:
done

%files
%_bindir/dssave

%files doc
%doc ARPACK/readme.*%{name} ARPACK/DOCUMENTS/*

%files -n lib%name
%_libdir/lib%{name}_LINUX.so.*
%_libdir/lib%{name}_LINUX_Carley.so.*

%files -n lib%name-devel
%_libdir/lib%{name}_LINUX.so
%_libdir/lib%{name}_LINUX_Carley.so
%_includedir/%name
%exclude %_includedir/%name/BLACS
%exclude %_includedir/%name/MPI

#files -n lib%name-devel-static
#_libdir/lib%{name}_LINUX.a
#_libdir/lib%{name}_LINUX_Carley.a

%files examples
%_bindir/%{name}_*

%files examples-sources
%_datadir/%name
%exclude %_datadir/%name/examples/MPI
%exclude %_datadir/%name/examples/BLACS

%files -n p%name-blacs-examples
%_bindir/p%{name}_BLACS_*

%files -n p%name-blacs-examples-sources
%_datadir/%name/examples/BLACS

%files -n p%name-mpi-examples
%_bindir/p%{name}_MPI_*

%files -n p%name-mpi-examples-sources
%_datadir/%name/examples/MPI

%files -n libp%name-blacs
%_libdir/libp%{name}_BLACS-LINUX.so.*
%_libdir/libp%{name}_BLACS-LINUX_Carley.so.*

%files -n libp%name-blacs-devel
%_libdir/libp%{name}_BLACS-LINUX.so
%_libdir/libp%{name}_BLACS-LINUX_Carley.so
%_includedir/%name/BLACS

#files -n libp%name-blacs-devel-static
#_libdir/p%{name}_BLACS-LINUX.a
#_libdir/libp%{name}_BLACS-LINUX.a
#_libdir/p%{name}_BLACS-LINUX_Carley.a
#_libdir/libp%{name}_BLACS-LINUX_Carley.a

%files -n libp%name-mpi
%_libdir/libp%{name}_MPI-LINUX.so.*
%_libdir/libp%{name}_MPI-LINUX_Carley.so.*

%files -n libp%name-mpi-devel
%_libdir/libp%{name}_MPI-LINUX.so
%_libdir/libp%{name}_MPI-LINUX_Carley.so
%_includedir/%name/MPI

#files -n libp%name-mpi-devel-static
#_libdir/p%{name}_MPI-LINUX.a
#_libdir/libp%{name}_MPI-LINUX.a
#_libdir/p%{name}_MPI-LINUX_Carley.a
#_libdir/libp%{name}_MPI-LINUX_Carley.a

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt10
- Rebuilt with OpenMPI 1.6

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt9
- Fixed RPATH
- Disabled devel-static packages

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt8
- Rebuilt for debuginfo

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt7
- Fixed linking of libraries

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt6.1
- Changed requirement: libscalapack-full -> libscalapack

* Wed Aug 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt6
- Added shared libraries (bootstrap for ScaLAPACK)

* Sun Jul 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt5
- Added library links (NAME -> libNAME)

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt4
- Rebuild with PIC

* Thu May 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt3
- Rebuild with OpenMPI

* Sat Apr 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt2
- Add the Cayley transformation mode with ARPACK
- Add executable file for periodicly save the state during an ARPACK run

* Sun Apr 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 96-alt1
- Initial build for Sisyphus

