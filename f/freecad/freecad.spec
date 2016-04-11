%define oname freecad
%define ldir %_libdir/%oname

Name:    freecad
Version: 0.16
Release: alt1
Epoch:   1
Summary: OpenSource 3D CAD modeller
License: GPL / LGPL
Group:   Graphics
Url:     http://free-cad.sourceforge.net/
# VCS:   https://github.com/FreeCAD/FreeCAD
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

Patch1: %name-fix-circular-cmake-call.patch
Patch2: %name-fix-ImageConv-build.patch

Provides:  free-cad = %version-%release
Obsoletes: free-cad < %version-%release
Requires:  lib%name = %EVR

BuildPreReq: libGConf-devel pyside-tools
BuildPreReq: python-devel cmake swig gcc-fortran libf2c-ng-devel chrpath
BuildPreReq: boost-devel libqt4-devel libcoin3d-devel libSoQt-devel zlib-devel
BuildPreReq: libopencv2-devel libxerces-c-devel gcc-c++ boost-filesystem-devel
BuildPreReq: java-devel-default qt4-designer boost-program_options-devel
BuildPreReq: boost-signals-devel libXxf86misc-devel libqt4-sql-sqlite
BuildPreReq: libopencascade-devel libgts-devel libGL-devel libGLU-devel
BuildPreReq: libode-devel phonon-devel libann-devel qt4-assistant
BuildPreReq: doxygen graphviz libqt4-help eigen3
BuildPreReq: python-module-pivy libnumpy-devel libqt4-assistant-devel
BuildPreReq: boost-interprocess-devel libshiboken-devel shiboken
BuildPreReq: libpyside-qt4-devel boost-python-devel
BuildRequires: gdb
#BuildRequires: texlive-extra-utils

%py_requires pivy PySide
%py_provides Fem FreeCAD FreeCADGui Mesh Part MeshPart Drawing ImportGui
%py_provides PartGui Sketcher TestSketcherApp Robot RobotGui SketcherGui
%py_provides ImageGui PartDesignGui _PartDesign
%add_python_req_skip pyopencl IfcImport Units
%add_findreq_skiplist %ldir/Mod/*

%description
FreeCAD will be a general purpose 3D CAD modeler. FreeCAD is aimed directly at
mechanical engineering and product design but also fits in a wider range of uses
around engineering, such as architecture or other engineering specialties.

FreeCAD features tools similar to Catia, SolidWorks or Solid Edge, and therefore
also falls into the category of MCAD, PLM, CAx and CAE. It will be a feature
based parametric modeler with a modular software architecture which makes it
easy to provide additional functionality without modifying the core system.

%package thumbnailer
Summary: Thumbnailer utility for FreeCAD
Group: Graphics
Provides:  free-cad-thumbnailer = %version-%release
Obsoletes: free-cad-thumbnailer < %version-%release
Requires: %name = %EVR

%description thumbnailer
FreeCAD will be a general purpose 3D CAD modeler. FreeCAD is aimed directly at
mechanical engineering and product design but also fits in a wider range of uses
around engineering, such as architecture or other engineering specialties.

FreeCAD features tools similar to Catia, SolidWorks or Solid Edge, and therefore
also falls into the category of MCAD, PLM, CAx and CAE. It will be a feature
based parametric modeler with a modular software architecture which makes it
easy to provide additional functionality without modifying the core system.

This package contains thumbnailer utility for FreeCAD.

%package qt4-designer-plugin
Summary: FreeCAD plugin for Qt4
Group: Development/KDE and QT
Provides:  free-cad-qt4-designer-plugin = %version-%release
Obsoletes: free-cad-qt4-designer-plugin < %version-%release
Requires: %name = %EVR
Requires: qt4-designer

%description qt4-designer-plugin
FreeCAD will be a general purpose 3D CAD modeler. FreeCAD is aimed directly at
mechanical engineering and product design but also fits in a wider range of uses
around engineering, such as architecture or other engineering specialties.

FreeCAD features tools similar to Catia, SolidWorks or Solid Edge, and therefore
also falls into the category of MCAD, PLM, CAx and CAE. It will be a feature
based parametric modeler with a modular software architecture which makes it
easy to provide additional functionality without modifying the core system.

This package contains FreeCAD plugin for Qt4 Designer.

%package docs
Summary: Documentation for FreeCAD
Group: Documentation
#BuildArch: noarch
Provides:  free-cad-docs = %version-%release
Obsoletes: free-cad-docs < %version-%release
Requires: qt4-assistant

%description docs
FreeCAD will be a general purpose 3D CAD modeler. FreeCAD is aimed directly at
mechanical engineering and product design but also fits in a wider range of uses
around engineering, such as architecture or other engineering specialties.

FreeCAD features tools similar to Catia, SolidWorks or Solid Edge, and therefore
also falls into the category of MCAD, PLM, CAx and CAE. It will be a feature
based parametric modeler with a modular software architecture which makes it
easy to provide additional functionality without modifying the core system.

This package contains documentation for FreeCAD.

%package -n lib%name
Summary: Shared libraries of FreeCAD
Group: System/Libraries
Provides:  libfree-cad = %version-%release
Obsoletes: libfree-cad < %version-%release
Requires: %name = %EVR

%description -n lib%name
FreeCAD will be a general purpose 3D CAD modeler. FreeCAD is aimed directly at
mechanical engineering and product design but also fits in a wider range of uses
around engineering, such as architecture or other engineering specialties.

FreeCAD features tools similar to Catia, SolidWorks or Solid Edge, and therefore
also falls into the category of MCAD, PLM, CAx and CAE. It will be a feature
based parametric modeler with a modular software architecture which makes it
easy to provide additional functionality without modifying the core system.

This package contains shared libraries FreeCAD.

%package -n lib%name-devel
Summary: Development files of FreeCAD
Group: Development/C++
Provides:  libfree-cad-devel = %version-%release
Obsoletes: libfree-cad-devel < %version-%release
Requires: lib%name = %EVR
Requires: libopencascade-devel

%description -n lib%name-devel
FreeCAD will be a general purpose 3D CAD modeler. FreeCAD is aimed directly at
mechanical engineering and product design but also fits in a wider range of uses
around engineering, such as architecture or other engineering specialties.

FreeCAD features tools similar to Catia, SolidWorks or Solid Edge, and therefore
also falls into the category of MCAD, PLM, CAx and CAE. It will be a feature
based parametric modeler with a modular software architecture which makes it
easy to provide additional functionality without modifying the core system.

This package contains development files of FreeCAD.

%prep
%setup
%patch1 -p1
%patch2 -p1
sed -i 's|@LIBDIR@|%_libdir|g' CMakeLists.txt \
	src/3rdParty/salomesmesh/CMakeLists.txt
ln -s FindOpenCasCade.cmake cMake/FindOCE.cmake

%build
export PATH=$PATH:%_qt4dir/bin
%add_optflags -Wl,-rpath,%ldir/lib
%cmake_insource \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_DATADIR=%ldir \
	-DCMAKE_INSTALL_DOCDIR=%ldir/doc \
	-DCMAKE_INSTALL_LIBDIR=%ldir/lib \
	-DFREECAD_USE_EXTERNAL_PIVY=ON 

%make_build

optiSed() {
	sed -i 's|^\(CC.*\)|\1 -g|' Makefile
	sed -i 's|^\(CXX.*\)|\1 -g|g' Makefile
}

pushd src/Tools/plugins/widget
%qmake_qt4 -Wall -d plugin.pro
optiSed
%make_build
popd
pushd src/Tools/ImageTools/ImageConv
%qmake_qt4 -Wall -d ImageConv.pro
optiSed
%make_build
popd
pushd src/Gui/iisTaskPanel
%qmake_qt4 -Wall -d taskpanel.pro
optiSed
%make_build
popd

%install
%makeinstall_std

# binaries
install -d %buildroot%ldir/bin
if [ -d %buildroot%_bindir ] ; then
mv -v %buildroot%_bindir/* %buildroot%ldir/bin
fi
pushd %buildroot%ldir/bin
for i in $(ls); do
	ln -s %ldir/bin/$i %buildroot%_bindir/
done
ln -s FreeCAD %buildroot%_bindir/%oname
ln -s FreeCADCmd %buildroot%_bindir/%{oname}cmd
popd

# libraries
install -d %buildroot%_libdir
install -p -m755 package/debian/mime/%oname-thumbnailer \
	src/Tools/ImageTools/ImageConv/ImageConv \
	%buildroot%_bindir
cp -P src/Gui/iisTaskPanel/lib/* %buildroot%_libdir/

# qt4 designer
install -d %buildroot%_qt4dir/plugins/designer
install -p -m644 src/Tools/plugins/widget/*.so \
	%buildroot%_qt4dir/plugins/designer

# desktop files
install -d %buildroot%_sysconfdir/gconf/schemas
install -p -m755 package/debian/mime/*.schemas \
	%buildroot%_sysconfdir/gconf/schemas
install -d %buildroot%_desktopdir
install -p -m644 package/debian/*.desktop %buildroot%_desktopdir
install -d %buildroot%_niconsdir
install -p -m644 src/Gui/Icons/freecad.xpm %buildroot%_niconsdir
install -d %buildroot%_xdgdatadir/mime/packages
install -p -m644 package/debian/%oname.sharedmimeinfo \
	%buildroot%_xdgdatadir/mime/packages/%oname.xml

# docs
install -d %buildroot%_man1dir
install -p -m644 package/debian/*.1 package/debian/mime/*.1 \
	%buildroot%_man1dir

# stuff
cp -af %buildroot%_prefix/Mod/* %buildroot%ldir/Mod
rm -rf %buildroot%_prefix/Mod

# cleanup
rm -f %buildroot%_libdir/libiistaskpanel.so

# l10n
%find_lang --with-kde %name

%post
%gconf2_install %oname

%preun
if [ $1 = 0 ]; then
  %gconf2_uninstall %oname
fi

%files -f %name.lang
%doc ChangeLog.txt copying.lib package/debian/changelog
%doc %ldir/License.txt
%dir %ldir
%_bindir/*
%ldir/bin
%ldir/Gui
%ldir/Mod
%ldir/examples
%ldir/*.png
%ldir/*.svg
%ldir/*.xpm
%exclude %_bindir/freecad-thumbnailer
%_desktopdir/*
%_niconsdir/*
%_man1dir/*
%exclude %_man1dir/freecad-thumbnailer.1*
%_xdgdatadir/mime/packages/*
#python_sitelibdir/*
%config %_sysconfdir/gconf/schemas/*

%files thumbnailer
%_bindir/freecad-thumbnailer
%_man1dir/freecad-thumbnailer.1*

%files -n lib%name
%_libdir/*.so.*
%ldir/lib

#files -n lib%name-devel
#_libdir/*.so
#ldir/include

%files docs
%ldir/doc

%files qt4-designer-plugin
%_qt4dir/plugins/designer/*.so

%changelog
* Mon Apr 11 2016 Andrey Cherepanov <cas@altlinux.org> 1:0.16-alt1
- New version
- Add boost-python-devel to build requirements

* Thu Dec 10 2015 Andrey Cherepanov <cas@altlinux.org> 1:0.15-alt1
- New version (ALT #31511)
- Rename free-cad to freecad

* Sun Dec 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.14.0-alt1.git20141214
- Version 0.14.0 (ALT #30563)

* Wed Jul 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.13.0-alt1.git20140701
- New snapshot

* Thu May 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.13.0-alt1.git20140521
- New snapshot

* Tue Nov 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.13.0-alt1.git20131111
- New snapshot

* Fri Sep 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.13.0-alt1.git20130912
- Version 0.13.0

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.12.2237-alt3.git20130123
- Rebuilt with Boost 1.53.0

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.12.2237-alt2.git20130123
- Rebuilt with OpenCASCADE 6.5.4

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.12.2237-alt1.git20130123
- Version 0.12.2237 (from git)

* Tue Dec 04 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.13.5443-alt5.svn20120331
- Rebuild with new libxerces-c

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5443-alt4.svn20120331
- Rebuilt with Boost 1.52.0

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5443-alt3.svn20120331
- Fixed build with gcc 4.7

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5443-alt2.svn20120331
- Rebuilt with Boost 1.51.0

* Wed Aug 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5443-alt1.svn20120331
- Version 0.13.5443

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5438-alt3.svn20120226
- Rebuilt with Boost 1.49.0

* Tue Mar 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5438-alt2.svn20120226
- Built with Eigen3

* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5438-alt1.svn20120226
- Version 0.13.5438

* Wed Jan 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5214-alt2.svn20111203
- Fixed build with new Mesa

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.5214-alt1.svn20111203
- Version 0.13.5214

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.2237-alt1.svn20110830.1.1
- Rebuild with Python-2.7

* Thu Sep 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2237-alt1.svn20110830.1
- Rebuilt with OpenCASCADE 6.5.1

* Thu Sep 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2237-alt1.svn20110830
- New snapshot

* Wed Jul 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2237-alt1.svn20110501.1
- Rebuilt with Boost 1.47.0

* Tue May 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2237-alt1.svn20110501
- Version 0.12.2237

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.5
- Rebuilt with Boost 1.46.1

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.4
- Really rebuilt for debuginfo

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.3
- Rebuilt with debuginfo
- Fixed build with Boost 1.46.0

* Thu Jan 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.2
- Extracted freecad-thumbnailer into separate package

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120.1
- Rebuilt with set-versioned libxerces-c

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3752-alt1.svn20101120
- Version 0.11.3752

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3340-alt1.svn20100725.1
- Rebuilt for soname set-versions

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3340-alt1.svn20100725
- Version 0.10.3340

* Fri Mar 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3017-alt1.svn20100308.1
- Built with libopencv4

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3017-alt1.svn20100308
- Version 0.9.3017

* Fri Jan 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2237-alt1.svn20091224
- Initial build for Sisyphus
