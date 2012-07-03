%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: tau
Version: 2.19.2
Release: alt21
Summary: TAU Portable Profiling Package
License: BSD-like
Group: Development/Tools
Url: http://www.cs.uoregon.edu/research/tau/home.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.cs.uoregon.edu/research/paracomp/tau/tauprofile/dist/tau_latest.tar.gz
Source1: http://www.cs.uoregon.edu/research/tau/tau-usersguide.pdf

Requires: lib%name = %version-%release
Requires: %name-j = %version-%release
Requires: libpapi pdbsql
Requires: openpdt
Conflicts: pdtoolkit
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release
%add_python_req_skip edu java javax

BuildRequires(pre): rpm-build-java rpm-build-python
BuildPreReq: java-devel-default libgmp-devel %mpiimpl-devel gcc-c++ gcc-fortran
BuildPreReq: openpdt libopenpdt-devel libpapi-devel chrpath
BuildPreReq: jflex postgresql-devel libscalasca-devel binutils-devel
BuildPreReq: libgomp-devel libotf-devel zlib-devel
BuildPreReq: libstdc++-devel libsz0-devel python-devel mysql-connector-java
BuildPreReq: jfreechart jcommon swing-layout postgresql-jdbc xerces-j2 junit

%description
TAU is a program and performance analysis tool framework being developed for
the DOE and ASC program at University of Oregon. TAU provides a suite of 
static and dynamic tools that provide graphical user
interaction and interoperation to form an integrated analysis environment for
parallel Fortran 95, C and C++ applications.  In particular, a robust
performance profiling facility availble in TAU has been applied extensively in
the ACTS toolkit.  Also, recent advancements in TAU's code analysis
capabilities have allowed new static tools to be developed, such as an
automatic instrumentation tool.

%package -n lib%name
Summary: Shared libraries of TAU Portable Profiling Package
Group: System/Libraries

%description -n lib%name
TAU is a program and performance analysis tool framework being developed for
the DOE and ASC program at University of Oregon. TAU provides a suite of 
static and dynamic tools that provide graphical user
interaction and interoperation to form an integrated analysis environment for
parallel Fortran 95, C and C++ applications.  In particular, a robust
performance profiling facility availble in TAU has been applied extensively in
the ACTS toolkit.  Also, recent advancements in TAU's code analysis
capabilities have allowed new static tools to be developed, such as an
automatic instrumentation tool.

This package contains shared libraries of TAU Portable Profiling Package.

%package -n lib%name-common
Summary: Common development files of TAU Portable Profiling Package
Group: Development/Other
Requires: libscalasca-devel
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-common
TAU is a program and performance analysis tool framework being developed for
the DOE and ASC program at University of Oregon. TAU provides a suite of 
static and dynamic tools that provide graphical user
interaction and interoperation to form an integrated analysis environment for
parallel Fortran 95, C and C++ applications.  In particular, a robust
performance profiling facility availble in TAU has been applied extensively in
the ACTS toolkit.  Also, recent advancements in TAU's code analysis
capabilities have allowed new static tools to be developed, such as an
automatic instrumentation tool.

This package contains common development files of TAU Portable Profiling Package.

%package -n lib%name-devel
Summary: Development files of TAU Portable Profiling Package
Group: Development/Other
Requires: lib%name = %version-%release
Requires: lib%name-common = %version-%release
Requires: libscalasca-devel libpapi-devel libgomp-devel libsz0-devel
Requires: openpdt
Conflicts: pdtoolkit
Requires: libopenpdt-devel
Conflicts: libpdtoolkit-devel
Conflicts: %name < %version-%release
Obsoletes: %name < %version-%release

%description -n lib%name-devel
TAU is a program and performance analysis tool framework being developed for
the DOE and ASC program at University of Oregon. TAU provides a suite of 
static and dynamic tools that provide graphical user
interaction and interoperation to form an integrated analysis environment for
parallel Fortran 95, C and C++ applications.  In particular, a robust
performance profiling facility availble in TAU has been applied extensively in
the ACTS toolkit.  Also, recent advancements in TAU's code analysis
capabilities have allowed new static tools to be developed, such as an
automatic instrumentation tool.

This package contains development files of TAU Portable Profiling Package.

%package -n lib%name-devel-static
Summary: Static libraries of TAU Portable Profiling Package
Group: Development/Other
Requires: lib%name-devel = %version-%release
Requires: lib%name-common = %version-%release
Requires: libpapi-devel libgomp-devel libsz0-devel
Requires: libopenpdt-devel openpdt libscalasca-devel libpapi-devel

%description -n lib%name-devel-static
TAU is a program and performance analysis tool framework being developed for
the DOE and ASC program at University of Oregon. TAU provides a suite of 
static and dynamic tools that provide graphical user
interaction and interoperation to form an integrated analysis environment for
parallel Fortran 95, C and C++ applications.  In particular, a robust
performance profiling facility availble in TAU has been applied extensively in
the ACTS toolkit.  Also, recent advancements in TAU's code analysis
capabilities have allowed new static tools to be developed, such as an
automatic instrumentation tool.

This package contains static libraries of TAU Portable Profiling Package.

%package doc
Summary: Documentation for TAU Portable Profiling Package
Group: Documentation
BuildArch: noarch

%description doc
TAU is a program and performance analysis tool framework being developed for
the DOE and ASC program at University of Oregon. TAU provides a suite of 
static and dynamic tools that provide graphical user
interaction and interoperation to form an integrated analysis environment for
parallel Fortran 95, C and C++ applications.  In particular, a robust
performance profiling facility availble in TAU has been applied extensively in
the ACTS toolkit.  Also, recent advancements in TAU's code analysis
capabilities have allowed new static tools to be developed, such as an
automatic instrumentation tool.

This package contains documentation for TAU Portable Profiling Package.

%package j
Summary: Java libraries of TAU Portable Profiling Package
Group: Development/Tools
BuildArch: noarch
Requires: java-cup jatha jcommon jfreechart jgraph jython xerces-j2
Requires: swing-layout jargs
Conflicts: libjogl

%description j
TAU is a program and performance analysis tool framework being developed for
the DOE and ASC program at University of Oregon. TAU provides a suite of 
static and dynamic tools that provide graphical user
interaction and interoperation to form an integrated analysis environment for
parallel Fortran 95, C and C++ applications.  In particular, a robust
performance profiling facility availble in TAU has been applied extensively in
the ACTS toolkit.  Also, recent advancements in TAU's code analysis
capabilities have allowed new static tools to be developed, such as an
automatic instrumentation tool.

This package contains java libraries of TAU Portable Profiling Package.

%prep
%setup
%ifarch x86_64
sed -i -e 's/^BITS.*/BITS = 64/' src/Profile/Makefile
sed -i 's|lib/libpdb\.a|lib64/libpdb.a|g' utils/Makefile
%endif

%install
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

export BUILDROOT=%buildroot
./configure \
	-arch=%_arch \
	-c++=mpic++ \
	-cc=mpicc \
	-fortran=gfortran \
	-prefix=%prefix \
	-exec-prefix= \
	-mpi \
	-mpiinc=%mpidir/include \
	-mpilib=%mpidir/lib -mpilibrary="-lmpi" \
	-otf=%prefix \
	-pdt=%prefix \
	-papi=%prefix \
	-slog2 \
	-PROFILE -PROFILECALLPATH -PROFILEPARAM \
	-DEPTHLIMIT -PROFILEMEMORY \
	-CPUTIME -MULTIPLECOUNTERS \
	-useropt="%optflags %optflags_shared -I$PWD/include -fno-strict-aliasing" \
	-opari=%prefix -MPITRACE \
	-openmp \
	-extrashlibopts="-Wl,-R%mpidir/lib -L%mpidir/lib -lmpi -lgomp"

export BUILDROOTLIB=%buildroot%_libexecdir
%ifarch x86_64
export LIBSUFF=64
%endif
sed -i 's|^\(TAU_PREFIX_INSTALL_DIR\).*|\1=%buildroot%prefix|' \
	include/Makefile utils/Makefile
TOPDIR=$PWD
%make install TOPDIR=$TOPDIR
%make exports TOPDIR=$TOPDIR

pushd utils
%make_build tau2profile TOPDIR=$TOPDIR
install -m755 tau2profile %buildroot%_bindir
popd

pushd utils/elgconverter
%make_build includedir=%_includedir libdir=%_libdir TOPDIR=$TOPDIR
install -m755 tau2elg %buildroot%_bindir
popd

pushd %buildroot%_bindir
mv opari tau_opari
popd

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

install -d %buildroot%_sysconfdir
mv %buildroot%prefix/etc/* %buildroot%_sysconfdir/
mv %buildroot%prefix/tools/src/perfdmf/etc/* %buildroot%_sysconfdir/
rm -f %buildroot%_bindir/*.ini %buildroot%_includedir/Makefile \
	%buildroot%_sysconfdir/*.py
rm -fR %buildroot%_includedir/makefiles

install -d %buildroot%_datadir/%name
sed -i \
	-e 's/^\(TAU_CONFIG\).*/\1=/g' \
	%buildroot%_libdir/Makefile*
mv %buildroot%_libdir/Makefile* %buildroot%_datadir/%name/

# fix TAU shared library

%ifarch x86_64
export OBJECT_MODE=64
%endif
sed -i \
	-e 's/^\(CONFIG_CC\).*/\1=kinst-pomp gcc/' \
	-e 's/^\(CONFIG_CXX\).*/\1=kinst-pomp g++/' \
	-e 's/^\(TAU_F90\ *\=\).*\(gfortran.*\)/\1 kinst-pomp \2/' \
	include/Makefile
pushd src/Profile
%make clean
sed -i -e '278s|\$(TAU_DISABLE)||' Makefile
%make TOPDIR=$TOPDIR
cp -f libTAU*so.2.19.2 %buildroot%_libdir/
popd

# fix scripts

pushd %buildroot%_bindir
for i in tau_analyze perfexplorer ppscript paraprof phaseconvert \
	perfdmf_loadtrial perfdmf_createexp perfdmf_createapp perfdmf_configure \
	tau2slog2 slog2print jumpshot perfexplorer_configure
do
	sed -i 's|^\(TAUROOT\).*|\1=%prefix|' $i
	sed -i -e 's/jcommon\-0\.9\.6/jcommon0/g' $i
	sed -i -e 's/jfreechart\-0\.9\.21/jfreechart0/g' $i
	sed -i -e 's/xerces/xerces-j2/g' $i
	sed -i 's|^\(TRACE_LIBDIR\).*|\1=%_javadir|' $i
	sed -i 's|^\(GUI_LIBDIR\).*|\1=%_javadir|' $i
	sed -i 's|^\(TAU_LIBDIR\).*|\1=%_javadir|' $i
	sed -i 's|^\(LIBDIR\).*|\1=%_javadir|' $i
	sed -i 's|^\(JARDIR\).*|\1=%_javadir|' $i
	sed -i 's|\${TAUROOT}/\${CONFIG_ARCH}/lib|%_javadir|g' $i
	sed -i 's|\$TAUROOT/\$CONFIG_ARCH/lib|%_javadir|g' $i
done
sed -i 's|%buildroot||g' $(egrep -R '%buildroot' ./ |\
	egrep -v 'Binary\ file.*matches' |awk -F : '{print $1}')
rm -f racy taud
install -d %buildroot%python_sitelibdir/%name
mv *portal.py %buildroot%python_sitelibdir/%name/
popd

rm -f %buildroot%_includedir/include/Makefile*
rm -fR %buildroot%_includedir/include/makefiles

# libs

pushd %buildroot%_libdir
#ln -s libTAU.so.2 libTAU.so
ln -s libTAU.so.2 libtau.so
ln -s libTauDisable.so.2 libTauDisable.so
#ln -s libTraceInput.so.2 libTraceInput.so
ln -s $(ls libtau-memory*.a) libtau.a
ln -s $(ls libtau-memory*.a) libTAU.a
ln -s $(ls libTauMpi*.a) libTauMpi.a
rm -f libjogl*

install -d %buildroot%_javadir
rm -f derby.jar java_cup.jar jcommon-*.jar jfreechart-*.jar \
	jgraph.jar jython.jar xerces.jar
mv *.jar %buildroot%_javadir/
popd

# docs

install -d %buildroot%_docdir/%name
install -d %buildroot%_mandir
install -p -m644 %SOURCE1 %buildroot%_docdir/%name
mv %buildroot%prefix/examples %buildroot%_docdir/%name/
mv %buildroot%prefix/man/* %buildroot%_mandir/
pushd %buildroot%_man1dir
rm -f tau2vtf.1 tau_validate.1 tau_poe.1 tau_setup.1 vtf*
popd

touch %buildroot%python_sitelibdir/%name/__init__.py

sed -i 's|%buildroot||g' %buildroot%_includedir/*.h \
	%buildroot%_datadir/%name/Makefile.*

for i in %buildroot%_libdir/*; do
	chrpath -r %mpidir/lib $i || chrpath -d $i ||:
done
rm -f %buildroot%_libdir/*/*.so

%files
%doc README COPYRIGHT LICENSE CREDITS
%_bindir/*
%exclude %_bindir/tau_opari
%exclude %_bindir/tau_reduce
%exclude %_bindir/tau_ompcheck
%exclude %_bindir/tau_wrap
%exclude %_bindir/tau_instrumentor
%exclude %_bindir/tau-config
%exclude %_bindir/tau_cc.sh
%exclude %_bindir/tau_compiler.sh
%exclude %_bindir/tau_cxx.sh
%exclude %_bindir/tau_f90.sh
%exclude %_bindir/taucc
%exclude %_bindir/taucxx
%exclude %_bindir/tauex*
%exclude %_bindir/tauf90
%exclude %_bindir/tau_header_list
%exclude %_bindir/tau_header_replace.pl
%exclude %_bindir/tau_load.sh
%exclude %_bindir/tau_throttle.sh
%exclude %_bindir/tauinc.pl
%python_sitelibdir/%name
%_sysconfdir/*
%_man1dir/*
%exclude %_man1dir/tau_reduce.1*
%exclude %_man1dir/tau_ompcheck.1*
%exclude %_man1dir/tau_wrap.1*
%exclude %_man1dir/tau_instrumentor.1*
%exclude %_man1dir/tau_compiler.sh.1*
%exclude %_man1dir/tau_throttle.sh.1*
%exclude %_man1dir/taucc.1*
%exclude %_man1dir/taucxx.1*
%exclude %_man1dir/tauex.1*
%exclude %_man1dir/tauf90.1*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-common
%_bindir/tau_opari
%_bindir/tau_reduce
%_bindir/tau_ompcheck
%_bindir/tau_wrap
%_bindir/tau_instrumentor
%_bindir/tau-config
%_bindir/tau_cc.sh
%_bindir/tau_compiler.sh
%_bindir/tau_cxx.sh
%_bindir/tau_f90.sh
%_bindir/taucc
%_bindir/taucxx
%_bindir/tauex*
%_bindir/tauf90
%_bindir/tau_header_list
%_bindir/tau_header_replace.pl
%_bindir/tau_load.sh
%_bindir/tau_throttle.sh
%_bindir/tauinc.pl
%_includedir/*
%exclude %_includedir/pomp_lib.h
%_datadir/%name
%_man1dir/tau_reduce.1*
%_man1dir/tau_ompcheck.1*
%_man1dir/tau_wrap.1*
%_man1dir/tau_instrumentor.1*
%_man1dir/tau_compiler.sh.1*
%_man1dir/tau_throttle.sh.1*
%_man1dir/taucc.1*
%_man1dir/taucxx.1*
%_man1dir/tauex.1*
%_man1dir/tauf90.1*
%_man3dir/*

%files -n lib%name-devel
%_libdir/*.so

#files -n lib%name-devel-static
#_libdir/*.a

%files doc
%_docdir/%name

%files j
%_javadir/*
%exclude %_javadir/jargs.jar

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt21
- Rebuilt with OpenMPI 1.6

* Sat Mar 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt20
- Rebuilt with OpenPDT

* Tue Mar 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt19
- Removed requirement on pdbsql

* Tue Mar 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt18
- Rebuilt without pdtoolkit

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt17
- Deleted unused files from buildroot

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt16
- Removed RPATH
- Disabled devel-static package

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt15
- Rebuilt with papi 4.2.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.19.2-alt14.1
- Rebuild with Python-2.7

* Wed Aug 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt14
- Rebuilt without perfctr

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt13
- Rebuilt with internal jogl.jar

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt12
- Rebuilt for debuginfo

* Tue Feb 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt11
- Fixed build

* Tue Dec 14 2010 Kirill A. Shutemov <kas@altlinux.org> 2.19.2-alt10
- Rebuilt with binutils-devel

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt9
- Rebuilt with PostgreSQL 9

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt8
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Kirill A. Shutemov <kas@altlinux.org> 2.19.2-alt7
- Rebuilt with new binutils

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt6
- Fixed insecure setting of LD_LIBRARY_PATH (ALT #24331)

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt5
- Fixed linking of libraries and executables
- Fixed for checkbashisms

* Mon Sep 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt4
- Avoid conflict with jargs

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt3
- Removed paths to buildroot
- Set shebangs to bash

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt2
- Fixed unsafe-tmp-usage-in-scripts

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19.2-alt1
- Version 2.19.2
- Rebuilt with papi 4.1.0

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.3-alt7
- Rebuilt with binutils 2.20.51.0.9

* Sat Mar 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.3-alt6
- Rebuilt with new binutils

* Mon Mar 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.3-alt5
- Rebuilt width postgresql 8.4

* Sat Jan 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.3-alt4
- Rebuilt with new binutils

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.3-alt3
- Rebuilt with python 2.6

* Tue Nov 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.3-alt2
- Fixed using of temp files

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.3-alt1
- Version 2.18.3-alt1

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt10
- Rebuilt with binutils 2.20.51.0.2

* Thu Sep 3 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt9.1
- Rebuilt with shared libraries of PDToolkit, SCALASCA and OTF

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt9
- Rebuilt

* Wed Jul 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt8
- Add requirement on libjogl for tau-j package

* Fri Jun 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt7
- Change requirements: *-devel-static -> *-devel

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt6
- Moved development executables, header and man pages into separate package

* Wed Jun 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt5
- Rebuild with SCALASCA (instead obsoleted KOJAK)

* Tue Jun 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt4
- Changed Makefile and library linking for use TAU instrumentor by client
	development software (e.g. legacy taucc)
- Moved instrumentation executables into devel package

* Sun May 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt3
- Fixed headers for gcc 4.4

* Fri May 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt2
- Resolved conflict with libkojak-devel

* Sun May 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.18.1p1-alt1
- Initial build for Sisyphus

