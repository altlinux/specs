%define _unpackaged_files_terminate_build 1
%add_python3_path %_libdir/freecad/Mod %_libdir/freecad/Ext/*
%add_python3_req_skip FreeCADGui FreeCAD
%ifnarch %qt6_qtwebengine_arches
%add_python3_req_skip PySide6.QtWebEngineCore PySide6.QtWebEngineWidgets
%endif
%add_findprov_skiplist %_libdir/freecad/Mod/* %_libdir/freecad/Ext/*
%def_with bundled_libs
%def_without bundled_pycxx
%def_with glvnd
%def_with ninja
%def_with pybind11
%def_with pyside

%define oname freecad
%define ldir %_libdir/%oname
%ifndef build_parallel_jobs
%define build_parallel_jobs 7
%endif
%define git_rev b9bfa5c550
%define git_date 13.11.2023

Name:    freecad
Version: 0.21.2
Release: alt7.2
Epoch:   1
Summary: OpenSource 3D CAD modeller
License: LGPL-2.0+
Group:   Graphics
Url:     http://free-cad.sourceforge.net/
# VCS:   https://github.com/FreeCAD/FreeCAD
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: freecad.1

%if_without bundled_libs
Patch1: %name-remove-3rdParty.patch
%endif
Patch2: freecad-0.19.2-alt-boost-link.patch
Patch3: freecad-alt-fix-icon-name-in-menu.patch
Patch4: freecad-unbundled-pycxx.patch
Patch5: freecad-vtk9.3.patch

# https://github.com/FreeCAD/FreeCAD/pull/13570
Patch6: freecad-upstream-pr13570-fix-for-boost-1.85.0.patch

# Part of https://github.com/FreeCAD/FreeCAD/pull/13226
# fixes build with boost 1.85.0+
Patch7: freecad-upstream-fix-copy-option-deprecation.patch

# Gentoo
Patch20: freecad-0.21.2-navcube-qt6.patch
Patch21: freecad-0.21.2-qtsvg-qt6.patch
Patch22: freecad-0.21.2-shiboken-6.7.0.patch

Provides:  free-cad = %version-%release
Obsoletes: free-cad < %version-%release

ExcludeArch: %ix86 armh ppc64le

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-macros-qt6-webengine
%if_with ninja
BuildRequires(pre): rpm-build-ninja
%endif
BuildRequires(pre): rpm-build-python3
BuildRequires: qt6-base-devel
BuildRequires: qt6-assistant
BuildRequires: qt6-designer
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel
%endif
%if_with pyside
BuildRequires: python3-module-pyside6
BuildRequires: python3-module-pyside6-devel
BuildRequires: python3-module-shiboken6-devel
BuildRequires: python3-module-pivy
%else
%filter_from_requires /python3(PySide2/d
%endif
%define qmake %qmake_qt6
%define qtbindir %_qt6_bindir
BuildRequires: python3-devel swig gcc-fortran chrpath
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-geometry-devel
BuildRequires: boost-polygon-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-python3-devel
BuildRequires: boost-signals-devel
BuildRequires: libcoin3d-devel
#BuildRequires: libSoQt-devel
BuildRequires: zlib-devel
BuildRequires: libopencv2-devel libxerces-c-devel gcc-c++
BuildRequires: java-devel-default
BuildRequires: libXxf86misc-devel
BuildRequires: opencascade-devel libgts-devel
BuildRequires: libode-devel libann-devel
BuildRequires: doxygen graphviz
BuildRequires: eigen3
BuildRequires: libnumpy-py3-devel
BuildRequires: boost-interprocess-devel
BuildRequires: gdb
BuildRequires: libvtk-devel vtk-examples vtk-python3
BuildRequires: libhdf5-devel
BuildRequires: libmed-devel libspnav-devel
#BuildRequires: python3-module-matplotlib-qt6
BuildRequires: libkdtree++-devel
%if_without bundled_libs
BuildRequires: libsmesh-devel libnetgen-devel netgen openmpi-devel
%endif
%if_with glvnd
BuildRequires: libglvnd-devel
%else
Requires: libEGL-devel libGLU-devel
%endif
#BuildRequires: texlive-extra-utils
BuildRequires: libnetgen-devel netgen
%if_with pybind11
BuildRequires: pybind11-devel
%endif
%if_without bundled_pycxx
BuildRequires: python3-module-pycxx-devel
%endif

#%%py3_requires matplotlib.backends.backend_qt6
%py3_requires pivy
#py3_provides Fem FreeCAD FreeCADGui Mesh Part MeshPart Drawing ImportGui
#py3_provides PartGui Sketcher TestSketcherApp Robot RobotGui SketcherGui
#py3_provides ImageGui PartDesignGui _PartDesign
%add_python3_req_skip pyopencl IfcImport Units
%add_findreq_skiplist %ldir/Mod/*

%ifnarch armh
# TODO: cgal needed for openscad was not built for armh
Requires: openscad
%endif
Requires: python3-module-GitPython
Requires: netgen
Requires: libredwg

Provides:  free-cad-docs = %version-%release
Obsoletes: free-cad-docs < %version-%release
Provides:  freecad-docs = %version-%release
Obsoletes: freecad-docs < %version-%release

%description
FreeCAD will be a general purpose 3D CAD modeler. FreeCAD is aimed directly at
mechanical engineering and product design but also fits in a wider range of uses
around engineering, such as architecture or other engineering specialties.

FreeCAD features tools similar to Catia, SolidWorks or Solid Edge, and therefore
also falls into the category of MCAD, PLM, CAx and CAE. It will be a feature
based parametric modeler with a modular software architecture which makes it
easy to provide additional functionality without modifying the core system.

%prep
%setup
%if_without bundled_libs
# Removed bundled libraries
%patch1 -p1
rm -rf src/3rdParty
%endif
%patch2 -p1
%patch3 -p1
%if_without bundled_pycxx
%patch4 -p1
rm -rf src/CXX
%endif
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

%ifarch %e2k
sed -i "/-fext-numeric-literals/d" src/Mod/Path/App/CMakeLists.txt
# because "error: cpio archive too big"
%define optflags_debug -g0
# too much warnings of this type
%add_optflags -Wno-overloaded-virtual
sed -i "s/FC_OS_WIN32/__EDG__/" src/Mod/Sketcher/App/GeoEnum.{h,cpp}
sed -i "/extern template/{N;s/.*/#ifndef OBSERVER_CPP\n&\n#endif/}" src/Base/Observer.h
sed -i "1i #define OBSERVER_CPP" src/Base/Observer.cpp
%endif

%build
export PATH=$PATH:%_qt6_bindir
%add_optflags -Wl,-rpath,%ldir/lib
%if_with ninja
%cmake_insource -GNinja \
%else
%cmake_insource \
%endif
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_INSTALL_DATADIR=%ldir \
	-DCMAKE_INSTALL_DOCDIR=%ldir/doc \
	-DCMAKE_INSTALL_LIBDIR=%ldir/lib \
	-DOPENMPI_INCLUDE_DIRS=%_libdir/openmpi/include \
	-DPYTHON_EXECUTABLE=%__python3 \
%if_with pybind11
    -DFREECAD_USE_PYBIND11=ON \
%endif
	-DFREECAD_LIBPACK_USEPYSIDE=OFF \
	-DBUILD_QT6=ON \
	-DFREECAD_QT_VERSION=6 \
%ifnarch %qt6_qtwebengine_arches
	-DBUILD_WEB=OFF \
%endif
%if_without bundled_libs
	-DFREECAD_USE_EXTERNAL_SMESH=ON \
	-DSMESH_DIR=%_libdir/cmake \
	-DSMESH_INCLUDE_DIR=%_includedir/smesh \
	-DBUILD_FEM_NETGEN=ON \
%endif
%if_with glvnd
	-DOpenGL_GL_PREFERENCE=GLVND \
%endif
	-DFREECAD_USE_EXTERNAL_PIVY=ON \
	-DPACKAGE_WCREF="%git_rev" \
	-DPACKAGE_WCDATE="%git_date" \
	-DPACKAGE_WCURL="https://github.com/FreeCAD/FreeCAD" \
    -DUSE_OPENCV=ON \
%if_without bundled_pycxx
    -DPYCXX_INCLUDE_DIR=$(pkg-config --variable=includedir PyCXX) \
    -DPYCXX_SOURCE_DIR=$(pkg-config --variable=srcdir PyCXX) \
%endif
	-Wno-dev
export NPROCS=%build_parallel_jobs
%if_with ninja
%ninja_build
%else
%make_build
%endif

%install
%if_with ninja
%ninja_install
%else
%makeinstall_std
%endif

# binaries
mkdir -p %buildroot%ldir/bin
mv %buildroot%_bindir/* %buildroot%ldir/bin
ln -s ../%_lib/%name/bin/FreeCAD %buildroot%_bindir/freecad
ln -s ../%_lib/%name/bin/FreeCADCmd %buildroot%_bindir/freecadcmd
ln -s ../%_lib/%name/bin/FreeCAD %buildroot%_bindir/FreeCAD
ln -s ../%_lib/%name/bin/FreeCADCmd %buildroot%_bindir/FreeCADCmd

# manpage
install -Dm0644 %SOURCE1 %buildroot%_man1dir/%name.1

# stuff
cp -af %buildroot%_prefix/Mod/* %buildroot%ldir/Mod
rm -rf %buildroot%_prefix/Mod
cp -af %buildroot%_prefix/Ext/ %buildroot%ldir/Ext
rm -rf %buildroot%_prefix/Ext

# l10n
%find_lang --with-kde %name

# fix python shebang
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' %buildroot%_libdir/freecad/Mod)

# remove static libraries
rm -f %buildroot%_libdir/freecad/lib/*.a

# remove header file
rm -f %buildroot%_includedir/E57Format/*.h
rm -rf %buildroot%_includedir/{gmock,gtest}

# remove buggy Tux mod
rm -rf %buildroot%ldir/Mod/Tux

%files -f %name.lang
%doc README.md SECURITY.md
%doc %ldir/doc
%dir %ldir
%_bindir/*
%ldir/bin
%ldir/lib
%ldir/Gui
%ldir/Ext
%ldir/Mod
%ldir/3Dconnexion
%ldir/examples
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/*/*.svg
%_man1dir/*
%_xdgdatadir/mime/packages/*
%_pixmapsdir/%name.xpm
%_datadir/metainfo/*.appdata.xml
%_datadir/thumbnailers/FreeCAD.thumbnailer

%changelog
* Fri Aug 30 2024 Sergey V Turchin <zerg@altlinux.org> 1:0.21.2-alt7.2
- NMU: fix building new Qt/PySide

* Mon May 13 2024 Ivan A. Melnikov <iv@altlinux.org> 1:0.21.2-alt7.1
- NMU: fix building with boost 1.85.0.

* Tue Apr 09 2024 Michael Shigorin <mike@altlinux.org> 1:0.21.2-alt7
- Avoid PySide6.QtWebEngine* deps on arches lacking those.

* Thu Apr 04 2024 Andrey Cherepanov <cas@altlinux.org> 1:0.21.2-alt6
- Built with Qt6 and PySide6.
- Did not build for i586.

* Thu Feb 29 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:0.21.2-alt5
- Fixed build for Elbrus.

* Wed Feb 07 2024 Grigory Ustinov <grenka@altlinux.org> 1:0.21.2-alt4
- Fixed build with vtk9.3.

* Fri Jan 05 2024 Grigory Ustinov <grenka@altlinux.org> 1:0.21.2-alt3
- Build without bundled pycxx.

* Thu Jan 04 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:0.21.2-alt2
- NMU: build without web addon on LoongArch (requires qt5-webengine,
  not available here).

* Wed Jan 03 2024 Andrey Cherepanov <cas@altlinux.org> 1:0.21.2-alt1
- New version.
- Made build with PySide2 optional.

* Wed Nov 01 2023 Andrey Cherepanov <cas@altlinux.org> 1:0.21.1-alt4
- Removed python3-module-shiboken2-devel.

* Thu Oct 19 2023 Andrey Cherepanov <cas@altlinux.org> 1:0.21.1-alt3
- Complete remove PySide2 from requirements.

* Wed Oct 18 2023 Andrey Cherepanov <cas@altlinux.org> 1:0.21.1-alt2
- Remove PySide2 from requires.

* Sat Oct 14 2023 Andrey Cherepanov <cas@altlinux.org> 1:0.21.1-alt1
- New version.
- FTBFS: removed qt5-sql-sqlite3.
- Added support of netgen, pybind11 and opencv.
- Merge freecad-docs with freecad.

* Sun Sep 24 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:0.20.2-alt3.2
- Fixed build for Elbrus.

* Sun Jul 16 2023 Ivan A. Melnikov <iv@altlinux.org> 1:0.20.2-alt3.1
- NMU: drop obsolete BR on libf2c-ng-devel.

* Tue Jul 04 2023 Andrey Cherepanov <cas@altlinux.org> 1:0.20.2-alt3
- FTBFS: fixed build with GCC 13.x.

* Tue Jan 03 2023 Andrey Cherepanov <cas@altlinux.org> 1:0.20.2-alt2
- Rebuilt with opencascade-7.7.0.

* Mon Dec 05 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.20.2-alt1
- New version.

* Sun Aug 28 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.20.1-alt2
- Fixed application version (ALT #43585).

* Thu Aug 11 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.20.1-alt1
- New version.
- Added support of LibreDWG.

* Thu Jun 16 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.20-alt1
- New version.
- Do not build for armh.

* Mon Apr 25 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.19.4-alt2
- Rebuild with opencascade 7.6.

* Thu Mar 03 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.19.4-alt1
- New version.

* Mon Dec 06 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.19.3-alt1
- New version.

* Sun Oct 17 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:0.19.2-alt5
- Fixed build for Elbrus.

* Wed Aug 18 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.19.2-alt4
- Rebuilt with boost-1.77.0.

* Mon Jul 05 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.19.2-alt3
- Fix icon name in desktop file (ALT #40371).

* Wed May 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.19.2-alt2
- Rebuilt with VTK-9.0.1.

* Wed May 05 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.19.2-alt1
- New version.
- Build with opencascade instead of obsoleted OCE.
- Enable bundled libs to add lazy_loader python module (thanks rider@).
- Several fixes by rider@.

* Wed Mar 24 2021 Andrey Cherepanov <cas@altlinux.org> 1:0.19.1-alt1
- New version.

* Tue Mar 16 2021 Sergey V Turchin <zerg@altlinux.org> 1:0.18.5-alt3
- Add compatibility with p9.

* Thu Jan 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.18.5-alt2
- Rebuilt with boost-1.75.0 and enabled c++14 by default.

* Fri Nov 27 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.5-alt0.1.p9
- Backport new version to p9 branch.

* Fri Nov 27 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.5-alt1
- New version.
- Add requirements of openscad and GitPython.
- Fix Addon Manager during macro info retrieving.

* Tue Oct 06 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt4.2.p9
- Build with new version of coin3d.
- Build without glvnd.

* Tue Sep 15 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt4.1.p9
- Backport fixes to p9 branch.

* Fri Sep 11 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt5
- Require python-module-matplotlib-qt4 for workbench (ALT #38925).

* Wed Sep 09 2020 Sergey V Turchin <zerg@altlinux.org> 1:0.18.4-alt1.2.p9
- Backport to p9 branch.

* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.18.4-alt4
- Fixed build with qt-5.15.

* Wed Jun 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.18.4-alt3
- Rebuilt with boost-1.73.0.

* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt2
- Fix Unknown release and repository URL.
- Build with Qt5.
- Fix License tag according to upstream information and SPDX.
- Build using ninja-build.

* Tue Apr 14 2020 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt0.1.p9
- Backport new version to p9 branch.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.4-alt1
- New version.

* Thu Jul 18 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.3-alt1
- New version.

* Fri May 24 2019 Slava Aseev <ptrnine@altlinux.org> 1:0.18.2-alt3
- Rebuild with vtk8.2

* Tue May 21 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.2-alt2
- Use desktop file and mime data from upstream (ALT #36762).
- Add Russian localization of desktop file as patch.

* Sun May 12 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.2-alt1
- New version.

* Fri Apr 05 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18.1-alt1
- New version (ALT #36524).

* Fri Mar 22 2019 Andrey Cherepanov <cas@altlinux.org> 1:0.18-alt1
- New version (ALT #36332).

* Thu Nov 22 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17.13543-alt1
- Version 0.17 with changes from releases/FreeCAD-0-17.

* Tue Nov 06 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt7
- Build with libglvnd-devel.

* Wed Sep 26 2018 Anton Midyukov <antohami@altlinux.org> 1:0.17-alt6
- Fix segfault (Closes: 35002)

* Fri Sep 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.17-alt5
- NMU: rebuilt with vtk-8.1.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.17-alt4.1
- NMU: rebuilt with boost-1.67.0

* Tue May 22 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt4
- Fix path in desktop file.

* Mon May 21 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt3
- Fix run from menu (add FreeCAD executable to %_bindir).

* Fri May 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt2
- Build with OCE instead of opencascade

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.17-alt1
- New version (ALT #34781).

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
