%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,rpath=relaxed,unresolved=relaxed

Name: ogre
Version: 13.5.1
Release: alt1
Summary: Object-Oriented Graphics Rendering Engine
# CC-BY-SA is for devel docs
License: MIT
Group: System/Libraries
Url: https://www.ogre3d.org/
ExcludeArch: %ix86

# https://github.com/OGRECave/ogre
Source: %name-%version.tar

# https://github.com/ocornut/imgui
Source1: %name-%version-imgui.tar

Patch1: ogre-alt-build.patch

BuildRequires: gcc-c++ cmake
BuildRequires: zziplib-devel libfreetype-devel libgtk+2-devel libois-devel openexr-devel cppunit-devel
BuildRequires: doxygen graphviz texi2html libtbb-devel boost-devel
BuildRequires: libXaw-devel libXrandr-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel
BuildRequires: libXinerama-devel libXi-devel libXpm-devel libXv-devel libXxf86misc-devel xorg-xf86miscproto-devel
BuildRequires: libXxf86vm-devel libXext-devel libGLU-devel libfreeimage-devel tinyxml-devel
BuildRequires: libharfbuzz-devel libGLES-devel libpoco-devel
BuildRequires: libGLEW-devel
BuildRequires: libSDL2-devel
BuildRequires: libgtest-devel
BuildRequires: libpugixml-devel
BuildRequires: libfreetype-devel
BuildRequires: zlib-devel

%description
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier and more
intuitive for developers to produce applications utilising
hardware-accelerated 3D graphics. The class library abstracts all the
details of using the underlying system libraries like Direct3D and
OpenGL and provides an interface based on world objects and other
intuitive classes.

%package -n lib%name
Summary: Object-oriented Graphics Rendering Engine (libraries)
Group: System/Libraries

%description -n lib%name
Ogre is a complete object-oriented 3D rendering engine. It supports
different rendering subsystems but only the OpenGL system is useful
for Linux.

This package contains the Ogre library and plugins.

%package -n lib%name-devel
Summary: Object-oriented Graphics Rendering Engine (development files)
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Ogre is a complete object-oriented 3D rendering engine. It supports
different rendering subsystems but only the OpenGL system is useful
for Linux.

This package contains the headers needed to develop with Ogre.

%package devel-doc
Summary: Ogre development documentation
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
This package contains the Ogre API documentation and the Ogre development
manual. Install this package if you want to develop programs that use Ogre.

%package samples
Summary: Ogre samples executables and media
Group: Development/Other
Requires: %name = %EVR

%description samples
This package contains the compiled (not the source) sample applications coming
with Ogre.  It also contains some media (meshes, textures,...) needed by these
samples.

%prep
%setup
%patch1 -p1

mkdir %_cmake__builddir
pushd %_cmake__builddir &>/dev/null
tar xvf %SOURCE1
popd


%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -print0 -name '*.cpp' -o -name '*.hpp' -name '*.h' |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.20
%add_optflags -std=c++11
%endif
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	-DOGRE_LIB_DIRECTORY=%_lib \
	-DOGRE_INSTALL_SAMPLES=ON \
	-DOGRE_BUILD_TESTS=ON \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DOpenGL_GL_PREFERENCE=GLVND \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS LICENSE
%_bindir/Ogre*
%_bindir/Test_Ogre*
%_bindir/VRMLConverter
%dir %_datadir/OGRE
%_datadir/OGRE/GLX_backdrop.png
%config(noreplace) %_datadir/OGRE/plugins.cfg
%config(noreplace) %_datadir/OGRE/resources.cfg
%_datadir/OGRE/Media

%exclude %_datadir/OGRE/samples.cfg

%files -n lib%name
%dir %_libdir/OGRE
%_libdir/libOgre*.so.*
%_libdir/OGRE/*.so*

%files  -n lib%name-devel
%_libdir/libOgre*.so
%_libdir/pkgconfig/*
%_libdir/OGRE/cmake
%_includedir/OGRE

%files devel-doc
%_defaultdocdir/OGRE

%files samples
%config(noreplace) %_datadir/OGRE/samples.cfg
%_bindir/SampleBrowser
%_libdir/OGRE/Samples

%changelog
* Sun Nov 20 2022 Anton Farygin <rider@altlinux.ru> 13.5.1-alt1
- 13.2.4 -> 13.5.1

* Mon Oct 24 2022 Artyom Bystrov <arbars@altlinux.org> 13.2.4-alt3
- Fixed build.

* Wed Feb 09 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 13.2.4-alt2
- Fixed build.

* Wed Jan 12 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 13.2.4-alt1
- Updated to upstream version 13.2.4.

* Tue Apr 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt4
- Rebuilt without glsl-optimizer and hlsl2glsl.

* Wed Feb 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt3
- Fixed build on armh and rebuilt with new boost libraries.

* Wed Oct 02 2019 Michael Shigorin <mike@altlinux.org> 1.9.0-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24; explicit -std=c++11

* Tue Aug 13 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.9.0-alt1.2.qa1
- Rebuilt without libcg.

* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1.2
- NMU: aarch64 build

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt1.1.1.3
- NMU: rebuilt with boost-1.67.0

* Mon Sep 04 2017 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1.1.1.2
- Rebuild with boost 1.65

* Fri Jul 21 2017 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1.1.1.1
- Rebuild with new libcppunit

* Tue Jun 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.9.0-alt1.1.1
- Rebuilt for gcc5 C++11 ABI.
- Removed BR: cegui-devel (needed by some samples).

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.9.0-alt1.1
- rebuild with boost 1.57.0

* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Version 1.9.0

* Tue Dec 31 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.9.0-alt1
- New version

* Tue Jul 23 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.1-alt1
- New version

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.3
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.2
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.1
- Rebuilt with Boost 1.51.0

* Sat May 26 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.0-alt1
- New version

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3-alt1.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3-alt1.2
- Rebuilt with Boost 1.48.0

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3-alt1.1
- Rebuilt with Boost 1.47.0

* Wed May 11 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.3-alt1
- New version

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.2
- Rebuilt with Boost 1.46.1

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.1
- Rebuilt for debuginfo

* Sun Nov 14 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.2-alt1
- New version

* Sat May 15 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.1-alt1
- New version

* Sat Mar 20 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.0-alt1
- New version
- Update spec for new build system
- Change license to MIT

* Wed Oct 07 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.4-alt2
- Fix path in samples config
- Add %_libdir/OGRE to package

* Mon Oct 05 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.4-alt1
- New version

* Wed Jun 17 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.6.2-alt1
- Build for ALT
