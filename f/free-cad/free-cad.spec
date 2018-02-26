%define oname freecad
%define ldir %_libexecdir/%oname

Name: free-cad
Version: 0.13.5438
Release: alt3.svn20120226
Summary: OpenSource 3D CAD modeller
License: GPL / LGPL
Group: Graphics
Url: http://free-cad.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# from .git/config :
#[svn-remote "svn"]
#  url = https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk
#  fetch = :refs/remotes/git-svn
Source: %name-%version.tar
Source1: CMakeCache.txt

Requires: lib%name = %version-%release

BuildPreReq: libGConf-devel libavformat53 libavcodec53
BuildPreReq: python-devel cmake swig gcc-fortran libf2c-ng-devel chrpath
BuildPreReq: boost-devel libqt4-devel libcoin3d-devel libSoQt-devel zlib-devel
BuildPreReq: libopencv2-devel libxerces-c-devel gcc-c++ boost-filesystem-devel
BuildPreReq: java-devel-default qt4-designer boost-program_options-devel
BuildPreReq: boost-signals-devel libXxf86misc-devel libqt4-sql-sqlite
BuildPreReq: libopencascade-devel libgts-devel libGL-devel libGLU-devel
BuildPreReq: libode-devel eigen2 phonon-devel libann-devel qt4-assistant
BuildPreReq: doxygen graphviz texlive-extra-utils libqt4-help eigen3
BuildPreReq: python-module-pivy libnumpy-devel libqt4-assistant-devel
%py_requires pivy
%py_provides Fem FreeCAD FreeCADGui Mesh Part MeshPart Drawing ImportGui
%py_provides PartGui Sketcher TestSketcherApp Robot RobotGui SketcherGui

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
Requires: %name = %version-%release

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
Requires: %name = %version-%release
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
BuildArch: noarch

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
Requires: %name = %version-%release

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
Requires: lib%name = %version-%release
Requires: libstdc++4.5-devel
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
install -p -m644 %SOURCE1 .
sed -i 's|@LIBDIR@|%_libdir|g' CMakeLists.txt CMakeCache.txt \
	src/3rdParty/salomesmesh/CMakeLists.txt
sed -i 's|@PYVER@|%_python_version|' \
	src/3rdParty/Pivy/CMakeLists.txt \
	src/3rdParty/Pivy-0.5/CMakeLists.txt
ln -s FindOpenCasCade.cmake cMake/FindOCE.cmake

%build
export PATH=$PATH:%_qt4dir/bin
./autogen.sh
cmake .
%make

optiSed() {
	sed -i 's|^\(CC.*\)|\1 -g -DBOOST_FILESYSTEM_VERSION=2|' Makefile
	sed -i 's|^\(CXX.*\)|\1 -g -DBOOST_FILESYSTEM_VERSION=2|g' Makefile
}

pushd src/Tools/plugins/widget
qmake-qt4 -Wall -d plugin.pro
optiSed
%make_build
popd
pushd src/Tools/ImageTools/ImageConv
qmake-qt4 -Wall -d ImageConv.pro
optiSed
%make_build
popd
pushd src/Gui/iisTaskPanel
qmake-qt4 -Wall -d taskpanel.pro
optiSed
%make_build
popd

%install
%makeinstall_std

install -d %buildroot%_bindir
install -d %buildroot%_libdir
ln -s %_libexecdir/%oname/bin/FreeCAD %buildroot%_bindir/%oname
ln -s %_libexecdir/%oname/bin/FreeCADCmd %buildroot%_bindir/%{oname}cmd
install -p -m755 package/debian/mime/%oname-thumbnailer \
	src/Tools/ImageTools/ImageConv/ImageConv \
	%buildroot%_bindir
cp -P src/Gui/iisTaskPanel/lib/* %buildroot%_libdir/

# qt4 designer

install -d %buildroot%_libexecdir/qt4/plugins/designer
install -p -m644 src/Tools/plugins/widget/*.so \
	%buildroot%_libexecdir/qt4/plugins/designer

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
# debian/menu - don't packaging?

# docs
install -d %buildroot%_man1dir
install -p -m644 package/debian/*.1 package/debian/mime/*.1 \
	%buildroot%_man1dir
pushd src/Doc
popd
#install -d %buildroot%_docdir/%name
#cp -fR Doc/SourceDocu/html %buildroot%_docdir/%name

install -d %buildroot%python_sitelibdir
install $(find ./ -name _coin.so) -m644 %buildroot%python_sitelibdir
install $(find ./ -name _soqt.so) -m644 %buildroot%python_sitelibdir

install -d %buildroot%_bindir
install -d %buildroot%_libexecdir/%oname/bin
pushd %buildroot%ldir/bin
for i in $(ls); do
	ln -s %ldir/bin/$i %buildroot%_bindir/
#ifarch x86_64
#	ln -s %ldir/bin/$i %buildroot%_libdir/%oname/bin/
#endif
done
popd

#ifarch x86_64
#mv %buildroot%_libdir/%oname/lib/* %buildroot%ldir/lib/
#endif

for i in %python_sitelibdir/_coin.so \
	%ldir/Mod/PartDesign/PartDesign.so
do
	chrpath -r %ldir/lib %buildroot$i
done
chrpath -d %buildroot%python_sitelibdir/_soqt.so

%find_lang --with-kde %name

%post
%gconf2_install %oname

%preun
if [ $1 = 0 ]; then
  %gconf2_uninstall %oname
fi

%files -f %name.lang
%doc ChangeLog.txt copying.lib package/debian/changelog
%dir %ldir
#exclude %_libdir/%oname/lib/Robot*
%_bindir/*
#ifarch x86_64
#_libdir/%oname
#endif
%ldir/bin
%ldir/Mod
%exclude %_bindir/freecad-thumbnailer
#exclude %ldir/bin/freecad-thumbnailer
%_desktopdir/*
%exclude %_desktopdir/fcstd-thumbnailer.desktop
%_niconsdir/*
%_man1dir/*
%exclude %_man1dir/freecad-thumbnailer.1*
%_xdgdatadir/mime/packages/*
%python_sitelibdir/*
%config %_sysconfdir/gconf/schemas/*
%ldir/data

%files thumbnailer
%_bindir/freecad-thumbnailer
#ldir/bin/freecad-thumbnailer
%_desktopdir/fcstd-thumbnailer.desktop
%_man1dir/freecad-thumbnailer.1*

%files -n lib%name
%_libdir/*.so.*
%ldir/lib

%files -n lib%name-devel
%_libdir/*.so
%ldir/include

#files docs
#_docdir/%name

%files qt4-designer-plugin
%_libexecdir/qt4/plugins/designer/*

%changelog
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
