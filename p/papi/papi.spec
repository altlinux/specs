Name: papi
License: BSD-like
Group: Development/Tools
Summary: Performance Application Programming Interface
Version: 4.2.1
Release: alt1
Url: http://icl.cs.utk.edu/papi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: libncurses-devel gcc-fortran /proc
BuildPreReq: libltdl-devel

%description
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

%package -n lib%name
Summary: Shared libraries of PAPI (Performance Application Programming Interface)
Group: System/Libraries

%description -n lib%name
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains shared libraries of PAPI.

%package -n lib%name-devel
Summary: Development files of Performance Application Programming Interface
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains development files of PAPI.

%package -n lib%name-devel-static
Summary: Static libraries of Performance Application Programming Interface
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains static libraries of PAPI.

%package doc
Summary: Documentation for Performance Application Programming Interface
Group: Documentation
BuildArch: noarch

%description doc
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains documentation for PAPI.

%prep
%setup

rm -fR src/perfctr-*
cp -f src/Rules.pfm src/Rules.perfctr
cp -f src/Rules.pfm src/Rules.perfctr-pfm

%build
cd src
cp Makefile.inc Makefile.inc.bak
sed -i -e 's/\-Werror//g' libpfm-3.?/config.mk
%add_optflags %optflags_shared
%autoreconf
%configure --with-ffsll \
	--with-static-lib=no \
	--with-virtualtimer=clock_thread_cputime_id \
	--with-perf-events \
	--with-libpfm3
#cp -f Makefile.inc.bak Makefile.inc
%make libpapi.a
%make

%install
cd src
%makeinstall_std

#rm -f %buildroot%_bindir/perfex %buildroot%_includedir/*perfctr* \
#	%buildroot%_libdir/libperfctr.*

ln -s libpapi.so %buildroot%_libdir/libpapi64.so
ln -s libpfm.so %buildroot%_libdir/libpfm64.so
#ln -s libpapi.a %buildroot%_libdir/libpapi64.a
#ln -s libpfm.a %buildroot%_libdir/libpfm64.a

%files
%doc *.txt
%_bindir/*
%_man1dir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

#files -n lib%name-devel-static
#_libdir/*.a

#files doc
#_docdir/%name

%changelog
* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt2
- Removed setting of RPATH

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Version 4.2.0

* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2.1-alt1
- Version 4.1.2.1
- Disabled devel-static subpackage

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2
- Rebuilt for soname set-versions

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0
- Built with PerfCtr 2.6.41

* Sat Jan 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt6
- Rebuild with PerfCtr 2.6.40

* Thu Jun 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt5
- Rebuild with PerfCtr 2.6.39

* Fri Jun 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt4
- Rebuild with PIC

* Thu Jun 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt3
- Add links libpapi64.*

* Fri May 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt2
- Rebuild with PerfCtr 2.6.38

* Tue May 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Initial build for Sisyphus

