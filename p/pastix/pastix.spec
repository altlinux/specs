%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.31.84
Name: pastix
%define ldir %_libdir/%name
Version: 3184
Release: alt4
Summary: Parallel Sparse matriX package
License: CeCILL
Group: Sciences/Mathematics
Url: http://pastix.gforge.inria.fr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: https://gforge.inria.fr/frs/download.php/26891/pastix_release_%version.tar.bz2
Source1: config.in

Requires: lib%name = %version-%release

BuildPreReq: libscotch-devel libmetis0-devel %mpiimpl-devel
BuildPreReq: libgotoblas-devel chrpath

%description
PaStiX (Parallel Sparse matriX package) is a scientific library that
provides a high performance parallel solver for very large sparse
linear systems based on direct and block ILU(k) iterative methods.

%package -n lib%name
Summary: Shared libraries of PaStiX
Group: System/Libraries

%description -n lib%name
PaStiX (Parallel Sparse matriX package) is a scientific library that
provides a high performance parallel solver for very large sparse
linear systems based on direct and block ILU(k) iterative methods.

This package contains shared libraries of PaStiX.

%package -n lib%name-devel
Summary: Development files of PaStiX
Group: Development/C
Requires: %mpiimpl-devel
Requires: %name = %version-%release
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
PaStiX (Parallel Sparse matriX package) is a scientific library that
provides a high performance parallel solver for very large sparse
linear systems based on direct and block ILU(k) iterative methods.

This package contains development files of PaStiX.

%package -n lib%name-devel-doc
Summary: Development documentation for PaStiX
Group: Development/C
BuildArch: noarch

%description -n lib%name-devel-doc
PaStiX (Parallel Sparse matriX package) is a scientific library that
provides a high performance parallel solver for very large sparse
linear systems based on direct and block ILU(k) iterative methods.

This package contains development documentation for PaStiX.

%prep
%setup
install -m644 %SOURCE1 src

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|" src/config.in

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"


pushd src
%make_build -f makefile.old expor
mkdir ../install
%make $PWD/../install/libpastix.a
popd


%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

TOPDIR=$PWD
DESTDIR=%buildroot%_libdir
%make_install -C src -f makefile.old \
	DESTDIR=$DESTDIR TOPDIR=$TOPDIR MPIDIR=%mpidir install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -d %buildroot%ldir/bin
install -d %buildroot%ldir/include
install -d %buildroot%_docdir/%name

install -m755 bin/genheader bin/print_options %buildroot%ldir/bin
ln -s %ldir/bin/genheader %buildroot%_bindir
ln -s %ldir/bin/print_options %buildroot%_bindir
install -m644 bin/*.a %buildroot%_libdir
install -m644 install/*.a %buildroot%_libdir
install -m644 bin/*.h %buildroot%ldir/include

mv %buildroot%_libdir/*.sh %buildroot/%_bindir/
pushd %buildroot/%_bindir/
ln -s $(ls *.sh) pastix-conf
popd
rm -f %buildroot%_libdir/pastix-conf*
cp -f %buildroot%_libdir/*real.h %buildroot%_libdir/*real.inc \
	%buildroot%_libdir/murge.h %buildroot%_libdir/pastix_nompi.h \
	%buildroot%_includedir/

pushd %buildroot%_libdir
rm -f libpastix.a libpastix_murge.a
SUFFIX=_mpi_smp_nobubble_long_double_real_metis_
for i in libpastix libpastix_murge; do
	ln -s $i$SUFFIX.a $i.a
done
popd

mv %buildroot%_libdir/*.h %buildroot%_libdir/*.inc %buildroot%_includedir/
pushd %buildroot%_includedir
rm -f csc_utils.h cscd_utils.h murge.inc pastix.h pastix_fortran.h
SUFFIX=_long_double_real
for i in csc_utils cscd_utils pastix pastix_fortran; do
	ln -s $i$SUFFIX.h $i.h
done
ln -s murge$SUFFIX.inc murge.inc
popd

cp -fR doc/* %buildroot%_docdir/%name/

# shared libraries

simpleShare()
{
	if [ "$1" = "common" ]; then
		FINALIB=
	elif [ "$1" = "pastixutils" -o "$1" = "pastix" ]; then
		FINALIB="-lcommon_d $FINLIB"
	elif [ "$1$3" = "kass" ]; then
		FINALIB="-lcommon_d $FINLIB -lkass"
	else
		FINALIB=$FINLIB$3
	fi
	rm -f lib$1$3.so*
	mpif77 -shared $2 -L%buildroot%_libdir \
		$ADDLIB -lesmumps -lscotchmetis -lptscotch $FINALIB -lgoto2 -lrt \
		-Wl,-R%mpidir/lib \
		-Wl,-soname,lib$1$3.so.%somver -o lib$1$3.so.%sover
	ln -s lib$1$3.so.%sover lib$1$3.so.%somver
	ln -s lib$1$3.so.%somver lib$1$3.so
	rm -f $2
}

shareIt() {
	if [ "$1" = "pastix" -o "$1" = "sopalin3d" -o "$1" = "pastix_murge" ]
	then
		FINLIB="-lpthread -L. -lkass"
	elif [ "$1" = "common" ]; then
		FINLIB=
	elif [ "$1" = "pastixutils" -o "$1" = "blend3d" -o "$1" = "kass" ]
	then
		FINLIB=-lpastix
	else
		FINLIB=-lcommon
	fi
	ar x lib$1.a
	rm -f *_s.o *_d.o *_c.o *_z.o
	rm -f lib$1.so*
	simpleShare $1 '*.o'
	if [ "$1" = "pastix_murge" ]; then
		ADDLIB="lib$1.a $ADDLIB"
	else
		ADDLIB="-l$1 $ADDLIB"
	fi
	if [ "$1" = "pastix" -o "$1" = "common" -o "$1" = "pastixutils" \
		-o "$1" = "kass" ]
	then
		ar x lib$1.a
		simpleShare $1 '*_s.o' _s
		simpleShare $1 '*_d.o' _d
		simpleShare $1 '*_c.o' _c
		simpleShare $1 '*_z.o' _z
	fi
	rm -f *.o
}

pushd %buildroot%_libdir
for i in common pastixutils symbol %name blend3d order \
	kass dof fax sopalin3d %name %{name}_murge
do
	shareIt $i
done
popd

for i in %buildroot%ldir/bin/*
do
	chrpath -r %mpidir/lib $i || chrpath -d $i ||:
done

# fix pastix-conf

pushd %buildroot%_bindir
sed -i 's|^INC.*|INC="-I%_includedir -I%ldir/include"|g' \
	%name-conf
sed -i 's|%buildroot||g' *.sh
popd

%files
%doc src/Licence_CeCILL_V2-en.txt src/README.txt
%dir %ldir
%ldir/bin
%_bindir/genheader
%_bindir/print_options

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%ldir/include
%_includedir/*
%_bindir/*
%exclude %_bindir/genheader
%exclude %_bindir/print_options
%_libdir/*.so

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3184-alt4
- Rebuilt with OpenMPI 1.6

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3184-alt3
- Fixed RPATH

* Mon Sep 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3184-alt2
- Rebuilt with libmetis0 instead of libmetis

* Thu May 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3184-alt1
- Version 3184 (5.1.4)

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2995-alt5
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2995-alt4
- Built with GotoBLAS2 instead of ATLAS
- Disabled static libraries

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2995-alt3
- Added -g into compiler flags
- Moved libraries into %_libdir

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2995-alt2
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2995-alt1
- Version 2995

* Fri Oct 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt11
- Rebuilt for soname set-versions

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt10
- Fixed overlinking of libraries

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt9
- Removed paths to buildroot

* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt8
- Rebuilt with reformed Metis

* Sun Nov 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt7
- Fixed %name-conf

* Mon Oct 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt6
- Disabled requirement on openmpi-devel-static

* Sat Sep 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt5.1
- Added missing libraries

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt5
- Added shared libraries

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt4
- Rebuild with PIC

* Mon Jun 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt3
- Renamed function: quicksort -> pastix_quicksort (resolve conflict with IFPACK)

* Sun Jun 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt2
- Reform directory layout

* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2200-alt1
- Initial build for Sisyphus
