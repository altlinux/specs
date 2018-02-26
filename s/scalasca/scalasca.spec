%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define over 1.3.1
%define cubever 3.0.%over
%define somver 0
%define sover %somver.%over
Name: scalasca
Version: %over
Release: alt14
Summary: Scalable performance Analysis of Large-Scale parallel Applications
License: MIT
Group: Development/Tools
Url: http://www.fz-juelich.de/jsc/scalasca/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.fz-juelich.de/jsc/datapool/scalasca/scalasca-1.3.1.tar.gz
Source1: Makefile.shared

Requires: papi
Conflicts: linuxtv-dvb-apps
Provides: kojak = 2.2p1_%over-%release
Conflicts: kojak < 2.2p1_%over-%release
Obsoletes: kojak < 2.2p1_%over-%release

%set_gcc_version 4.5
BuildPreReq: libgomp-devel libqt4-devel libpapi-devel libotf-devel
BuildPreReq: libpdtoolkit-devel pdtoolkit gcc4.5-fortran
BuildPreReq: %mpiimpl-devel doxygen binutils-devel gcc4.5-c++
BuildPreReq: texlive-latex-base ghostscript-utils libgomp4.5-devel

%description
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

%package doc
Summary: Documentation for SCALASCA
Group: Documentation
BuildArch: noarch

%description doc
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

This package contains documentation for SCALASCA.

%package devel-example
Summary: Example of using SCALASCA
Group: Development/Documentation
Requires: lib%name-devel = %version-%release

%description devel-example
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

This package contains example of using SCALASCA.

%package -n lib%name
Summary: Shared libraries of SCALASCA
Group: System/Libraries

%description -n lib%name
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

This package contains shared libraries of SCALASCA.

%package -n lib%name-devel
Summary: development files of SCALASCA
Group: Development/Other
Requires: libpapi-devel libgomp-devel libotf-devel
Requires: libiberty-devel %mpiimpl-devel binutils-devel
Requires: libsz0-devel = 2.2p1_%over-%release
Provides: libkojak-devel = 2.2p1_%over-%release
Conflicts: libkojak-devel < 2.2p1_%over-%release
Obsoletes: libkojak-devel < 2.2p1_%over-%release
Conflicts: kojak < 2.2p1_%over-%release
Obsoletes: kojak < 2.2p1_%over-%release
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

This package contains development files of SCALASCA.

%package -n lib%name-devel-static
Summary: Static libraries of SCALASCA
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

This package contains static libraries of SCALASCA.

%package -n lib%name-devel-doc
Summary: Development documentation for SCALASCA
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

This package contains development documentation for SCALASCA.

%package -n cube
Summary: CUBE Uniform Behavioral Encoding
Group: Monitoring
Version: %cubever
Requires(post,preun): alternatives
Requires: %name = %over-%release
Conflicts: kojak < 2.2p1_%over-%release
Obsoletes: kojak < 2.2p1_%over-%release

%description -n cube
CUBE (CUBE Uniform Behavioral Encoding) is a generic presentation component
suitable for displaying a wide variety of performance metrics for parallel
programs including MPI and OpenMP applications. CUBE allows interactive
exploration of a multidimensional performance space in a scalable fashion.
Scalability is achieved in two ways: hierarchical decomposition of individual
dimensions and aggregation across different dimensions. All performance
metrics are uniformly accommodated in the same display and thus provide the
ability to easily compare the effects of different kinds of performance
behavior.

%package -n cube-qt
Summary: Qt4 GUI for CUBE Uniform Behavioral Encoding
Group: Monitoring
Version: %cubever
Requires(post,preun): alternatives
Requires: cube = %cubever-%release

%description -n cube-qt
CUBE (CUBE Uniform Behavioral Encoding) is a generic presentation component
suitable for displaying a wide variety of performance metrics for parallel
programs including MPI and OpenMP applications. CUBE allows interactive
exploration of a multidimensional performance space in a scalable fashion.
Scalability is achieved in two ways: hierarchical decomposition of individual
dimensions and aggregation across different dimensions. All performance
metrics are uniformly accommodated in the same display and thus provide the
ability to easily compare the effects of different kinds of performance
behavior.

This package contains Qt4 interface for CUBE.

%package -n cube-wx
Summary: wxGTK+ GUI for CUBE Uniform Behavioral Encoding
Group: Monitoring
Version: %cubever
Requires(post,preun): alternatives
Requires: cube = %cubever-%release

%description -n cube-wx
CUBE (CUBE Uniform Behavioral Encoding) is a generic presentation component
suitable for displaying a wide variety of performance metrics for parallel
programs including MPI and OpenMP applications. CUBE allows interactive
exploration of a multidimensional performance space in a scalable fashion.
Scalability is achieved in two ways: hierarchical decomposition of individual
dimensions and aggregation across different dimensions. All performance
metrics are uniformly accommodated in the same display and thus provide the
ability to easily compare the effects of different kinds of performance
behavior.

This package contains wxGTK+ interface for CUBE.

%package -n libsz0
Summary: szlib - stripped down and slightly modified version of the zlib
Group: System/Libraries
Version: 2.2p1_%over
Provides: szlib = 2.2p1_%over-%release
Provides: libsz = 2.2p1_%over-%release
Conflicts: libsz < 2.2p1_%over-%release
Obsoletes: libsz < 2.2p1_%over-%release

%description -n libsz0
This is a stripped down and slightly modified version of the zlib data
compression library. All changes are documented in the ChangeLog file.
See below for the contents of the original README file.

Markus Geimer <m.geimer@fz-juelich.de>
Forschungszentrum Juelich GmbH, Germany

%package -n libsz0-headers
Summary: Development headers of szlib
Group: Development/C
Version: 2.2p1_%over
BuildArch: noarch
Provides: szlib-headers = 2.2p1_%over-%release
Provides: libsz-headers = 2.2p1_%over-%release
Conflicts: libsz-devel < 2.2p1_%over-%release
Obsoletes: libsz-devel < 2.2p1_%over-%release

%description -n libsz0-headers
Stripped down and slightly modified version of the zlib data
compression library. All changes are documented in the ChangeLog file.
See below for the contents of the original README file.

This package contains development headers of szlib.

%package -n libsz0-devel
Summary: Development files of szlib
Group: Development/C
Version: 2.2p1_%over
Requires: libsz0 = 2.2p1_%over-%release
Requires: libsz0-headers = 2.2p1_%over-%release
Provides: szlib-devel = 2.2p1_%over-%release
Provides: libsz-devel = 2.2p1_%over-%release
Conflicts: libsz-devel < 2.2p1_%over-%release
Obsoletes: libsz-devel < 2.2p1_%over-%release

%description -n libsz0-devel
Stripped down and slightly modified version of the zlib data
compression library. All changes are documented in the ChangeLog file.
See below for the contents of the original README file.

This package contains development files of szlib.

%package -n libsz0-devel-static
Summary: szlib static library
Group: Development/C
Version: 2.2p1_%over
Requires: libsz0-headers = 2.2p1_%over-%release
Provides: libsz-devel-static = 2.2p1_%over-%release
Conflicts: libsz-devel-static < 2.2p1_%over-%release
Obsoletes: libsz-devel-static < 2.2p1_%over-%release

%description -n libsz0-devel-static
Stripped down and slightly modified version of the zlib data
compression library. All changes are documented in the ChangeLog file.
See below for the contents of the original README file.

This package contains static version of szlib.

%prep
%setup

%install
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export PATH=$PATH:%_qt4dir/bin
export MPIDIR=%mpidir

%ifarch x86_64
sed -i -e 's/^\(PREC\).*/\1 = 64/' \
	mf/Makefile.defs.linux-gomp
%endif

export CC="mpicc -g"
export CXX="mpicxx -g"
./configure \
	--prefix=%prefix \
	--with-papi=%prefix \
	--with-otf=%prefix \
	--with-pdt=%prefix \
	--with-qmake=qmake \
	--compiler=gnu \
	--mpi=%mpiimpl

pushd build-*

sed -i 's|^\(MPILIB.*\)|\1 -Wl,-R%mpidir/lib|' Makefile.defs
sed -i 's|^\(FMPILIB\).*|\1 = -lmpi_f77 -lmpi_f90|' Makefile.defs
sed -i 's|^#OMPCXX|OMPCXX|' Makefile.defs
sed -i 's|^#OMPF90|OMPF90|' Makefile.defs
sed -i 's|^#OMPELGLIB|OMPELGLIB|' Makefile.defs
sed -i 's|^#OTFOMPELGLIB|OTFOMPELGLIB|' Makefile.defs
sed -i 's|^#OTFHYBELGLIB|OTFHYBELGLIB|' Makefile.defs
sed -i 's|^#PDTMPIINC|PDTMPIINC|' Makefile.defs
sed -i 's|^#PDTDIR.*|PDTDIR = %prefix|' Makefile.defs
sed -i 's|^#PDTARCH.*|PDTARCH =|' Makefile.defs
sed -i 's|^#PDTBIN.*|PDTBIN = $(PDTDIR)/bin|' Makefile.defs
%make

# szlib

pushd build/utils/szlib
install -m644 %SOURCE1 .
%make_build
rm -f *.o
%make_build -f Makefile.shared
popd

# libpomp

KINST_DIR=$(find $PWD -name kinst-pomp|sed 's|/kinst-pomp||')
OPARI_DIR=$(find $PWD -name opari -type f|sed 's|/opari$||')
chmod +x $KINST_DIR/kinst-pomp
export PATH=$KINST_DIR:$OPARI_DIR:$PATH

pushd build/opari/tool/Test
%make ctest
for i in `ls test*.c*inc.out`; do
	sed -i "1a\#include \"$i\"" opari.tab.c
done
kinst-pomp mpicc -I../../lib -c opari.tab.c
popd
cp -f build/opari/tool/Test/opari.tab.o build/opari/lib/
pushd build/opari/lib
%make libpomp.a
popd

popd

%make_install PREFIX=%buildroot%prefix install

pushd build-*
install -m644 build/opari/lib/*.a %buildroot%_libexecdir

install -d %buildroot%_docdir/%name
install -d %buildroot%_docdir/lib%name-devel/pearl
install -d %buildroot%_docdir/lib%name-devel/epik
install -d %buildroot%_docdir/cube3
install -d %buildroot%_libdir/%name-devel

# docs

pushd build/pearl
# unknown non-zero result (heed help :( )
doxygen doc/doxygen.conf ||:
popd

pushd build/epik
doxygen doc/doxygen.conf
popd


mv build/pearl/html/* %buildroot%_docdir/lib%name-devel/pearl/
mv build/epik/html/* %buildroot%_docdir/lib%name-devel/epik/
popd

sed -i 's|%buildroot||g' %buildroot%_bindir/cube-config

pushd %buildroot/%prefix/doc
mv *.used manuals/earl.pdf html/opari* \
	%buildroot%_docdir/lib%name-devel/
mv ../example %buildroot%_libdir/%name-devel/
mv METRICS.SPEC html manuals \
	%buildroot%_docdir/%name/
popd
install -p -m644 cube-3.0/doc/* %buildroot%_docdir/cube3

install -d %buildroot%_includedir/szlib
pushd build-*/build/utils/szlib
%make_install -f Makefile.shared PREFIX=%buildroot%prefix install

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

install -m644 *.h %buildroot%_includedir/szlib
ln -s zlib.h %buildroot%_includedir/szlib/szlib.h
ln -s libsz0.so.0.0.1 %buildroot%_libdir/libsz0.so.0
ln -s libsz0.so.0 %buildroot%_libdir/libsz0.so
popd

# shared libraries

pushd %buildroot%_libdir
LIBS0="pomp cubew3 elg.omp elg.mpi pearl.base pearl.mpi pearl.omp pearl.replay"
LIBS="$(ls *.a|sed 's|^lib\(.*\)\.a$|\1|'|egrep -v sz0)"
mkdir tmp
pushd tmp
for i in $LIBS0 $LIBS
do
	if [ ! -f ../lib$i.so.%sover ]; then
		ar x ../lib$i.a
		mpicxx -shared * -Wl,--as-needed -L.. $ADDLIB \
			-lsz0 -lpapi -lgomp -lbfd -lmpi_f77 -lgfortran \
			-Wl,-R%mpidir/lib \
			-Wl,-soname,lib$i.so.%somver -o ../lib$i.so.%sover
		ln -s lib$i.so.%sover ../lib$i.so.%somver
		ln -s lib$i.so.%somver ../lib$i.so
		rm -f *
		ADDLIB="$ADDLIB -l$i"
	fi
done
popd
rmdir tmp
popd

rm -f %buildroot%_bindir/cube3
ln -s cube3-qt %buildroot%_bindir/cube3

sed -i '1s|/sh|/bash|' \
	%buildroot%_bindir/cube-config \
	%buildroot%_bindir/pearl-config \
	%buildroot%_bindir/scarlet

%files
%doc COPYRIGHT LICENSE OPEN_ISSUES README.1st
%_bindir/*
%exclude %_bindir/kinst*
%exclude %_bindir/kconfig
%exclude %_bindir/cube*
%exclude %_bindir/opari*

%files doc
%_docdir/%name

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/libsz0.*

%files -n lib%name-devel
%_bindir/kinst*
%_bindir/kconfig
%_bindir/cube-config
%_bindir/opari*
%_libdir/*.so
%exclude %_libdir/libsz0.*
%dir %_libdir/%name-devel
%exclude %_libdir/%name-devel/*
%_includedir/*
%exclude %_includedir/szlib

%files -n lib%name-devel-static
%_libdir/*.a
%exclude %_libdir/libsz0.*

%files devel-example
%_libdir/%name-devel/*

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%files -n cube
%_bindir/cube3*
%exclude %_bindir/cube3-qt
%_docdir/cube3

%files -n cube-qt
%_bindir/cube3-qt

%files -n libsz0
%doc utils/szlib/ChangeLog utils/szlib/README utils/szlib/FAQ
%_libdir/libsz0.so.*

%files -n libsz0-headers
%_includedir/szlib

%files -n libsz0-devel
%_libdir/libsz0.so

%files -n libsz0-devel-static
%_libdir/libsz0.a

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt14
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt13
- Fixed build

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt12
- Fixed RPATH

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt11
- Rebuilt with papi 4.2.0
- Disabled using of perfctr

* Wed Nov 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt10
- Rebuilt

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt9
- Added -g into compiler flags

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt8
- Rebuilt for debuginfo

* Tue Dec 14 2010 Kirill A. Shutemov <kas@altlinux.org> 1.3.1-alt7
- Rebuilt with binutils-devel

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt6
- Rebuilt for soname set-versions

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 1.3.1-alt5
- Rebuilt wit new binutils

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt4
- Fixed linking

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt3
- Fixed for checkbashisms

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2
- Rebuilt with papi 4.1.0

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt7
- Rebuilt with binutils 2.20.51.0.9

* Sat Mar 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt6
- Rebuilt wit new binutils

* Sat Jan 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt5
- Rebuilt wit new binutils

* Tue Dec 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt4
- Release up

* Tue Nov 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3
- Rebuilt with texlive instead of tetex

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Rebuilt with binutils 2.20.51.0.2

* Tue Sep 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2
- Added shared libraries

* Wed Aug 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt6
- Rebuilt

* Wed Jul 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt5
- Created alternatives for CUBE

* Mon Jun 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt4.1
- Minimize requirements for devel package
- Extract Qt4/wxGTK+ CUBE's GUI and example into separate packages

* Mon Jun 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt4
- Nothing news

* Thu Jun 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Changed requirements: *-devel-static -> *-devel

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Moved szlib headers into separate package

* Wed Jun 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

