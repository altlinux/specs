%filter_from_provides /^pkgconfig.OGRE/d
%filter_from_requires /^pkgconfig.OGRE/d
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++ texinfo
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define oldname ogre
%define	oname OGRE

Summary:	Object-Oriented Graphics Rendering Engine
Name:		ogre19
Version:	1.9.1
Release:	alt1_12

%define soname %{version}
%define libname lib%{name}%{soname}
%define	develname lib%{name}-devel

License:	MIT
Group:		System/Libraries
URL:		https://www.ogre3d.org
Source0:	https://github.com/OGRECave/ogre/archive/v%{version}/%{oldname}-%{version}.tar.gz

Patch0:		ogre-1.9.0-cmake-ois-check.patch
Patch1:		ogre-1.9.1-dynlib-allow-no-so.patch
Patch2:		ogre-1.9.1-fix-version.patch
Patch3:		ogre-1.9.1-glibc2.32.patch

BuildRequires:	boost-complete
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	libfreeimage-devel
BuildRequires:	libatomic-devel-static
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(OIS)
BuildRequires:	pkgconfig(tbb)
BuildRequires:	pkgconfig(tinyxml)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(zziplib)

Source44: import.info

Conflicts:	ogre
Conflicts:	libogre

%description
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n %{libname}
Summary:	Libraries needed for programs using %{oname}
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{libname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n %{develname}
Summary:	Development headers and libraries for writing programs using %{oname}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
#Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

Conflicts:	libogre
Conflicts:	libogre-devel

%description -n %{develname}
Development headers and libraries for writing programs using %{oname}.

%prep
%setup -q -n %oldname-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
%{mageia_cmake} \
    -DOGRE_BUILD_DOCS=OFF \
    -DOGRE_BUILD_RENDERSYSTEM_GL=ON \
    -DOGRE_BUILD_RENDERSYSTEM_GL3PLUS=ON \
    -DOGRE_BUILD_RENDERSYSTEM_GLES2=ON \
    -DOGRE_BUILD_SAMPLES=OFF \
    -DOGRE_BUILD_TESTS=OFF \
    -DOGRE_BUILD_TOOLS=ON \
    -DOGRE_INSTALL_DOCS=OFF \
    -DOGRE_INSTALL_SAMPLES=OFF \
    -DOGRE_INSTALL_TOOLS=ON \
    -DOGRE_STATIC=OFF
%mageia_cmake_build

%install
%mageia_cmake_install

%files
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter

%files -n %{libname}
%{_libdir}/libOgre*.so.%{soname}
%dir %{_libdir}/%{oname}
%{_libdir}/%{oname}/*.so.%{soname}

%files -n %{develname}
%{_libdir}/libOgre*.so
%{_libdir}/pkgconfig/%{oname}*.pc
%{_libdir}/%{oname}/*.so
%{_libdir}/%{oname}/cmake/
%{_includedir}/%{oname}/


%changelog
* Sun Jan 16 2022 Igor Vlasenko <viy@altlinux.org> 1.9.1-alt1_12
- compat version

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
