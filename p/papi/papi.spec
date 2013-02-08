Name: papi
License: BSD-like
Group: Development/Tools
Summary: Performance Application Programming Interface
Version: 5.1.0.2
Release: alt1
Url: http://icl.cs.utk.edu/papi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz
Patch: papi-5.0.1-alt-i586.patch

Requires: lib%name = %version-%release

BuildPreReq: libncurses-devel gcc-fortran /proc libsensors3-devel
BuildPreReq: libltdl-devel doxygen graphviz

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

%package doc
Summary: Documentation for Performance Application Programming Interface
Group: Documentation
#BuildArch: noarch

%description doc
PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter hardware
found in most major microprocessors. PAPI enables software engineers to see, in
near real time, the relation between software performance and processor events.

This package contains documentation for PAPI.

%prep
%setup
#ifarch %ix86
#patch -p1
#endif

rm -fR src/perfctr-*
cp -f src/Rules.pfm src/Rules.perfctr
cp -f src/Rules.pfm src/Rules.perfctr-pfm

%build
cd src

pushd components/lmsensors
%autoreconf
%configure \
	--with-sensors_incdir=%_includedir/sensors \
	--with-sensors_libdir=%_libdir
popd

#cp Makefile.inc Makefile.inc.bak
#sed -i -e 's/\-Werror//g' libpfm-3.?/config.mk
%add_optflags %optflags_shared
%autoreconf
%configure \
%ifarch x86_64
	--with-bitmode=64 \
%else
	--with-bitmode=32 \
%endif
	--with-ffsll \
	--with-static-lib=no \
	--with-virtualtimer=clock_thread_cputime_id \
	--with-perf-events \
	--with-libpfm3 \
	--with-components="appio coretemp lmsensors mx net rapl stealtime"
#cp -f Makefile.inc.bak Makefile.inc
#make libpapi.a
%make_build

%make -C ../doc html man

%install
cd src
%makeinstall_std
%make_install DESTDIR=%buildroot install-man

install -d %buildroot%_docdir/%name
cp -fR ../doc/html/* %buildroot%_docdir/%name/

ln -s libpapi.so %buildroot%_libdir/libpapi64.so
ln -s libpfm.so %buildroot%_libdir/libpfm64.so

%files
%doc *.txt README
%_bindir/*
%_man1dir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

%files doc
%_docdir/%name

%changelog
* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.0.2-alt1
- Version 5.1.0.2

* Thu Nov 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.1-alt1
- Version 5.0.1

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt1
- Version 5.0.0

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt2
- Fixed build with new glibc

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

