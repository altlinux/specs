%filter_from_requires /^.usr.share.plplot.*.examples.tk.xtk01$/d
%def_enable docs
%def_without python3

Name: plplot
%define fmoddir %_libdir/fortran/modules/%name
Version: 5.11.1
Release: alt1
Summary: Scientific graphics plotting library, supporting multiple languages
License: LGPL v2 or later
Group: Graphics
Url: http://plplot.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://plplot.svn.sourceforge.net/svnroot/plplot/trunk
Source: %name-%version.tar.gz
Source1: CMakeCache.txt

# cmake 3.4 support
Patch0:         plplot-cmake34.patch
# cmake 3.7 support
Patch1:         plplot-cmake37.patch
Patch2:         plplot-multiarch.patch
# Don't use -custom with ocamlc
Patch7:         plplot-ocaml.patch

BuildPreReq: graphviz cmake swig gcc-fortran python-devel libgtk+3-devel
BuildPreReq: gcc-c++ libltdl7-devel libfreetype-devel libqhull-devel
BuildPreReq: libncurses-devel libgd2-devel tcl-devel tk-devel
BuildPreReq: python-module-pygtk-devel libnumpy-devel libgnomeui-devel
BuildPreReq: python-module-pygnome-devel
BuildPreReq: python-module-pygnome-canvas perl-XML-DOM liblasi-devel
BuildPreReq: libwxGTK3.1-devel liblapack-devel dri2proto
%if_enabled docs
BuildPreReq: texinfo openjade docbook-dtds OpenSP
BuildPreReq: docbook2X docbook-utils-print docbook-style-dsssl
BuildPreReq: docbook-style-xsl fonts-ttf-freefont docbook-simple
%endif
BuildPreReq: liblua5-devel qt4-devel libcairo-devel
BuildPreReq: python-module-PyQt4-devel sgml-common lua5 libpixman-devel
BuildPreReq: OpenSP fonts-ttf-freefont libopal-devel
BuildPreReq: python-module-sip-devel /proc glproto libXdmcp-devel
BuildPreReq: libXdamage-devel libXxf86vm-devel libshape-devel
BuildPreReq: libexpat-devel xmlto doxygen libharfbuzz-devel
BuildPreReq: fonts-ttf-freefont xvfb-run libxshmfence-devel
BuildPreReq: libharu-devel libagg-devel libshape-devel
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
%setup -q
%patch0 -p1 -b .cmake34
%patch1 -p1 -b .cmake37
%patch2 -p1 -b .multiarch
%patch7 -p1 -b .ocaml

# Installation directory has changed
sed -i -e 's,qhull/qhull_a.h,libqhull/qhull_a.h,' \
        lib/nn/delaunay.c \
        src/plgridd.c \
        cmake/modules/FindQHULL.cmake \
        doc/doxygen/html/delaunay_8c_source.html \
        doc/doxygen/html/plgridd_8c_source.html


install -m644 %SOURCE1 .

#sed -i 's|@PKG_CONFIG_PATH@|%buildroot%_pkgconfigdir|' \
#	examples/tk/Makefile.examples.in
#sed -i 's|@INCDIR@|%buildroot%_includedir/plplot|' \
#	examples/tk/Makefile.examples.in
#sed -i 's|@LIBDIR@|%buildroot%_libdir|' \
#	examples/tk/Makefile.examples.in
%ifarch x86_64
sed -i 's|lib/|%_lib/|g' CMakeCache.txt
%endif

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -I../../bindings/tk
%if_with python3
pushd ../python3
xvfb-run --server-args="-screen 0 1024x768x24" \
	cmake \
%ifarch x86_64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DPYTHON_EXECUTABLE:FILEPATH=%_bindir/python3 \
	-DPYTHON_INCLUDE_DIR:PATH=%{python3_includedir}mu \
	-DPYTHON_LIBRARY:FILEPATH=%_libdir/libpython%{_python3_version}mu.so \
	.

exit 1
%make_build VERBOSE=1
popd
%endif

xvfb-run --server-args="-screen 0 1024x768x24" \
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
#pushd examples/tk
#export LD_LIBRARY_PATH=%buildroot%_libdir
#%make -f Makefile.examples
#install -m755 xtk01 %buildroot%_bindir
#ln -s %_bindir/xtk01 %buildroot%_datadir/plplot%version/examples/tk
#popd

sed -i 's|%buildroot||g' \
	%buildroot%_datadir/plplot%version/examples/tk/Makefile

install -m755 scripts/plm2gif scripts/plpr \
	%buildroot%_bindir

rm -fR %buildroot%_docdir/%name \
	%buildroot%_datadir/%name%version/examples/test_octave_interactive.sh

mkdir docbook
cp doc/docbook/src/*.html docbook/
cp -fR doc/doxygen/html doxygen

%files
%doc AUTHORS COPYING* ChangeLog* Copyright FAQ NEWS PROBLEMS
%doc README* SERVICE ToDo
%_bindir/pltek
#%_bindir/plrender
%_bindir/plm2gif
%_bindir/plpr
%_bindir/wxPLViewer
%_man1dir/pltek.1*
#%_man1dir/plrender.1*
#%_man1dir/plm2gif.1*
#%_man1dir/plpr.1*
%_infodir/*

%if_enabled docs
%files doc
%doc docbook doxygen
%endif

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
%_libdir/libplplotcxx.so.*
%_libdir/libplplot.so.*
#_libdir/libplplotf77c.so.*
#_libdir/libplplotf77.so.*
%_libdir/libplplotf95c.so.*
%_libdir/libplplotf95.so.*
%_libdir/libqsastime.so.*
%dir %_libexecdir/plplot%version
%dir %_libexecdir/plplot%version/drivers
%_libexecdir/plplot%version/drivers/cairo.driver_info
%_libexecdir/plplot%version/drivers/cairo.so
%_libexecdir/plplot%version/drivers/mem.driver_info
%_libexecdir/plplot%version/drivers/mem.so
#_libdir/plplot%version/driversd/ntk.rc
#_libdir/plplot%version/driversd/ntk.so
%_libexecdir/plplot%version/drivers/null.driver_info
%_libexecdir/plplot%version/drivers/null.so
%_libexecdir/plplot%version/drivers/ps.driver_info
%_libexecdir/plplot%version/drivers/ps.so
%_libexecdir/plplot%version/drivers/pdf.driver_info
%_libexecdir/plplot%version/drivers/pdf.so
#_libdir/plplot%version/drivers/pstex.rc
#_libdir/plplot%version/drivers/pstex.so
%_libexecdir/plplot%version/drivers/psttf.driver_info
%_libexecdir/plplot%version/drivers/psttf.so
%_libexecdir/plplot%version/drivers/svg.driver_info
%_libexecdir/plplot%version/drivers/svg.so
%_libexecdir/plplot%version/drivers/xfig.driver_info
%_libexecdir/plplot%version/drivers/xfig.so
%_libexecdir/plplot%version/drivers/xwin.driver_info
%_libexecdir/plplot%version/drivers/xwin.so

%files -n lib%name-devel
%_includedir/*
%_libdir/libcsirocsa.so
%_libdir/libcsironn.so
%_libdir/libplplotcxx.so
%_libdir/libplplot.so
%_libdir/libqsastime.so
%_pkgconfigdir/plplot.pc
%_pkgconfigdir/plplot-c++.pc
%_datadir/plplot%version/examples/CMakeLists.txt
%dir %_datadir/plplot%version/examples/cmake
%dir %_datadir/plplot%version/examples/cmake/modules
#_datadir/plplot%version/examples/cmake/modules/FindPkgConfig.cmake
#_datadir/plplot%version/examples/cmake/modules/export_plplot-noconfig.cmake
#_datadir/plplot%version/examples/cmake/modules/export_plplot.cmake
%_datadir/plplot%version/examples/cmake/modules/language_support.cmake
#_datadir/plplot%version/examples/cmake/modules/language_support/
%_datadir/plplot%version/examples/cmake/modules/pkg-config.cmake
%_datadir/plplot%version/examples/cmake/modules/plplot_configure.cmake
%_datadir/plplot%version/examples/cmake/modules/plplot_functions.cmake
%_datadir/plplot%version/examples/cmake/modules/ndp_UseQt4.cmake
%_datadir/plplot%version/examples/c/
%_datadir/plplot%version/examples/c++/
%_datadir/plplot%version/examples/Makefile
%_datadir/plplot%version/examples/test_c.sh
%_datadir/plplot%version/examples/test_c_interactive.sh
%_datadir/plplot%version/examples/test_cxx.sh
%_datadir/plplot%version/examples/test_diff.sh
%_man3dir/pl*.3*
%_libdir/cmake

%files -n lib%name-fortran-devel
%dir %_libdir/fortran
%dir %_libdir/fortran/modules
%dir %_libdir/fortran/modules/plplot
%_libdir/fortran/modules/plplot/*.mod
#dir %_libdir/fortran/include
#_libdir/fortran/include/plplot
%fmoddir/plplot.mod
#%fmoddir/plplot_flt.mod
%fmoddir/plplotp.mod
%fmoddir/plf95demolib.mod
#_libdir/libplplotf77c.so
#_libdir/libplplotf77.so
%_libdir/libplplotf95c.so
%_libdir/libplplotf95.so
#_pkgconfigdir/plplot-f77.pc
%_pkgconfigdir/plplot-f95.pc
#_datadir/plplot%version/examples/f77/
%_datadir/plplot%version/examples/f95/
#_datadir/plplot%version/examples/test_f77.sh
%_datadir/plplot%version/examples/test_f95.sh

%files lua
%_libdir/lua/5.3/plplot/
%_datadir/plplot%version/examples/lua/
%_datadir/plplot%version/examples/test_lua.sh

%files -n lib%name-qt
%_libdir/libplplotqt.so.*
%_libexecdir/plplot%version/drivers/qt.driver_info
%_libexecdir/plplot%version/drivers/qt.so

%files -n lib%name-qt-devel
%_libdir/libplplotqt.so
%_pkgconfigdir/plplot-qt.pc

%files tk
%_bindir/plserver
%_bindir/pltcl
#%_bindir/xtk01
%_man1dir/plserver.1.*
%_man1dir/pltcl.1.*
%dir %_datadir/plplot%version
%dir %_datadir/plplot%version/examples
%_datadir/plplot%version/pkgIndex.tcl
%_datadir/plplot%version/examples/test_tcl.sh
%_datadir/plplot%version/examples/tcl/
%_datadir/plplot%version/examples/tk/
%_datadir/plplot%version/tcl/
%_datadir/plplot%version/*.tcl
%_datadir/plplot%version/*.sh?
%_datadir/plplot%version/*.fnt
#_datadir/plplot%version/*.map
%_datadir/plplot%version/*.pal
%_datadir/plplot%version/examples/lena.pgm
%_datadir/plplot%version/examples/plplot-test.sh
%_datadir/plplot%version/examples/plplot-test-interactive.sh


%files -n lib%name-tk
%_libdir/libplplottcltk.so.*
%_libdir/libtclmatrix.so.*
%_libdir/libplplottcltk_Main.so.*
%_libexecdir/plplot%version/drivers/tk.driver_info
%_libexecdir/plplot%version/drivers/tk.so
%_libexecdir/plplot%version/drivers/tkwin.driver_info
%_libexecdir/plplot%version/drivers/tkwin.so
%_libexecdir/plplot%version/drivers/ntk.so
%_libexecdir/plplot%version/drivers/ntk.driver_info

%files -n python-module-%name-tk
%python_sitelibdir/plplot_widgetmodule.so

%if_with python3
%files -n python3-module-%name-tk
%python3_sitelibdir/plplot_widgetmodule.so
%endif

%files -n lib%name-tk-devel
%_libdir/libplplottcltk.so
%_libdir/libtclmatrix.so
%_libdir/libplplottcltk_Main.so
%_pkgconfigdir/plplot-tcl.pc
%_pkgconfigdir/plplot-tcl_Main.pc

%files -n lib%name-wxGTK
%_libdir/libplplotwxwidgets.so.*
%_libexecdir/plplot%version/drivers/wxwidgets.driver_info
%_libexecdir/plplot%version/drivers/wxwidgets.so

%files -n lib%name-wxGTK-devel
%_libdir/libplplotwxwidgets.so
%_pkgconfigdir/plplot-wxwidgets.pc

%changelog
* Wed Feb 15 2017 Igor Vlasenko <viy@altlinux.ru> 5.11.1-alt1
- NMU: fixed build by updating to 5.11.1
- note: it is not a proper build.
  better to replace with import or find it proper maintainer

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt2.svn20140807
- New snapshot

* Tue Oct 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt2.svn20140707
- plplot-lua: added requirement on lua5.1-alt-compat (ALT #30379)

* Wed Jul 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt1.svn20140707
- New snapshot

* Sun Jun 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt1.svn20140521
- Version 5.10.0
- Built with wxGTK3.1

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.10-alt2.svn20131115
- Rebuilt with wxGTK3.0

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.10-alt1.svn20131115
- Version 5.9.10

* Fri Jul 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.9-alt5.svn20130315
- New snapshot

* Tue Mar 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.9-alt5.svn20121223
- Built without libgnomeprintui

* Tue Jan 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.9-alt4.svn20121223
- New snapshot

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.9.9-alt4.svn20120816
- New snapshot

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

