# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%define abiversion 161
%define ot_abiversion 21
%define ot_version 3.3.1

# TODO: with additional buildreqs it builds
#    /usr/bin/osgQtBrowser
#    /usr/bin/osgQtWidgets
#    /usr/bin/osgqfont
#    /usr/bin/osgviewerFLTK
#    /usr/bin/osgviewerQt
#    /usr/bin/osgviewerWX


#
# Copyright (c) 2005, 2006, 2007, 2008, 2009 Ralf Corsepius, Ulm, Germany.
# Copyright (c) 2009 Michael Shigorin
# Copyright (c) 2011 Dmitry Derjavin
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

Name: OpenSceneGraph
Version: 3.6.5
Release: alt6

Summary: High performance real-time graphics toolkit
License: LGPL-2.1-only WITH WxWindows-exception-3.1
Group: System/Libraries
Url: http://www.openscenegraph.org
Vcs: https://github.com/openscenegraph/OpenSceneGraph

Source: %name-%version.tar

# thanks, Fedora
Patch1: 0001-Cmake-fixes.patch
# Upstream deactivated building osgviewerWX for obscure reasons
# Reactivate for now.
Patch2: 0002-Activate-osgviewerWX.patch
# Unset DOT_FONTNAME
Patch3: 0003-Unset-DOT_FONTNAME.patch
# Re-add osgframerenderer
Patch4: 0004-Re-add-osgframerenderer.patch
# Force osgviewerWX to always use X11 backend (wxGLCanvas is broken on Wayland)
Patch5: force-x11-backend.patch
# Minimal port to OpenEXR 3
# https://github.com/openscenegraph/OpenSceneGraph/issues/1075
Patch6: OpenSceneGraph-openexr3.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: boost-asio-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: gcc-c++
BuildRequires: libgif-devel
BuildRequires: gnuplot

BuildRequires: libcurl-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libvncserver-devel
BuildRequires: libxml2-devel
BuildRequires: libXmu-devel
BuildRequires: libX11-devel

BuildRequires: libInventor-devel
#BuildRequires: libSDL-devel
BuildRequires: libSDL2-devel
#BuildRequires: libXScrnSaver-devel
#BuildRequires: libXcomposite-devel
#BuildRequires: libXdmcp-devel
#BuildRequires: libXpm-devel
#BuildRequires: libXtst-devel
#BuildRequires: libXxf86misc-devel
#BuildRequires: libfreeglut-devel

BuildRequires: libcairo-devel
BuildRequires: libXrandr-devel

BuildRequires: libgtkglext-devel
BuildRequires: libopenal-devel
BuildRequires: libpoppler-glib-devel
BuildRequires: librsvg-devel
BuildRequires: libxkbfile-devel
BuildRequires: libxml2-devel
BuildRequires: libgta-devel

BuildRequires: libwxGTK3.2-devel
#BuildRequires: pkgconfig(gtk+-2.0)

BuildRequires: gstreamer1.0-devel
BuildRequires: libgstreamermm1.0-devel
BuildRequires: gst-plugins-bad1.0-devel
BuildRequires: gst-plugins1.0-devel

BuildRequires: libgdal-devel

%ifarch %e2k
# error: cpio archive too big - 4321M
%define optflags_debug -g0
%endif

%description
The OpenSceneGraph is an OpenSource, cross platform graphics
toolkit for the development of high performance graphics
applications such as flight simulators, games, virtual reality
and scientific visualization. Based around the concept of
a SceneGraph, it provides an object oriented framework on top
of OpenGL freeing the developer from implementing and optimizing
low level graphics calls, and provides many additional utilities
for rapid development of graphics applications.

%package -n libOpenSceneGraph%abiversion
Summary: Development files for OpenSceneGraph
Group: System/Libraries
Obsoletes: libOpenSceneGraph <= 3.6.5-alt4

%description -n libOpenSceneGraph%abiversion
Runtime libraries files for OpenSceneGraph

%package -n libOpenSceneGraph-devel
Summary: Development files for OpenSceneGraph
Group: Development/C++

%description -n libOpenSceneGraph-devel
Development files for OpenSceneGraph

%package gdal
Summary: OSG Gdal plugin
Group: System/Libraries

%description gdal
OSG Gdal plugin.

%package gstreamer
Summary: OSG gstreamer plugin
Group: System/Libraries

%description gstreamer
OSG gstreamer plugin.

%package inventor
Summary: OSG inventor plugin
Group: System/Libraries

%description inventor
OSG inventor plugin.

%package examples-SDL
Summary: OSG sample applications using SDL
Group: Development/Documentation

%description examples-SDL
OSG sample applications using SDL

# currently broken, see #25943
#package examples-fltk
#Summary: OSG sample applications using FLTK
#Group: Development/Documentation
#
#description examples-fltk
#OSG sample applications using FLTK
#
#files examples-fltk
#_bindir/osgviewerFLTK

# lcc 1.23.12:
# CMakeFiles/example_osgoscdevice.dir/osgoscdevice.o:(.rodata._ZTIPKN5osgFX6ScribeE[_ZTIPKN5osgFX6ScribeE]+0x18): undefined reference to `typeinfo for osgFX::Scribe'
# CMakeFiles/example_osgoscdevice.dir/osgoscdevice.o:(.rodata._ZTIPKN5osgFX6EffectE[_ZTIPKN5osgFX6EffectE]+0x18): undefined reference to `typeinfo for osgFX::Effect'
# OpenSceneGraph-examples
%package examples
Summary: Sample applications for OpenSceneGraph
Group: Development/Documentation

%description examples
Sample applications for OpenSceneGraph

%package -n libOpenThreads%ot_abiversion
Summary: OpenThreads
Group: System/Libraries
Provides: OpenThreads%ot_abiversion = OpenSceneGraph-%version
Obsoletes: libOpenThreads <= 3.6.5-alt4

%description -n libOpenThreads%ot_abiversion
OpenThreads is intended to provide a minimal & complete Object-Oriented
(OO) thread interface for C++ programmers. It is loosely modeled on the
Java thread API, and the POSIX Threads standards. The architecture of
the library is designed around "swappable" thread models which are
defined at compile-time in a shared object library.

%package -n libOpenThreads-devel
Summary: Development files for OpenThreads
Group: Development/C++

%description -n libOpenThreads-devel
Development files for OpenThreads

%package core-plugins
Summary: OSG core plugins
Group: System/Libraries

%description core-plugins
OSG core plugins.

%package -n libosgAnimation%abiversion
Summary: OSG library libosgAnimation
Group: System/Libraries

%description -n libosgAnimation%abiversion
This package contains library libosgAnimation of OSG.

%package -n libosgDB%abiversion
Summary: OSG library libosgDB
Group: System/Libraries

%description -n libosgDB%abiversion
This package contains library libosgDB of OSG.

%package -n libosgFX%abiversion
Summary: OSG library libosgFX
Group: System/Libraries

%description -n libosgFX%abiversion
This package contains library libosgFX of OSG.

%package -n libosgGA%abiversion
Summary: OSG library libosgGA
Group: System/Libraries

%description -n libosgGA%abiversion
This package contains library libosgGA of OSG.

%package -n libosgManipulator%abiversion
Summary: OSG library libosgManipulator
Group: System/Libraries

%description -n libosgManipulator%abiversion
This package contains library libosgManipulator of OSG.

%package -n libosgParticle%abiversion
Summary: OSG library libosgParticle
Group: System/Libraries

%description -n libosgParticle%abiversion
This package contains library libosgParticle of OSG.

%package -n libosgPresentation%abiversion
Summary: OSG library libosgPresentation
Group: System/Libraries

%description -n libosgPresentation%abiversion
This package contains library libosgPresentation of OSG.

%package -n libosgShadow%abiversion
Summary: OSG library libosgShadow
Group: System/Libraries

%description -n libosgShadow%abiversion
This package contains library libosgShadow of OSG.

%package -n libosgSim%abiversion
Summary: OSG library libosgSim
Group: System/Libraries

%description -n libosgSim%abiversion
This package contains library libosgSim of OSG.

%package -n libosgTerrain%abiversion
Summary: OSG library libosgTerrain
Group: System/Libraries

%description -n libosgTerrain%abiversion
This package contains library libosgTerrain of OSG.

%package -n libosgText%abiversion
Summary: OSG library libosgText
Group: System/Libraries

%description -n libosgText%abiversion
This package contains library libosgText of OSG.

%package -n libosgUI%abiversion
Summary: OSG library libosgUI
Group: System/Libraries

%description -n libosgUI%abiversion
This package contains library libosgUI of OSG.

%package -n libosgUtil%abiversion
Summary: OSG library libosgUtil
Group: System/Libraries

%description -n libosgUtil%abiversion
This package contains library libosgUtil of OSG.

%package -n libosgViewer%abiversion
Summary: OSG library libosgViewer
Group: System/Libraries

%description -n libosgViewer%abiversion
This package contains library libosgViewer of OSG.

%package -n libosgVolume%abiversion
Summary: OSG library libosgVolume
Group: System/Libraries
%description -n libosgVolume%abiversion
This package contains library libosgVolume of OSG.

%package -n libosgWidget%abiversion
Summary: OSG library libosgWidget
Group: System/Libraries

%description -n libosgWidget%abiversion
This package contains library libosgWidget of OSG.

%prep
%setup
%autopatch -p1
# FTBFS: fix: asio has not been declared (build with boost-asio-devel)
subst 's|#include <asio.hpp>|#include <boost/asio.hpp>|' src/osgPlugins/RestHttpDevice/connection.hpp
subst 's|#include <asio.hpp>|#include <boost/asio.hpp>|' src/osgPlugins/RestHttpDevice/server.hpp
subst 's|#include <asio.hpp>|#include <boost/asio.hpp>|' src/osgPlugins/RestHttpDevice/reply.hpp
subst 's|#include <asio.hpp>|#include <boost/asio.hpp>|' src/osgPlugins/RestHttpDevice/io_service_pool.hpp

# path to install examples (instead the patch)
sed -i "s|share/OpenSceneGraph/bin|bin|" CMakeModules/OsgMacroUtils.cmake

# Also look in /usr/share/fonts for fonts
sed -i -e 's,\.:/usr/share/fonts/ttf:,.:%{_datadir}/fonts:/usr/share/fonts/ttf:,' \
src/osgText/Font.cpp

iconv -f ISO-8859-1 -t utf-8 AUTHORS.txt > AUTHORS.txt~
mv AUTHORS.txt~ AUTHORS.txt

# Update doxygen
doxygen -u doc/Doxyfiles/doxyfile.cmake
doxygen -u doc/Doxyfiles/openthreads.doxyfile.cmake

%build
%cmake -DCMAKE_BUILD_TYPE="Release" \
      -DLIB_POSTFIX=%(l=%{_lib}; echo ${l:3}) \
      -DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
%ifarch %e2k
      -DBUILD_OSG_EXAMPLES=OFF \
%else
      -DBUILD_OSG_EXAMPLES=ON \
%endif
      -DBUILD_OSG_WRAPPERS=ON \
      -DBUILD_DOCUMENTATION=ON \
      -DOSG_AGGRESSIVE_WARNING_FLAGS=OFF \
      -Wno-dev

%cmake_build

%install
%cmake_install

# hack for 3.4.x (it is ok since 3.6.0)
rm -rf %buildroot/usr/doc/

%files
%doc AUTHORS.txt LICENSE.txt NEWS.txt README.md
%_bindir/osgarchive
%_bindir/osgconv
%_bindir/osgviewer
%_bindir/osgfilecache
%_bindir/present3D

%files -n libOpenSceneGraph%abiversion
%_libdir/libosg.so.%version
%_libdir/libosg.so.%abiversion

%files -n libosgAnimation%abiversion
%_libdir/libosgAnimation.so.%abiversion
%_libdir/libosgAnimation.so.%version

%files -n libosgDB%abiversion
%_libdir/libosgDB.so.%abiversion
%_libdir/libosgDB.so.%version

%files -n libosgFX%abiversion
%_libdir/libosgFX.so.%abiversion
%_libdir/libosgFX.so.%version

%files -n libosgGA%abiversion
%_libdir/libosgGA.so.%abiversion
%_libdir/libosgGA.so.%version

%files -n libosgManipulator%abiversion
%_libdir/libosgManipulator.so.%abiversion
%_libdir/libosgManipulator.so.%version

%files -n libosgParticle%abiversion
%_libdir/libosgParticle.so.%abiversion
%_libdir/libosgParticle.so.%version

%files -n libosgPresentation%abiversion
%_libdir/libosgPresentation.so.%abiversion
%_libdir/libosgPresentation.so.%version

%files -n libosgShadow%abiversion
%_libdir/libosgShadow.so.%abiversion
%_libdir/libosgShadow.so.%version

%files -n libosgSim%abiversion
%_libdir/libosgSim.so.%abiversion
%_libdir/libosgSim.so.%version

%files -n libosgTerrain%abiversion
%_libdir/libosgTerrain.so.%abiversion
%_libdir/libosgTerrain.so.%version

%files -n libosgText%abiversion
%_libdir/libosgText.so.%abiversion
%_libdir/libosgText.so.%version

%files -n libosgUI%abiversion
%_libdir/libosgUI.so.%abiversion
%_libdir/libosgUI.so.%version

%files -n libosgUtil%abiversion
%_libdir/libosgUtil.so.%abiversion
%_libdir/libosgUtil.so.%version

%files -n libosgViewer%abiversion
%_libdir/libosgViewer.so.%abiversion
%_libdir/libosgViewer.so.%version

%files -n libosgVolume%abiversion
%_libdir/libosgVolume.so.%abiversion
%_libdir/libosgVolume.so.%version

%files -n libosgWidget%abiversion
%_libdir/libosgWidget.so.%abiversion
%_libdir/libosgWidget.so.%version

%files core-plugins
%_libdir/osgPlugins-%version
%exclude %_libdir/osgPlugins-%version/osgdb_gstreamer.so
%exclude %_libdir/osgPlugins-%version/osgdb_gdal.so
%exclude %_libdir/osgPlugins-%version/osgdb_ogr.so
%exclude %_libdir/osgPlugins-%version/osgdb_gstreamer.so
%exclude %_libdir/osgPlugins-%version/osgdb_iv.so

%files gdal
%_libdir/osgPlugins-%version/osgdb_gdal.so
%_libdir/osgPlugins-%version/osgdb_ogr.so

%files gstreamer
%_libdir/osgPlugins-%version/osgdb_gstreamer.so

%files inventor
%_libdir/osgPlugins-%version/osgdb_iv.so

%files -n libOpenSceneGraph-devel
%_includedir/osg*
%_pkgconfigdir/openscenegraph*.pc
%_libdir/libosg*.so
%_bindir/osgversion

%ifnarch %e2k
#files examples-SDL
#_bindir/osgviewerSDL

%files examples
%_bindir/osg*
%exclude %_bindir/osgversion
%exclude %_bindir/osgarchive
%exclude %_bindir/osgconv
%exclude %_bindir/osgviewer
%exclude %_bindir/osgfilecache
%exclude %_bindir/present3D
%endif

%files -n libOpenThreads%ot_abiversion
%doc AUTHORS.txt LICENSE.txt NEWS.txt README.md
%_libdir/libOpenThreads.so.%ot_version
%_libdir/libOpenThreads.so.%ot_abiversion

%files -n libOpenThreads-devel
%_pkgconfigdir/openthreads.pc
%_libdir/libOpenThreads.so
%_includedir/OpenThreads

%changelog
* Thu Jun 04 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.6.5-alt6
- e2k build fix

* Wed Feb 11 2026 Pavel Petrykin <silverducks@altlinux.org> 3.6.5-alt5
- Ensure compliance with Shared Libs Policy.

* Mon Nov 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.6.5-alt4
- FTBFS: fix:
  + build with boost-asio-devel
  + drop OpenSceneGraph_asio.patch
  + changed license tag

* Mon Oct 16 2023 Anton Midyukov <antohami@altlinux.org> 3.6.5-alt3
- rebuild with wxGTK3.2

* Thu Jan 20 2022 Michael Shigorin <mike@altlinux.org> 3.6.5-alt2
- move present3D from examples (it isn't) to the main package

* Tue Jan 11 2022 Anton Midyukov <antohami@altlinux.org> 3.6.5-alt1
- new version (3.6.5) with rpmgs script
- unpackaged files in buildroot should terminate build
- update build requires
- cleanup spec
- new subpackages with plugins: gdal, gstreamer, inventor

* Sun Nov 28 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.4.1-alt2.2
- fixed passing optlevel to cmake

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 3.4.1-alt2.1
- NMU: spec: adapted to new cmake macros.

* Sun Aug 04 2019 Michael Shigorin <mike@altlinux.org> 3.4.1-alt2
- E2K:
  + disable examples build (some of them fail to link)
  + disable debuginfo (too large files for cpio)
- moved osgviewerGTK to examples where it belongs
- added present3D to examples (previously unpackaged)

* Thu Jun 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.4.1-alt1
- cleanup spec
- disable build with wxWidgets (any reasons?) and Qt

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- 3.4.0
- updated example filelist

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 3.2.3-alt1
- 3.2.3

* Tue Sep 29 2015 Michael Shigorin <mike@altlinux.org> 3.2.1-alt3
- rebuilt for gcc5 C++11 ABI (see also rh#1212707)

* Fri Oct 24 2014 Michael Shigorin <mike@altlinux.org> 3.2.1-alt2
- applied upstream patch (svn rev14400) to fix use-after-free
  + see also http://bugs.debian.org/765855

* Tue Jul 29 2014 Michael Shigorin <mike@altlinux.org> 3.2.1-alt1
- 3.2.1

* Thu Sep 26 2013 Michael Shigorin <mike@altlinux.org> 3.2.0-alt1
- 3.2.0
- fixed inter-subpackage deps
- built with libtiff

* Thu Sep 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt2.1
- Rebuilt with libpng15

* Wed Nov 30 2011 Michael Shigorin <mike@altlinux.org> 3.0.1-alt2
- moved osgversion from %name to lib%name-devel
  (thanks dd@ for hitting the problem and iv@ for diagnosing it)
- buildreq (added libxml2-devel, libopenal-devel, gnuplot)

* Sat Sep 24 2011 Michael Shigorin <mike@altlinux.org> 3.0.1-alt1
- 3.0.1
- minor spec cleanup
- include all pkgconfig files
- more strict (version-release) library subpackage deps

* Fri Jul 22 2011 Dmitry Derjavin <dd@altlinux.org> 3.0.0-alt1
- 3.0
- *-examples-fltk removed temporarily(?)
- osgviewer-QT renamed to osgviewer-Qt
- osgbrowser removed, changelog: 2008-11-20 11:28
- osgintrospection removed, changelog: 2010-06-23 13:28
- new 25 examples added

* Wed Jul 06 2011 Michael Shigorin <mike@altlinux.org> 2.8.3-alt3
- fix FTBFS (2.8.5/3.0.0 need a bit more time)

* Fri Apr 15 2011 Michael Shigorin <mike@altlinux.org> 2.8.3-alt2
- rebuild

* Wed Mar 09 2011 Michael Shigorin <mike@altlinux.org> 2.8.3-alt1
- 2.8.3
- updated fedora patch
- updated linking (now makefile) patch
- description fixup
- added (a tiny part of) gentoo patch
- added osganimationhardware to examples

* Mon Sep 27 2010 Michael Shigorin <mike@altlinux.org> 2.8.0-alt2.1
- rebuilt against current X libraries (thanks dd@)

* Tue Mar 24 2009 Michael Shigorin <mike@altlinux.org> 2.8.0-alt2
- spec cleanup

* Sun Mar 22 2009 Michael Shigorin <mike@altlinux.org> 2.8.0-alt1
- built for ALT Linux
  + based on Fedora (and to some extent Mandriva Cooker) specs/patches
  + heavy spec cleanup
  + libification
  + slight %%files shuffle

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Ralf Corsépius <rc040203@freenet.de> - 2.8.0-1
- Upgrade to OSG-2.8.0.
- Remove Obsolete: Producer hacks.

* Wed Aug 14 2008 Ralf Corsépius <rc040203@freenet.de> - 2.6.0-1
- Upgrade to OSG-2.6.0.

* Wed Aug 13 2008 Ralf Corsépius <rc040203@freenet.de> - 2.4.0-4
- Preps for 2.6.0.
- Reflect the Source0-URL having changed.
- Major spec-file overhaul.

* Thu May 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.0-3
- fix license tag

* Tue May 13 2008 Ralf Corsépius <rc040203@freenet.de> - 2.4.0-2
- Add Orion Poplawski's patch to fix building with cmake-2.6.0.

* Mon May 12 2008 Ralf Corsépius <rc040203@freenet.de> - 2.4.0-1
- Upstream update.
- Adjust patches to 2.4.0.

* Mon Feb 11 2008 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-5
- Add *-examples-SDL package.
- Add osgviewerSDL.
- Add *-examples-fltk package.
- Add osgviewerFLTK.
- Add *-examples-qt package.
- Move osgviewerQT to *-examples-qt package.

* Mon Feb 11 2008 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-4
- Rebuild for gcc43.
- OpenSceneGraph-2.2.0.diff: Add gcc43 hacks.

* Wed Nov 28 2007 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-3
- Re-add apivers.
- Rebuild against doxygen-1.5.3-1 (BZ 343591).

* Thu Nov 02 2007 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-2
- Add qt.

* Thu Nov 01 2007 Ralf Corsépius <rc040203@freenet.de> - 2.2.0-1
- Upstream upgrade.
- Reflect Source0-URL having changed once again.
- Reflect upstream packaging changes to spec.

* Sat Oct 20 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-8
- Reflect Source0-URL having changed.

* Thu Sep 27 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-7
- Let OpenSceneGraph-libs Obsoletes: Producer
- Let OpenSceneGraph-devel Obsoletes: Producer-devel.

* Wed Sep 26 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-6
- By public demand, add upstream's *.pcs.
- Add hacks to work around the worst bugs in *.pcs.
- Add OpenSceneGraph2-devel.
- Move ldconfig to *-libs.
- Abandon OpenThreads2.
- Remove obsolete applications.

* Wed Aug 22 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-5
- Prepare renaming package into OpenSceneGraph2.
- Split out run-time libs into *-libs subpackage.
- Rename pkgconfig files into *-2.pc.
- Reactivate ppc64.
- Mass rebuild.

* Sat Jun 30 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-4
- Cleanup CVS.
- Add OSG1_Producer define.

* Fri Jun 29 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-3
- Re-add (but don't ship) *.pc.
- Let OpenSceneGraph "Obsolete: Producer".
- Let OpenSceneGraph-devel "Obsolete: Producer-devel".

* Wed Jun 27 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-2
- Build docs.

* Fri Jun 22 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0-1
- Upgrade to 2.0.

* Thu Jun 21 2007 Ralf Corsépius <rc040203@freenet.de> - 1.2-4
- ExcludeArch: ppc64 (BZ 245192, 245196).

* Thu Jun 21 2007 Ralf Corsépius <rc040203@freenet.de> - 1.2-3
- Remove demeter (Defective, abandoned by upstream).

* Wed Mar 21 2007 Ralf Corsépius <rc040203@freenet.de> - 1.2-2
- Attempt to build with gdal enabled.

* Wed Oct 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2-1
- Upstream update.
- Remove BR: flex bison.
- Drop osgfbo and osgpbuffer.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.1-2
- Mass rebuild.

* Thu Aug 24 2006 Ralf Corsépius <rc040203@freenet.de> - 1.1-1
- Upstream update.

* Sat Jul 08 2006 Ralf Corsépius <rc040203@freenet.de> - 1.0-5
- Rebuilt to with gcc-4.1.1-6.

* Tue Jun 07 2006 Ralf Corsépius <rc040203@freenet.de> - 1.0-4
- Try to avoid adding SONAMEs on plugins and applications.

* Tue Jun 06 2006 Ralf Corsépius <rc040203@freenet.de> - 1.0-3
- Add SONAME hack to spec (PR 193934).
- Regenerate OpenSceneGraph-1.0.diff.
- Remove OpenSceneGraph-1.0.diff from look-aside cache. Add to CVS instead.
- Fix broken shell fragments.

* Sun Feb 19 2006 Ralf Corsépius <rc040203@freenet.de> - 1.0-2
- Rebuild.

* Sat Dec 10 2005 Ralf Corsépius <rc040203@freenet.de> - 1.0-1
- Upstream update.

* Wed Dec 07 2005 Ralf Corsépius <rc040203@freenet.de> - 0.9.9-5
- Try at getting this package buildable with modular X11.

* Tue Dec 06 2005 Ralf Corsepius <rc040203@freenet.de> - 0.9.9-4%{?dist}.1
- Merge diffs into one file.
- Fix up *.pcs from inside of *.spec.

* Sun Aug 28 2005 Ralf Corsepius <rc040203@freenet.de> - 0.9.9-4
- Propagate %%_libdir to pkgconfig files.
- Fix typo in %%ifarch magic to setup LD_LIBRARY_PATH
- Move configuration to %%build.
- Spec file cosmetics.

* Sat Aug 27 2005 Ralf Corsepius <rc040203@freenet.de> - 0.9.9-3
- Add full URL to Debian patch.
- Add _with_demeter.
- Extend Producer %%description.
- Extend OpenThreads %%description.

* Tue Aug 09 2005 Ralf Corsepius <ralf@links2linux.de> - 0.9.9-2
- Fix license to OSGPL.
- Change permissions on pkgconfig files to 0644.

* Tue Aug 02 2005 Ralf Corsepius <ralf@links2linux.de> - 0.9.9-1
- FE submission.

* Thu Jul 21 2005 Ralf Corsepius <ralf@links2linux.de> - 0.9.9-0
- Initial spec.
