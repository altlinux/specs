%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.5.8
Name: dsdp
Version: 5.8
Release: alt11
Summary: Implementation of an interior-point method for semidefinite programming
License: BSD-like
Group: Sciences/Mathematics
Url: http://www.mcs.anl.gov/hs/software/DSDP/

Source: http://www.mcs.anl.gov/hs/software/DSDP/DSDP5.8.tar.gz

BuildPreReq: liblapack-devel libscalapack-devel
BuildPreReq: %mpiimpl-devel unzip pblas-devel libplapack-devel

%description
The DSDP software is a free open source implementation of an interior-point
method for semidefinite programming. It provides primal and dual solutions,
exploits low-rank structure and sparsity in the data, and has relatively low
memory requirements for an interior-point method. It allows feasible and
infeasible starting points and provides approximate certificates of
infeasibility when no feasible solution exists. The dual-scaling algorithm
implemented in this package has a convergence proof and worst-case polynomial
complexity under mild assumptions on the data. The software can be used as a set
of subroutines, or by reading and writing to data files. Furthermore, the solver
offers scalable parallel performance for large problems and a well documented
interface.

%package doc
Summary: Documentation for DSDP
Group: Documentation
BuildArch: noarch

%description doc
The DSDP software is a free open source implementation of an interior-point
method for semidefinite programming. It provides primal and dual solutions,
exploits low-rank structure and sparsity in the data, and has relatively low
memory requirements for an interior-point method. It allows feasible and
infeasible starting points and provides approximate certificates of
infeasibility when no feasible solution exists. The dual-scaling algorithm
implemented in this package has a convergence proof and worst-case polynomial
complexity under mild assumptions on the data. The software can be used as a set
of subroutines, or by reading and writing to data files. Furthermore, the solver
offers scalable parallel performance for large problems and a well documented
interface.

This package contains documentation for DSDP.

%package -n lib%name
Summary: Shared library of DSDP
Group: System/Libraries

%description -n lib%name
The DSDP software is a free open source implementation of an interior-point
method for semidefinite programming. It provides primal and dual solutions,
exploits low-rank structure and sparsity in the data, and has relatively low
memory requirements for an interior-point method. It allows feasible and
infeasible starting points and provides approximate certificates of
infeasibility when no feasible solution exists. The dual-scaling algorithm
implemented in this package has a convergence proof and worst-case polynomial
complexity under mild assumptions on the data. The software can be used as a set
of subroutines, or by reading and writing to data files. Furthermore, the solver
offers scalable parallel performance for large problems and a well documented
interface.

This package contains shared library of DSDP.

%package -n lib%name-devel
Summary: Development files of DSDP
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
The DSDP software is a free open source implementation of an interior-point
method for semidefinite programming. It provides primal and dual solutions,
exploits low-rank structure and sparsity in the data, and has relatively low
memory requirements for an interior-point method. It allows feasible and
infeasible starting points and provides approximate certificates of
infeasibility when no feasible solution exists. The dual-scaling algorithm
implemented in this package has a convergence proof and worst-case polynomial
complexity under mild assumptions on the data. The software can be used as a set
of subroutines, or by reading and writing to data files. Furthermore, the solver
offers scalable parallel performance for large problems and a well documented
interface.

This package contains development files of DSDP.

%package -n lib%name-devel-doc
Summary: Development documentation for DSDP
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The DSDP software is a free open source implementation of an interior-point
method for semidefinite programming. It provides primal and dual solutions,
exploits low-rank structure and sparsity in the data, and has relatively low
memory requirements for an interior-point method. It allows feasible and
infeasible starting points and provides approximate certificates of
infeasibility when no feasible solution exists. The dual-scaling algorithm
implemented in this package has a convergence proof and worst-case polynomial
complexity under mild assumptions on the data. The software can be used as a set
of subroutines, or by reading and writing to data files. Furthermore, the solver
offers scalable parallel performance for large problems and a well documented
interface.

This package contains development documentation for DSDP.

%prep
%setup
rm -f $(find ./ -name '*.o')

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

sed -i "s|(PWD)|$PWD|g" make.include
sed -i "s|(MPIDIR)|%mpidir|g" make.include
mkdir lib
%make_build dsdpapi

pushd pdsdp/ScaLAPACK
%make_build all
%make_build maxcut
mv pdsdp5.scalapack pmaxcut ../../bin/
popd
%ifarch %ix86
pushd pdsdp/PLAPPACK
%make_build all
mv pdsdp5.plapack ../../bin/
popd
%endif
pushd examples
%make_build stable color
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name
install -d %buildroot%_docdir/%name
install -d %buildroot%_docdir/lib%name-devel/html

mv bin/*.dat-s bin/graph1 bin/results* bin/output.* \
	%buildroot%_datadir/%name/
rm -f bin/Makefile
install -m755 bin/* %buildroot%_bindir
install -m644 lib/* %buildroot%_libdir
install -p -m644 $(find ./ -name '*.h') \
	%buildroot%_includedir/%name
%ifnarch %ix86
rm -f %buildroot%_includedir/%name/pdsdp5plapack.h
%endif

install -p -m644 docs/DSDP5-Exe-UserGuide.pdf \
	docs/DSDP5-P1289-0905.pdf \
	%buildroot%_docdir/%name
install -p -m644 docs/DSDP5-API-UserGuide.pdf \
	%buildroot%_docdir/lib%name-devel
unzip docs/DSDP5-api-html.zip
install -p -m644 dox/html/* \
	%buildroot%_docdir/lib%name-devel/html

# shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../lib%name.a
mpicc -shared * \
	-lscalapack -lblacs -larpack_LINUX -llapack -lopenblas \
	-Wl,-rpath,%mpidir/lib \
	-Wl,-soname,lib%name.so.%somver -o ../lib%name.so.%sover
rm -f *
popd
rmdir tmp
ln -s lib%name.so.%sover lib%name.so.%somver
ln -s lib%name.so.%somver lib%name.so
popd

%files
%doc dsdp-license
%_bindir/*
%_datadir/%name

%files doc
%_docdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%changelog
* Tue Nov 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.8-alt11
- Fixed build with gcc-6.

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt10
- Built with OpenBLAS instead of GotoBLAS2

* Wed Jul 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt9
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt8
- Fixed RPATH

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt7
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt6
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt5
- Rebuilt for debuginfo

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt4
- Fixed overlinking of libraries

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt3
- Rebuilt with shared library of ARPACK
- Added shared library

* Tue Jul 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt2
- Fixed "always overflow destination buffer"

* Wed Jun 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8-alt1
- Initial build for Sisyphus

