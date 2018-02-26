#
# Copyright (c) 2005, 2006, 2007, 2008, 2009 Ralf Corsepius, Ulm, Germany.
# Copyright (c) 2009 Michael Shigorin
# Copyright (c) 2011 Dmitry Derjavin
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%define apiver 3.0.1
%define osgbranch 3.0

Name: OpenSceneGraph
Version: 3.0.1
Release: alt2

Summary: High performance real-time graphics toolkit
License: OSGPL (wxWidgets, clarified LGPL)
Group: System/Libraries

Url: http://www.openscenegraph.org
Source: %url/downloads/stable_releases/OpenSceneGraph-%osgbranch/OpenSceneGraph-%version.zip
Patch: OpenSceneGraph-3.0.0-alt-cmake.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Nov 30 2011
# optimized out: cmake-modules fontconfig fontconfig-devel fonts-ttf-liberation glib2-devel libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXau-devel libXcursor-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXrandr-devel libXrender-devel libXt-devel libXv-devel libatk-devel libcairo-devel libcurl-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libjpeg-devel libpango-devel libpng-devel libpoppler8-glib libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-webkit libqt4-xml libstdc++-devel libtiff-devel pkg-config xml-utils xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
BuildRequires: cmake doxygen gcc-c++ gnuplot graphviz libInventor-devel libSDL-devel libXScrnSaver-devel libXcomposite-devel libXdmcp-devel libXpm-devel libXtst-devel libXxf86misc-devel libfreeglut-devel libgif-devel libgtkglext-devel libopenal-devel libpoppler-glib-devel librsvg-devel libwxGTK-devel libxkbfile-devel libxml2-devel phonon-devel unzip wget

#BuildRequires: libpixman-devel

%description
The OpenSceneGraph is an OpenSource, cross platform graphics
toolkit for the development of high performance graphics
applications such as flight simulators, games, virtual reality
and scientific visualization.  Based around the concept of
a SceneGraph, it provides an object oriented framework on top
of OpenGL freeing the developer from implementing and optimizing
low level graphics calls, and provides many additional utilities
for rapid development of graphics applications.

%prep
%setup
%patch -p1

%build
mkdir BUILD
pushd BUILD
cmake -DCMAKE_BUILD_TYPE="Release" -DCMAKE_INSTALL_PREFIX:PATH=%_usr \
      -DBUILD_OSG_EXAMPLES=ON -DBUILD_OSG_WRAPPERS=ON -DBUILD_DOCUMENTATION=ON \
      ..
# still uses single CPU core
%make_build VERBOSE=1
make doc_openscenegraph doc_openthreads
popd

%install
pushd BUILD
%makeinstall_std
# Supposed to take OpenSceneGraph data
mkdir -p %buildroot%_datadir/OpenSceneGraph
popd

%files
%doc AUTHORS.txt LICENSE.txt NEWS.txt README.txt
%_bindir/osgarchive
%_bindir/osgconv
%_bindir/osgviewer
%_bindir/osgviewerGTK
%_bindir/osgfilecache

%package -n lib%name
Summary: Development files for OpenSceneGraph
Group: System/Libraries
Requires: libOpenThreads = %version-%release
Provides: %name = %version-%release

%description -n lib%name
Runtime libraries files for OpenSceneGraph

%files -n lib%name
%_libdir/osgPlugins-%apiver
%_libdir/libosg*.so.*

%package -n lib%name-devel
Summary: Development files for OpenSceneGraph
Group: Development/C++
Requires: lib%name = %version-%release
Requires: libOpenThreads-devel = %version-%release
Requires: pkgconfig

%description -n lib%name-devel
Development files for OpenSceneGraph

%files -n lib%name-devel
%doc BUILD/doc/OpenSceneGraphReferenceDocs
%_includedir/osg*
%_pkgconfigdir/openscenegraph*.pc
%_libdir/libosg*.so
%_bindir/osgversion

%package examples-SDL
Summary: OSG sample applications using SDL
Group: Development/Documentation

%description examples-SDL
OSG sample applications using SDL

%files examples-SDL
%_bindir/osgviewerSDL

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

%package examples-qt
Summary: OSG sample applications using qt
Group: Development/Documentation

%description examples-qt
OSG sample applications using qt

%files examples-qt
%_bindir/osgviewerQt
%_bindir/osgQtBrowser
%_bindir/osgQtWidgets

# OpenSceneGraph-examples
%package examples
Summary: Sample applications for OpenSceneGraph
Group: Development/Documentation

%description examples
Sample applications for OpenSceneGraph

%files examples
%_bindir/osg2cpp
%_bindir/osgdatabaserevisions
%_bindir/osgfpdepth
%_bindir/osggpx
%_bindir/osggraphicscost
%_bindir/osgmultiviewpaging
%_bindir/osgoit
%_bindir/osgoutline
%_bindir/osgparticleshader
%_bindir/osgposter
%_bindir/osgqfont
%_bindir/osgshadercomposition
%_bindir/osgshadergen
%_bindir/osgtexturecompression
%_bindir/osgthreadedterrain
%_bindir/osguniformbuffer
%_bindir/osguserdata
%_bindir/osguserstats
%_bindir/osgvertexattributes
%_bindir/osgvirtualprogram
%_bindir/present3D
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
%_bindir/osgdelaunay
%_bindir/osgdepthpartition
%_bindir/osgdistortion
%_bindir/osgfadetext
%_bindir/osgforest
%_bindir/osgfxbrowser
%_bindir/osggeodemo
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
%_bindir/osgscalarbar
%_bindir/osgscribe
%_bindir/osgsequence
%_bindir/osgshaders
%_bindir/osgshaderterrain
%_bindir/osgshadow
%_bindir/osgshape
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
%_bindir/osgviewerGLUT
%_bindir/osgviewerWX
%_bindir/osgvolume
%_bindir/osgwindows

%_bindir/osgphotoalbum
%_bindir/osgsimulation

%_datadir/OpenSceneGraph

# libOpenThreads
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

%files -n libOpenThreads
%doc AUTHORS.txt LICENSE.txt NEWS.txt README.txt
%_libdir/libOpenThreads.so.*

# libOpenThreads-devel
%package -n libOpenThreads-devel
Summary: Development files for OpenThreads
Group: Development/C++
Requires: libOpenThreads = %version-%release

%description -n libOpenThreads-devel
Development files for OpenThreads

%files -n libOpenThreads-devel
%doc BUILD/doc/OpenThreadsReferenceDocs
%_pkgconfigdir/openthreads.pc
%_libdir/libOpenThreads.so
%_includedir/OpenThreads

%changelog
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
