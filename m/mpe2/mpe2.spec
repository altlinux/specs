%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 1
%define sover %somver.3.0
Name: mpe2
Version: 1.3.0
Release: alt5
Summary: The Multi-Processing Environment
License: Free
Group: Development/Tools
Url: http://www.mcs.anl.gov/research/projects/perfvis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ftp://ftp.mcs.anl.gov/pub/mpi/mpe/mpe2.tar.gz
Source1: http://www.mcs.anl.gov/mpi/mpich1/docs/mpeman.pdf
Source2: ftp://ftp.mcs.anl.gov/pub/mpi/slog2/js4-usersguide.pdf

Requires: %name-j = %version-%release
Requires: libTraceInput = %version-%release
Requires: tau

BuildRequires(pre): rpm-build-java
BuildPreReq: %mpiimpl-devel libX11-devel java-devel-default libtau-devel
BuildRequires: binutils-devel

%description
The Multi-Processing Environment (MPE) attempts to provide programmers with 
a complete suite of performance analysis tools for their MPI programs based
on post processing approach.  These tools include a set of profiling libraries, 
a set of utility programs, and a set of graphical tools.

%package j
Summary: JAR files for The Multi-Processing Environment (MPE)
Group: Development/Tools
BuildArch: noarch
Requires: tau-j

%description j
The Multi-Processing Environment (MPE) attempts to provide programmers with 
a complete suite of performance analysis tools for their MPI programs based
on post processing approach.  These tools include a set of profiling libraries, 
a set of utility programs, and a set of graphical tools.

This package contains JAR files for MPE.

%package -n lib%name-devel-doc
Summary: Documentation for The Multi-Processing Environment (MPE)
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-doc
The Multi-Processing Environment (MPE) attempts to provide programmers with 
a complete suite of performance analysis tools for their MPI programs based
on post processing approach.  These tools include a set of profiling libraries, 
a set of utility programs, and a set of graphical tools.

This package contains development documentation for MPE.

%package -n libTraceInput
Summary: Trace library for log2sdk
Group: Development/Tools

%description -n libTraceInput
The Multi-Processing Environment (MPE) attempts to provide programmers with 
a complete suite of performance analysis tools for their MPI programs based
on post processing approach.  These tools include a set of profiling libraries, 
a set of utility programs, and a set of graphical tools.

This package contains trace library for lig2sdk.

%package -n lib%name
Summary: Shared libraries of The Multi-Processing Environment (MPE)
Group: System/Libraries
Requires: libTraceInput = %version-%release

%description -n lib%name
The Multi-Processing Environment (MPE) attempts to provide programmers with 
a complete suite of performance analysis tools for their MPI programs based
on post processing approach.  These tools include a set of profiling libraries, 
a set of utility programs, and a set of graphical tools.

This package contains shared libraries of MPE.

%package -n lib%name-devel
Summary: Development files of The Multi-Processing Environment (MPE)
Group: Development/Other
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
The Multi-Processing Environment (MPE) attempts to provide programmers with 
a complete suite of performance analysis tools for their MPI programs based
on post processing approach.  These tools include a set of profiling libraries, 
a set of utility programs, and a set of graphical tools.

This package contains development files of MPE.

%package -n lib%name-devel-static
Summary: Static libraries of The Multi-Processing Environment (MPE)
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
The Multi-Processing Environment (MPE) attempts to provide programmers with 
a complete suite of performance analysis tools for their MPI programs based
on post processing approach.  These tools include a set of profiling libraries, 
a set of utility programs, and a set of graphical tools.

This package contains static libraries of MPE.

%prep
%setup

%build
mpi-selector --set %mpiimpl
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

cp src/slog2sdk/src/logformat/trace/trace_API.h include/
%autoreconf
%configure \
	--enable-checkMPIwtime \
	--enable-wrappers \
	--enable-collchk \
	--enable-strict \
	--with-mpiinc="-I%mpidir/include" \
	--with-mpilibs="-L%mpidir/lib -lmpi_f77 -lmpi_f90 -lmpi -lm" \
	--with-f2cmpilibs="-lmpi_f77 -lmpi_f90" \
	--enable-slog2=build \
	--with-java2=%_libexecdir/jvm/java \
	CFLAGS="%optflags %optflags_shared -I$PWD/include" \
	FFLAGS="%optflags %optflags_shared" LDFLAGS="-L$PWD/lib"
%make

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -d %buildroot%_javadir
install -d %buildroot%_docdir/lib%name-devel

SRCDIR=$PWD
pushd %buildroot%_bindir
rm -f jumpshot slog2print
for i in clog2TOslog2 clog2print clogTOslog2 clogprint \
	logconvertor rlogTOslog2 rlogprint \
	slog2filter slog2navigator slog2updater \
	textlogTOslog2 textlogprint
do
	sed -i 's|^\(GUI_LIBDIR\).*|\1=%_javadir|' $i
	sed -i 's|^\(GUI_HOME\).*|\1=~|' $i
done
sed -i "s|$SRCDIR|%prefix|g" mpe?c
popd

rm -f %buildroot%_libdir/jumpshot.jar %buildroot%_libdir/traceTOslog2.jar
rm -f %buildroot%_libdir/slog2printserial.jar
mv %buildroot%_libdir/*.jar %buildroot%_javadir/
#mv %buildroot%prefix/doc/* %buildroot%_docdir/lib%name-devel/
#mv %buildroot%prefix/www %buildroot%_docdir/lib%name-devel/
pushd %buildroot%_datadir
mv example* logfiles %buildroot%_docdir/lib%name-devel/
popd
install %SOURCE1 %SOURCE2 %buildroot%_docdir/lib%name-devel

# shared libraries

pushd %buildroot%_libdir
LIBS="$(ls *.a|egrep -v 'libmpe\.a'|sed 's|\.a||')"
mkdir tmp
pushd tmp
for i in libmpe $LIBS; do
	ar x ../$i.a
	mpicc -shared * -L.. $ADDLIB -lX11 -lpthread \
		-Wl,-R%mpidir/lib \
		-Wl,-soname,$i.so.%somver -o ../$i.so.%sover
	ln -s $i.so.%sover ../$i.so.%somver
	ln -s $i.so.%somver ../$i.so
	rm -f *
	ADDLIB="-lmpe"
done
popd
rmdir tmp
popd

sed -i 's|%buildroot||g' %buildroot%_sbindir/mpeuninstall

mv %buildroot%_docdir/www4 %buildroot%_docdir/lib%name-devel/

%files
%doc README
%_sysconfdir/*
%_bindir/*
%exclude %_bindir/mpe?c
%_sbindir/*

%files -n libTraceInput
%_libdir/trace_*

%files j
%_javadir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/mpe?c
%_includedir/*
%_libdir/*.so

#files -n lib%name-devel-static
#_libdir/*.a
#_libdir/*.o

%files -n lib%name-devel-doc
%_docdir/lib%name-devel
%_docdir/jumpshot-4
%_man4dir/*

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt5
- Rebuilt with OpenMPI 1.6
- Disabled devel-static package
* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt4
- Fixed RPATH
- Disabled devel-static package

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt3
- Added -g into compiler flags

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Rebuilt for debuginfo

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6p1-alt6
- Fixed linking of libraries

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6p1-alt5
- Removed paths to buildroot

* Sun Aug 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6p1-alt4
- Added shared libraries

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6p1-alt3
- Rebuild with PIC
- Moved libTraceInput library into separate package
- Moved compiling scripts into devel package

* Wed Jun 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6p1-alt2
- Rebuild all java classes instead simple copying jar files
- Added sample and rlog trace library
- Resolved conflicts with tau

* Tue Jun 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6p1-alt1
- Initial build for Sisyphus

