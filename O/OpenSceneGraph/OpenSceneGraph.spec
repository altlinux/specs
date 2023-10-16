# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

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
Release: alt3

Summary: High performance real-time graphics toolkit
License: OSGPL (wxWidgets, clarified LGPL)
Group: System/Libraries

Url: http://www.openscenegraph.org
# Source-url: https://github.com/openscenegraph/OpenSceneGraph/archive/OpenSceneGraph-%version.tar.gz
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

# thanks, Fedora
Patch1: 0001-Cmake-fixes.patch
# Upstream deactivated building osgviewerWX for obscure reasons
# Reactivate for now.
Patch2:         0002-Activate-osgviewerWX.patch
# Unset DOT_FONTNAME
Patch3:         0003-Unset-DOT_FONTNAME.patch
# Re-add osgframerenderer
Patch4:         0004-Re-add-osgframerenderer.patch
# Force osgviewerWX to always use X11 backend (wxGLCanvas is broken on Wayland)
Patch5:         force-x11-backend.patch
# Minimal port to OpenEXR 3
# https://github.com/openscenegraph/OpenSceneGraph/issues/1075
Patch6:         OpenSceneGraph-openexr3.patch
# Fix build against recent asio
Patch7:         OpenSceneGraph_asio.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: asio-devel
BuildRequires: doxygen graphviz
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

Requires: lib%name

%ifarch %e2k
# error: cpio archive too big - 4321M
%global __find_debuginfo_files %nil
%endif

%description
The OpenSceneGraph is an OpenSource, cross platform graphics
toolkit for the development of high performance graphics
applications such as flight simulators, games, virtual reality
and scientific visualization.  Based around the concept of
a SceneGraph, it provides an object oriented framework on top
of OpenGL freeing the developer from implementing and optimizing
low level graphics calls, and provides many additional utilities
for rapid development of graphics applications.

%package -n lib%name
Summary: Development files for OpenSceneGraph
Group: System/Libraries
Requires: libOpenThreads

%description -n lib%name
Runtime libraries files for OpenSceneGraph

%package -n lib%name-devel
Summary: Development files for OpenSceneGraph
Group: Development/C++
Requires: lib%name
Requires: libOpenThreads-devel
Requires: pkgconfig

%description -n lib%name-devel
Development files for OpenSceneGraph

%package gdal
Summary: OSG Gdal plugin
Group: System/Libraries
Requires: lib%name

%description gdal
OSG Gdal plugin.

%package gstreamer
Summary: OSG gstreamer plugin
Group: System/Libraries
Requires: lib%name

%description gstreamer
OSG gstreamer plugin.

%package inventor
Summary: OSG inventor plugin
Group: System/Libraries
Requires: lib%name

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

%package -n libOpenThreads
Summary: OpenThreads
Group: System/Libraries
Provides: OpenThreads = %name-%version

%description -n libOpenThreads
OpenThreads is intended to provide a minimal & complete Object-Oriented
(OO) thread interface for C++ programmers.  It is loosely modeled on the
Java thread API, and the POSIX Threads standards.  The architecture of
the library is designed around "swappable" thread models which are
defined at compile-time in a shared object library.

%package -n libOpenThreads-devel
Summary: Development files for OpenThreads
Group: Development/C++
Requires: libOpenThreads = %version-%release

%description -n libOpenThreads-devel
Development files for OpenThreads

%prep
%setup
%autopatch -p1

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
# Supposed to take OpenSceneGraph data
mkdir -p %buildroot%_datadir/OpenSceneGraph

# hack for 3.4.x (it is ok since 3.6.0)
rm -rf %buildroot/usr/doc/

%files
%doc AUTHORS.txt LICENSE.txt NEWS.txt README.md
%_bindir/osgarchive
%_bindir/osgconv
%_bindir/osgviewer
%_bindir/osgfilecache
%_bindir/present3D

%files -n lib%name
%_libdir/osgPlugins-%version
%_libdir/libosg*.so.*
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

%files -n lib%name-devel
%doc %_cmake__builddir/doc/OpenSceneGraphReferenceDocs
%_includedir/osg*
%_pkgconfigdir/openscenegraph*.pc
%_libdir/libosg*.so
%_bindir/osgversion

%ifnarch %e2k
#files examples-SDL
#_bindir/osgviewerSDL

%files examples
%_bindir/osg2cpp
%_bindir/osgbindlesstext
%_bindir/osgdatabaserevisions
%_bindir/osgdeferred
%_bindir/osgfpdepth
%_bindir/osgframerenderer
%_bindir/osggpx
%_bindir/osggraphicscost
%_bindir/osgmultiviewpaging
%_bindir/osgobjectcache
%_bindir/osgoit
%_bindir/osgoutline
%_bindir/osgparticleshader
%_bindir/osgposter
#_bindir/osgqfont
%_bindir/osgshadercomposition
%_bindir/osgshadergen
%_bindir/osgtexturecompression
%_bindir/osgthreadedterrain
%_bindir/osguniformbuffer
%_bindir/osguserdata
%_bindir/osguserstats
%_bindir/osgvertexattributes
%_bindir/osgvirtualprogram
%_bindir/osganalysis
%_bindir/osganimationeasemotion
%_bindir/osganimationmorph
%_bindir/osganimationhardware
%_bindir/osganimationmakepath
%_bindir/osganimationnode
%_bindir/osganimationskinning
%_bindir/osganimationsolid
%_bindir/osganimationtimeline
%_bindir/osganimationviewer
%_bindir/osgautocapture
#_bindir/osgbrowser
%_bindir/osgcluster
%_bindir/osgdrawinstanced
%_bindir/osggameoflife
%_bindir/osgmemorytest
%_bindir/osgpackeddepthstencil
%_bindir/osgpdf
%_bindir/osgrobot
%_bindir/osgsidebyside
%_bindir/osgwidgetmessagebox
%_bindir/osgwidgetperformance
%_bindir/osgfont
%_bindir/osgimagesequence
%_bindir/osgkdtree
%_bindir/osgscreencapture
%_bindir/osgwidgetaddremove
%_bindir/osgwidgetbox
%_bindir/osgwidgetcanvas
%_bindir/osgwidgetframe
%_bindir/osgwidgetinput
%_bindir/osgwidgetlabel
%_bindir/osgwidgetmenu
%_bindir/osgwidgetnotebook
%_bindir/osgwidgetscrolled
%_bindir/osgwidgetshader
%_bindir/osgwidgetstyled
%_bindir/osgwidgettable
%_bindir/osgwidgetwindow
%_bindir/osggeometryshaders
%_bindir/osgmultiplerendertargets
%_bindir/osgmultitexturecontrol
%_bindir/osgocclusionquery
%_bindir/osgsharedarray
%_bindir/osgstereomatch
%_bindir/osgtext3D
%_bindir/osgthirdpersonview
%_bindir/osgdepthpeeling
%_bindir/osganimate
%_bindir/osgautotransform
%_bindir/osgbillboard
%_bindir/osgblendequation
%_bindir/osgcallback
%_bindir/osgcamera
%_bindir/osgcatch
%_bindir/osgclip
%_bindir/osgcompositeviewer
%_bindir/osgcopy
%_bindir/osgcubemap
#_bindir/osgdelaunay
%_bindir/osgdepthpartition
%_bindir/osgdistortion
%_bindir/osgfadetext
%_bindir/osgforest
%_bindir/osgfxbrowser
#_bindir/osggeodemo
%_bindir/osggeometry
%_bindir/osghangglide
%_bindir/osghud
%_bindir/osgimpostor
%_bindir/osgintersection
#_bindir/osgintrospection
%_bindir/osgkeyboard
%_bindir/osgkeyboardmouse
%_bindir/osglauncher
%_bindir/osglight
%_bindir/osglightpoint
%_bindir/osglogicop
%_bindir/osglogo
%_bindir/osgmanipulator
%_bindir/osgmotionblur
%_bindir/osgmovie
%_bindir/osgmultitexture
%_bindir/osgoccluder
%_bindir/osgpagedlod
%_bindir/osgparametric
%_bindir/osgparticle
%_bindir/osgparticleeffects
%_bindir/osgpick
%_bindir/osgplanets
%_bindir/osgpoints
%_bindir/osgpointsprite
%_bindir/osgprecipitation
%_bindir/osgprerender
%_bindir/osgprerendercubemap
%_bindir/osgreflect
%_bindir/osgsampler
%_bindir/osgscalarbar
%_bindir/osgscribe
%_bindir/osgsequence
%_bindir/osgshaders
%_bindir/osgshadermultiviewport
%_bindir/osgshaderpipeline
%_bindir/osgshaderterrain
%_bindir/osgshadow
%_bindir/osgshape
%_bindir/osgsimpleMDI
%_bindir/osgsimplifier
%_bindir/osgslice
%_bindir/osgspacewarp
%_bindir/osgspheresegment
%_bindir/osgspotlight
%_bindir/osgstereoimage
%_bindir/osgteapot
%_bindir/osgterrain
%_bindir/osgtessellate
%_bindir/osgtext
%_bindir/osgtexture1D
%_bindir/osgtexture2D
%_bindir/osgtexture3D
%_bindir/osgtexturerectangle
%_bindir/osgunittests
%_bindir/osgvertexprogram
#_bindir/osgviewerGLUT
%_bindir/osgviewerWX
%_bindir/osgvolume
%_bindir/osgvnc
%_bindir/osgwindows

%_bindir/osgphotoalbum
%_bindir/osgsimulation

%_bindir/osgatomiccounter
%_bindir/osgcomputeshaders
#_bindir/osgframerenderer
%_bindir/osgkeystone
%_bindir/osgmultiplemovies
%_bindir/osgmultitouch
%_bindir/osgoscdevice
%_bindir/osgsimplegl3
%_bindir/osgsimpleshaders
%_bindir/osgtessellationshaders

%_bindir/osgSSBO
%_bindir/osgblenddrawbuffers
%_bindir/osggpucull
%_bindir/osgtexture2DArray
%_bindir/osgtransferfunction
%_bindir/osgtransformfeedback

%_bindir/osgviewerGTK

%_datadir/OpenSceneGraph
%endif

%files -n libOpenThreads
%doc AUTHORS.txt LICENSE.txt NEWS.txt README.md
%_libdir/libOpenThreads.so.*

%files -n libOpenThreads-devel
%doc %_cmake__builddir/doc/OpenThreadsReferenceDocs
%_pkgconfigdir/openthreads.pc
%_libdir/libOpenThreads.so
%_includedir/OpenThreads

%changelog
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
