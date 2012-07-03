%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define origname blacs

Name: lib%origname

%define somver 1
%define sover %somver.1
Version: 1.1
Release: alt12
Summary: Basic Linear Algebra Communication Subprograms
License: LGPL
Group: Sciences/Mathematics
Url: http://www.netlib.org/blacs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.netlib.org/blacs/mpiblacs.tar.gz
# patch: http://www.netlib.org/blacs/mpiblacs-patch03.tgz
Source1: Bmake.inc

BuildPreReq: gcc-fortran %mpiimpl-devel libgfortran-devel

%description
The BLACS (Basic Linear Algebra Communication Subprograms) project is an ongoing
investigation whose purpose is to create a linear algebra oriented message
passing interface that may be implemented efficiently and uniformly across a
large range of distributed memory platforms.

The length of time required to implement efficient distributed memory algorithms
makes it impractical to rewrite programs for every new parallel machine. The
BLACS exist in order to make linear algebra applications both easier to program
and more portable. It is for this reason that the BLACS are used as the
communication layer of ScaLAPACK.

%package devel-debug
Summary: Debug version of BLACS
Group: Sciences/Mathematics
Requires: %name-devel = %version-%release

%description devel-debug
Debug version of BLACS.

%package -n %origname-tests
Summary: Testing executables for BLACS
Group: Sciences/Mathematics
Requires: %origname-tests-data = %version-%release

%description -n %origname-tests
Testing executables for BLACS.

%package -n %origname-tests-data
Summary: Testing data files for blacs-tests
Group: Sciences/Mathematics
BuildArch: noarch

%description -n %origname-tests-data
Testing data files for blacs-tests.

%package devel
Summary: Developer files for BLACS
Group: Development/Other
Requires: %name = %version-%release
Conflicts: %name-devel < %version-%release
Obsoletes: %name-devel < %version-%release

%description devel
Developer files for BLACS.

%package devel-static
Summary: Static libraries of BLACS
Group: Development/Other
Requires: %name-devel = %version-%release
Conflicts: %name-devel < %version-%release

%description devel-static
Static libraries of BLACS.


%prep
%setup -n BLACS
install -p -m644 %SOURCE1 ./

%build
mpi-selector --set %mpiimpl
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
source %mpidir/bin/mpivars.sh

sed -i "s|(BUILDDIR)|$PWD|" Bmake.inc
sed -i "s|(MPIIMPL)|%mpidir|" Bmake.inc
sed -i -e 's/(OPTFLAGS)/%optflags %optflags_shared/g' Bmake.inc
%make_build mpi
mkdir -pv LIB0
mv LIB/*.a LIB0/
make mpi what=clean
sed -i \
	-e 's/\(BLACSDBGLVL\ =\).*/\1 1/' \
	-e 's/\(GPROF\)/-pg --coverage/' \
	Bmake.inc
%make_build mpi
%make_build tester

# for testing before build BLACS
#pushd INSTALL
#for file in xsize xintface xsyserrors xtc_CsameF77 xtc_UseMpich xcmpi_sane \
#	xfmpi_sane
#do
#	%make_build $file
#done
#popd

%install
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
source %mpidir/bin/mpivars.sh
mkdir -pv %buildroot%_bindir
mkdir -pv %buildroot%_libdir
mkdir -pv %buildroot%_includedir
mkdir -pv %buildroot%_datadir/%origname-tests
mv LIB/*.a %buildroot%_libdir/
mv LIB0/*.a %buildroot%_libdir/
ln -s blacsCinit_MPI-LINUX-0.a %buildroot%_libdir/libblacsCinit.a
ln -s blacsF77init_MPI-LINUX-0.a %buildroot%_libdir/libblacsF77init.a
ln -s blacs_MPI-LINUX-0.a %buildroot%_libdir/libblacs.a
rm -f TESTING/EXE/Makefile
mv TESTING/EXE/*.dat %buildroot%_datadir/%origname-tests
mv TESTING/EXE/* %buildroot%_bindir/
mv SRC/MPI/*.h %buildroot%_includedir/

# shared libraries

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
for i in F77 C; do
	if [ "$i" = "C" ]; then
		SUFF=c
	fi
	ar x ../libblacs.a
	ar x ../libblacs${i}init.a
	for j in $(ls *.C); do
		mv $j $j.o
	done
	mpif77 -shared * \
		-Wl,-R%mpidir/lib \
		-Wl,-soname,libblacs$SUFF.so.%somver \
		-o ../libblacs$SUFF.so.%sover
	ln -s libblacs$SUFF.so.%sover ../libblacs$SUFF.so.%somver
	ln -s libblacs$SUFF.so.%somver ../libblacs$SUFF.so
	ln -s libblacs$SUFF.so ../libblacs${i}init.so
	rm -f *
done
popd
rmdir tmp
popd

%files
%doc README
%_libdir/*.so.*

%files devel-debug
%_libdir/*-1.a
%_libdir/*-1.a

%files -n %origname-tests
%_bindir/*

%files -n %origname-tests-data
%_datadir/%origname-tests

%files devel
%_libdir/*.so
%_includedir/*.h

%files devel-static
%_libdir/*.a
%exclude %_libdir/*-1.a

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt12
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt11
- Fixed RPATH

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt10
- Rebuilt for debuginfo

* Mon Jan 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt9
- Rebuilt with glibc 2.11.3

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt8
- Rebuilt for soname set-versions

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt7
- Fixed overlinking of libraries and executables

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt6
- Rebuilt without udapl support

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt5
- Added shared libraries

* Thu Jun 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt4
- Rebuild with PIC

* Mon Jun 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Add links: blacs*_MPI-LINUX-0.a -> libblacs*.a

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Rebuild with OpenMPI instead mvapich2

* Sun Feb 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

