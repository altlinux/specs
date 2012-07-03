%def_enable docs
%def_without python3

Name: plplot
%define fmoddir %_libdir/fortran/modules/%name
Version: 5.9.9
Release: alt4.svn20120228
Summary: Scientific graphics plotting library, supporting multiple languages
License: LGPL v2 or later
Group: Graphics
Url: http://plplot.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://plplot.svn.sourceforge.net/svnroot/plplot/trunk
Source: %name-%version.tar.gz
Source1: CMakeCache.txt

BuildPreReq: graphviz cmake swig gcc-fortran python-devel
BuildPreReq: gcc-c++ libltdl7-devel libfreetype-devel libqhull-devel
BuildPreReq: libncurses-devel libgd2-devel tcl-devel tk-devel
BuildPreReq: python-module-pygtk-devel libnumpy-devel libgnomeui-devel
BuildPreReq: libgnomeprintui-devel python-module-pygnome-devel
BuildPreReq: python-module-pygnome-canvas perl-XML-DOM liblasi-devel
BuildPreReq: libwxGTK2.9-devel liblapack-devel dri2proto
%if_enabled docs
BuildPreReq: texinfo openjade docbook-dtds OpenSP
BuildPreReq: docbook2X docbook-utils-print docbook-style-dsssl
BuildPreReq: docbook-style-xsl fonts-ttf-freefont docbook-simple
%endif
BuildPreReq: liblua5-devel qt4-devel libcairo-devel
BuildPreReq: python-module-PyQt4-devel sgml-common lua5 libpixman-devel
BuildPreReq: OpenSP fonts-ttf-freefont libopal-devel
BuildPreReq: python-module-sip-devel /proc glproto libXdmcp-devel
BuildPreReq: libXdamage-devel libXxf86vm-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel python-tools-2to3
BuildPreReq: python3-module-PyQt4-devel python3-module-sip-devel
%endif

Requires: lib%name = %version-%release

%description
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

The PLplot core library can be used to create standard x-y plots,
semi-log plots, log-log plots, contour plots, 3D surface plots, mesh
plots, bar charts and pie charts. Multiple graphs (of the same or
different sizes) may be placed on a single page, and multiple pages are
allowed for those device formats that support them.

PLplot device drivers support a number of different file formats for
non-interactive plotting and a number of different platforms that are
suitable for interactive plotting. It is easy to add new device drivers
to PLplot by writing a small number of device dependent routines.

%if_enabled docs
%package doc
Summary: Documentation for PLplot
Group: Documentation
BuildArch: noarch

%description doc
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains documentation for PLplot.
%endif

%package -n lib%name
Summary: Shared libraries of PLplot
Group: System/Libraries

%description -n lib%name
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains shared libraries of PLplot.

%package -n lib%name-devel
Summary: Development files of PLplot
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains development files of PLplot.

%package -n python-module-%name
Summary: Python module of PLplot
Group: Development/Python
Requires: lib%name = %version-%release
%py_provides pl

%description -n python-module-%name
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains python module of PLplot.

%if_with python3
%package -n python3-module-%name
Summary: Python 3 module of PLplot
Group: Development/Python3
Requires: lib%name = %version-%release
%py3_provides pl

%description -n python3-module-%name
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains python module of PLplot.
%endif

%package -n lib%name-fortran-devel
Summary: Development files for using PLplot Fortran bindings
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-fortran-devel
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains development files for using PLplot Fortran
bindings.

%package lua
Summary: Functions for scientific plotting with Lua
Group: Development/Other
Requires: %name = %version-%release

%description lua
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains functions for scientific plotting with Lua.

%package -n lib%name-qt
Summary: Functions for scientific plotting with Qt
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-qt
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains functions for scientific plotting with Qt.

%package -n lib%name-qt-devel
Summary: Development files for using PLplot with Qt
Group: Development/C++
Requires: lib%name-devel = %version-%release
Requires: lib%name-qt = %version-%release

%description -n lib%name-qt-devel
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains development files for using PLplot with Qt.

%package tk
Summary: Functions for scientific plotting with Tk
Group: Development/Tcl
Requires: lib%name = %version-%release
Requires: lib%name-tk = %version-%release
Requires: %name = %version-%release
Provides: tcl(Pltk) = %version-%release

%description tk
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains functions for scientific plotting with Tk.

%package -n lib%name-tk
Summary: Shared libraries with functions for scientific plotting with Tk
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-tk
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains shared libraries with functions for scientific
plotting with Tk.

%package -n lib%name-tk-devel
Summary: Development files of functions for scientific plotting with Tk
Group: Development/Tcl
Requires: lib%name = %version-%release
Requires: lib%name-tk = %version-%release

%description -n lib%name-tk-devel
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains development files of functions for scientific
plotting with Tk.

%package -n python-module-%name-tk
Summary: Python module with functions for scientific plotting with Tk
Group: Development/Python
Requires: lib%name = %version-%release
Requires: lib%name-tk = %version-%release

%description -n python-module-%name-tk
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains python module with functions for scientific
plotting with Tk.

%if_with python3
%package -n python3-module-%name-tk
Summary: Python 3 module with functions for scientific plotting with Tk
Group: Development/Python3
Requires: lib%name = %version-%release
Requires: lib%name-tk = %version-%release

%description -n python3-module-%name-tk
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains python module with functions for scientific
plotting with Tk.
%endif

%package -n lib%name-wxGTK
Summary: Functions for scientific plotting with wxGTK
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-wxGTK
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains functions for scientific plotting with wxGTK.

%package -n lib%name-wxGTK-devel
Summary: Development files of functions for scientific plotting with wxGTK
Group: Development/C++
Requires: lib%name = %version-%release
Requires: lib%name-wxGTK = %version-%release

%description -n lib%name-wxGTK-devel
PLplot is a cross-platform software package for creating scientific
plots. To help accomplish that task it is organized as a core C library,
language bindings for that library, and device drivers which control how
the plots are presented in non-interactive and interactive plotting
contexts.

This package contains development files of functions for scientific
plotting with wxGTK.

%prep
%setup
install -m644 %SOURCE1 .

sed -i 's|@PKG_CONFIG_PATH@|%buildroot%_pkgconfigdir|' \
	examples/tk/Makefile.examples.in
sed -i 's|@INCDIR@|%buildroot%_includedir/plplot|' \
	examples/tk/Makefile.examples.in
sed -i 's|@LIBDIR@|%buildroot%_libdir|' \
	examples/tk/Makefile.examples.in

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%if_with python3
pushd ../python3
cmake \
%ifarch x86_64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DPYTHON_EXECUTABLE:FILEPATH=%_bindir/python3 \
	-DPYTHON_INCLUDE_DIR:PATH=%{python3_includedir}mu \
	-DPYTHON_LIBRARY:FILEPATH=%_libdir/libpython%{_python3_version}mu.so \
	.

%make_build VERBOSE=1
popd
%endif

cmake \
%ifarch x86_64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	.

%make_build VERBOSE=1

#%if_enabled docs
#pushd doc
#doxygen
#popd
#%endif

%install
%if_with python3
pushd ../python3
%make_install DESTDIR=$PWD/build3 install
install -d %buildroot%python3_sitelibdir
mv build3%python3_sitelibdir/* %buildroot%python3_sitelibdir/
popd
for i in $(find %buildroot%python3_sitelibdir -name '*.py'); do
	2to3 -w -n $i
	sed -i 's|%_bindir/env python|%_bindir/env python3|' $i
done
%endif

%makeinstall_std

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
mv %buildroot%_libdir/plplot%version %buildroot%_libexecdir/
%endif

# Examples
pushd examples/tk
export LD_LIBRARY_PATH=%buildroot%_libdir
%make -f Makefile.examples
install -m755 xtk01 %buildroot%_bindir
ln -s %_bindir/xtk01 %buildroot%_datadir/plplot%version/examples/tk
popd

sed -i 's|%buildroot||g' \
	%buildroot%_datadir/plplot%version/examples/tk/Makefile

install -m755 scripts/plm2gif scripts/plpr \
	%buildroot%_bindir

rm -fR %buildroot%_docdir/%name \
	%buildroot%_datadir/%name%version/examples/test_octave_interactive.sh

%files
%doc AUTHORS COPYING* ChangeLog* Copyright FAQ NEWS PROBLEMS
%doc README* SERVICE ToDo
%_bindir/pltek
%_bindir/plrender
%_bindir/plm2gif
%_bindir/plpr
%_man1dir/pltek.1*
%_man1dir/plrender.1*
%_man1dir/plm2gif.1*
%_man1dir/plpr.1*
%_infodir/*

#%if_enabled docs
#%files doc
#%doc doc/doxygen/html/*
#%endif

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/plplot_widgetmodule.so
%_datadir/plplot%version/examples/python/
%_datadir/plplot%version/examples/test_python.sh

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/plplot_widgetmodule.so
%endif

%files -n lib%name
%dir %_datadir/plplot%version
%dir %_datadir/plplot%version/examples
%_libdir/libcsirocsa.so.*
%_libdir/libcsironn.so.*
%_libdir/libplplotcxxd.so.*
%_libdir/libplplotd.so.*
%_libdir/libplplotf77cd.so.*
%_libdir/libplplotf77d.so.*
%_libdir/libplplotf95cd.so.*
%_libdir/libplplotf95d.so.*
%_libdir/libqsastime.so.*
%dir %_libexecdir/plplot%version
%dir %_libexecdir/plplot%version/driversd
%_libexecdir/plplot%version/driversd/cairo.driver_info
%_libexecdir/plplot%version/driversd/cairo.so
%_libexecdir/plplot%version/driversd/mem.driver_info
%_libexecdir/plplot%version/driversd/mem.so
#_libdir/plplot%version/driversd/ntk.rc
#_libdir/plplot%version/driversd/ntk.so
%_libexecdir/plplot%version/driversd/null.driver_info
%_libexecdir/plplot%version/driversd/null.so
%_libexecdir/plplot%version/driversd/ps.driver_info
%_libexecdir/plplot%version/driversd/ps.so
#_libdir/plplot%version/driversd/pstex.rc
#_libdir/plplot%version/driversd/pstex.so
%_libexecdir/plplot%version/driversd/psttf.driver_info
%_libexecdir/plplot%version/driversd/psttf.so
%_libexecdir/plplot%version/driversd/svg.driver_info
%_libexecdir/plplot%version/driversd/svg.so
%_libexecdir/plplot%version/driversd/xfig.driver_info
%_libexecdir/plplot%version/driversd/xfig.so
%_libexecdir/plplot%version/driversd/xwin.driver_info
%_libexecdir/plplot%version/driversd/xwin.so

%files -n lib%name-devel
%_includedir/*
%_libdir/libcsirocsa.so
%_libdir/libcsironn.so
%_libdir/libplplotcxxd.so
%_libdir/libplplotd.so
%_libdir/libqsastime.so
%_pkgconfigdir/plplotd.pc
%_pkgconfigdir/plplotd-c++.pc
%_datadir/plplot%version/examples/CMakeLists.txt
%dir %_datadir/plplot%version/examples/cmake
%dir %_datadir/plplot%version/examples/cmake/modules
#_datadir/plplot%version/examples/cmake/modules/FindPkgConfig.cmake
%_datadir/plplot%version/examples/cmake/modules/export_plplot-noconfig.cmake
%_datadir/plplot%version/examples/cmake/modules/export_plplot.cmake
%_datadir/plplot%version/examples/cmake/modules/language_support.cmake
#_datadir/plplot%version/examples/cmake/modules/language_support/
%_datadir/plplot%version/examples/cmake/modules/pkg-config.cmake
%_datadir/plplot%version/examples/cmake/modules/plplot_configure.cmake
%_datadir/plplot%version/examples/cmake/modules/plplot_functions.cmake
%_datadir/plplot%version/examples/c/
%_datadir/plplot%version/examples/c++/
%_datadir/plplot%version/examples/Makefile
%_datadir/plplot%version/examples/test_c.sh
%_datadir/plplot%version/examples/test_c_interactive.sh
%_datadir/plplot%version/examples/test_cxx.sh
%_datadir/plplot%version/examples/test_diff.sh
%_man3dir/pl*.3*

%files -n lib%name-fortran-devel
%dir %_libdir/fortran
%dir %_libdir/fortran/modules
%dir %_libdir/fortran/modules/plplot
%dir %_libdir/fortran/include
%_libdir/fortran/include/plplot
%fmoddir/plplot.mod
%fmoddir/plplot_flt.mod
%fmoddir/plplotp.mod
%fmoddir/plf95demolib.mod
%_libdir/libplplotf77cd.so
%_libdir/libplplotf77d.so
%_libdir/libplplotf95cd.so
%_libdir/libplplotf95d.so
%_pkgconfigdir/plplotd-f77.pc
%_pkgconfigdir/plplotd-f95.pc
%_datadir/plplot%version/examples/f77/
%_datadir/plplot%version/examples/f95/
%_datadir/plplot%version/examples/test_f77.sh
%_datadir/plplot%version/examples/test_f95.sh

%files lua
%dir %_libdir/lua
%dir %_libdir/lua/5.1
%_libdir/lua/5.1/plplot/
%_datadir/plplot%version/examples/lua/
%_datadir/plplot%version/examples/test_lua.sh

%files -n lib%name-qt
%_libdir/libplplotqtd.so.*
%_libexecdir/plplot%version/driversd/qt.driver_info
%_libexecdir/plplot%version/driversd/qt.so

%files -n lib%name-qt-devel
%_libdir/libplplotqtd.so
%_pkgconfigdir/plplotd-qt.pc

%files tk
%_bindir/plserver
%_bindir/pltcl
%_bindir/xtk01
%_man1dir/plserver.1.gz
%_man1dir/pltcl.1.gz
%dir %_datadir/plplot%version
%dir %_datadir/plplot%version/examples
%_datadir/plplot%version/pkgIndex.tcl
%_datadir/plplot%version/examples/test_tcl.sh
%_datadir/plplot%version/examples/tcl/
%_datadir/plplot%version/examples/tk/
%_datadir/plplot%version/tcl/
%_datadir/plplot%version/*.fnt
%_datadir/plplot%version/*.map
%_datadir/plplot%version/*.pal
%_datadir/plplot%version/examples/lena.pgm
%_datadir/plplot%version/examples/plplot-test.sh
%_datadir/plplot%version/examples/plplot-test-interactive.sh


%files -n lib%name-tk
%_libdir/libplplottcltkd.so.*
%_libdir/libtclmatrixd.so.*
%_libexecdir/plplot%version/driversd/tk.driver_info
%_libexecdir/plplot%version/driversd/tk.so
%_libexecdir/plplot%version/driversd/tkwin.driver_info
%_libexecdir/plplot%version/driversd/tkwin.so

%files -n python-module-%name-tk
%python_sitelibdir/plplot_widgetmodule.so

%if_with python3
%files -n python3-module-%name-tk
%python3_sitelibdir/plplot_widgetmodule.so
%endif

%files -n lib%name-tk-devel
%_libdir/libplplottcltkd.so
%_libdir/libtclmatrixd.so
%_pkgconfigdir/plplotd-tcl.pc

%files -n lib%name-wxGTK
%_libdir/libplplotwxwidgetsd.so.*
%_libexecdir/plplot%version/driversd/wxwidgets.driver_info
%_libexecdir/plplot%version/driversd/wxwidgets.so

%files -n lib%name-wxGTK-devel
%_libdir/libplplotwxwidgetsd.so
%_pkgconfigdir/plplotd-wxwidgets.pc

%changelog
* Sat May 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.9-alt4.svn20120228
- Rebuilt with new wxGTK 2.9

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 5.9.9-alt3.svn20120228
- Rebuilt with liblasi-1.1.1

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.9-alt2.svn20120228
- Rebuilt with qhull 2012.1

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.9-alt1.svn20120228
- New snapshot

* Sat Dec 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.9-alt1.svn20111215
- Version 5.9.9

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.7-alt2.svn20110504
- Rebuilt with qhull 2011.2
- Enabled docs

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.9.7-alt1.svn20110504.1.1
- Rebuild with Python-2.7

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.7-alt1.svn20110504.1
- Rebuilt with updated wxGKT2.9

* Fri May 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.7-alt1.svn20110504
- Version 5.9.7

* Thu May 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.11
- Rebuilt with qhull 2011.1

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.10
- Built with GotoBLAS2 instead of ATLAS

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.9
- Rebuilt with wxGTK2.9 2.9.2-alt1.svn20110322

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.8
- Rebuilt with wxGTK2.9 2.9.2-alt1.svn20110312

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.7
- Rebuilt for debuginfo
- Enabled PyQt4 interface

* Sun Dec 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.6
- Fixed build

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.5
- Rebuilt for soname set-versions

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.4
- Added necessary executables and man pages
- Moved some files from %name into %name-tk

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.3
- Moved plugins into %_libexecdir/plplot%version (ALT #24377)

* Fri Oct 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.2
- Fixed underlinking of libraries

* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915.1
- Avoid unowned directories
- Removed buildroot from Makefile of Tk examples

* Thu Sep 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.6-alt1.svn20100915
- Initial build for Sisyphus (based on spec from Fedora)

