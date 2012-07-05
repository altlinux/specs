%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%ifarch %ix86
%define barch IA32
%endif
%ifarch x86_64
%define barch X86_64
%endif

%define somver 0
%define sover %somver.3.3
Name: mpip
Version: 3.3
Release: alt4.svn20120216
Summary: Lightweight profiling library for MPI applications
License: BSD
Group: Development/Tools
Url: http://mpip.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://mpip.svn.sourceforge.net/viewvc/mpip.tar.gz
Source1: farg.f

Requires: lib%name = %version-%release

BuildPreReq: %mpiimpl-devel binutils-devel libunwind-devel
BuildPreReq: gcc-fortran libgfortran-devel
BuildPreReq: python%_python_version(copy) /proc

%description
mpiP is a lightweight profiling library for MPI applications. Because
it only collects statistical information about MPI functions, mpiP
generates considerably less overhead and much less data than tracing
tools. All the information captured by mpiP is task-local. It only uses
communication during report generation, typically at the end of the
experiment, to merge results from all of the tasks into one output
file.

To learn more about performance analysis with mpiP, see Vetter, J.S.
and M.O. McCracken, "Statistical Scalability Analysis of Communication
Operations in Distributed Applications," Proc. ACM SIGPLAN Symp. on
Principles and Practice of Parallel Programming (PPOPP), 2001.

%package -n lib%name
Summary: Shared libraries of mpiP (MPI profiling library)
Group: System/Libraries

%description -n lib%name
mpiP is a lightweight profiling library for MPI applications. Because
it only collects statistical information about MPI functions, mpiP
generates considerably less overhead and much less data than tracing
tools. All the information captured by mpiP is task-local. It only uses
communication during report generation, typically at the end of the
experiment, to merge results from all of the tasks into one output
file.

This package contains shared libraries of mpiP.

%package -n lib%name-devel
Summary: Development files of mpiP (MPI profiling library)
Group: Development/Other
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description -n lib%name-devel
mpiP is a lightweight profiling library for MPI applications. Because
it only collects statistical information about MPI functions, mpiP
generates considerably less overhead and much less data than tracing
tools. All the information captured by mpiP is task-local. It only uses
communication during report generation, typically at the end of the
experiment, to merge results from all of the tasks into one output
file.

This package contains development files of mpiP.

%package -n libfarg
Summary: Fortran command line arguments library for MPI applications
Group: System/Libraries

%description -n libfarg
This small library provides fortran functions `f__xargc' and `f__xargv'
needed for some MPI applications.

%package -n libfarg-devel
Summary: Development files of fortran command line arguments library for MPI applications
Group: Development/Other
Requires: libfarg = %version-%release

%description -n libfarg-devel
This small library provides fortran functions `f__xargc' and `f__xargv'
needed for some MPI applications.

This package contains development files of this library.

%prep
%setup
install -m644 %SOURCE1 .

%build
mpi-selector --set %mpiimpl
source %_sysconfdir/profile.d/mpi-selector.sh
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

f77 -fno-underscoring -fPIC -c farg.f
ar r libfarg.a farg.o
ranlib libfarg.a
f77 -shared farg.o -Wl,-soname,libfarg.so.%somver \
	-o libfarg.so.%sover
ln -s libfarg.so.%sover libfarg.so.%somver
ln -s libfarg.so.%somver libfarg.so

%add_optflags %optflags_shared
%configure \
	--enable-fortranweak \
	--enable-bfd \
	--enable-getarg \
	--with-include=-I%mpidir/include \
	--with-ldflags=-L%mpidir/lib \
	--with-libs="-lmpi -lmpi_f77 -lgfortran -Wl,-rpath,%mpidir/lib" \
	--with-binutils-dir=%prefix \
	--with-libunwind=%prefix \
	--with-wtime \
	--enable-stackdepth=16

%make _ARCH=%barch OS=Linux SOMVER=%somver SOVER=%sover all

%install
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/mpip_timers

mkdir exe
mv testing/*.exe exe/
pushd exe
for i in $(ls|sed -e 's/\.exe//'); do
	mv $i.exe $i.mpip
done
install -m755 * %buildroot%_bindir
popd
install -m644 *.a %buildroot%_libdir
cp -P *.so* %buildroot%_libdir/
install -m644 *.h %buildroot%_includedir
install -m644 mpip_timers/linux_posix.h %buildroot%_includedir/mpip_timers

%files
%doc doc/*
%_bindir/*

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/libfarg.so.*

%files -n lib%name-devel
%_libdir/*.so
%exclude %_libdir/libfarg.so
%_includedir/*

%files -n libfarg
%_libdir/libfarg.so.*

%files -n libfarg-devel
%doc farg.f
%_libdir/libfarg.so

%changelog
* Thu Jul 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt4.svn20120216
- Rebuilt with OpenMPI 1.6

* Tue Feb 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt3.svn20120216
- New snapshot

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt3.svn20110623
- New snapshot

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt3.svn20110316
- Fixed RPATH

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt2.svn20110316
- Fixed build

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.svn20110316
- Version 3.3
- Disable devel-static packages

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20100401.4
- Rebuilt for debuginfo

* Tue Dec 14 2010 Kirill A. Shutemov <kas@altlinux.org> 3.2.1-alt1.svn20100401.3
- Rebuilt with binutils-devel

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 3.2.1-alt1.svn20100401.2
- Rebuilt with new binutils

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20100401.1
- Fixed overlinking of libraries

* Wed Jun 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.svn20100401
- Version 3.2.1

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt3.svn20090520.4
- Rebuilt with binutils 2.20.51.0.9

* Sat Mar 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt3.svn20090520.3
- Rebuilt with new binutils

* Sat Jan 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt3.svn20090520.2
- Rebuilt with new binutils

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt3.svn20090520.1
- Rebuilt with python 2.6

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt3.svn20090520
- New snapshot
- Added shared libraries
- Rebuilt without udapl support

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt3
- Rebuilt with binutils 2.20.51.0.2

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt2
- Rebuilt

* Wed May 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1
- Initial build for Sisyphus

