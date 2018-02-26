Name: ogre
Version: 1.8.0
Release: alt1
Summary: Object-Oriented Graphics Rendering Engine
# CC-BY-SA is for devel docs
License: MIT
Group: System/Libraries
Url: http://www.ogre3d.org/
Source: %name-%version.tar
Patch: %name-%version-alt-changes.patch
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires: gcc-c++ cmake cegui-devel zziplib-devel libfreetype-devel libgtk+2-devel libois-devel openexr-devel cppunit-devel doxygen libtbb-devel boost-devel
BuildRequires: libXaw-devel libXrandr-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXinerama-devel libXi-devel libXpm-devel libXv-devel libXxf86misc-devel xorg-xf86miscproto-devel libXxf86vm-devel libXext-devel libGLU-devel libfreeimage-devel tinyxml-devel
#BuildRequires:  glew-devel 

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
Requires: lib%name = %version-%release

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
Requires: %name = %version-%release

%description samples
This package contains the compiled (not the source) sample applications coming
with Ogre.  It also contains some media (meshes, textures,...) needed by these
samples.

%prep
%setup -q -n ogre
%patch -p1

%build
%cmake \
	-DOGRE_LIB_DIRECTORY=%_lib \
	-DOGRE_INSTALL_SAMPLES=ON \
	-DOGRE_BUILD_TESTS=ON \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags"

%make_build -C BUILD

%install
%make install DESTDIR=$RPM_BUILD_ROOT -C BUILD

# Create config for ldconfig
mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo "%_libdir/OGRE" > $RPM_BUILD_ROOT/etc/ld.so.conf.d/%name-%_arch.conf

mkdir -p $RPM_BUILD_ROOT%_man1dir
#install -p -m 644 OgreMaterialUpgrade.1 $RPM_BUILD_ROOT%_man1dir/OgreMaterialUpgrade.1
install -p -m 644 OgreMeshUpgrade.1 $RPM_BUILD_ROOT%_man1dir/OgreMeshUpgrade.1
install -p -m 644 OgreXMLConverter.1 $RPM_BUILD_ROOT%_man1dir/OgreXMLConverter.1

#Copy working samples
cp -f samples.cfg $RPM_BUILD_ROOT%_datadir/OGRE/samples.cfg

%files
%doc AUTHORS BUGS COPYING
/etc/ld.so.conf.d/*
%_bindir/Ogre*
%_bindir/Test_Ogre
%dir %_datadir/OGRE
%config(noreplace) %_datadir/OGRE/plugins.cfg
%config(noreplace) %_datadir/OGRE/quakemap.cfg
%config(noreplace) %_datadir/OGRE/resources.cfg
%config(noreplace) %_datadir/OGRE/tests.cfg
%_datadir/OGRE/media
%_man1dir/*

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
%doc Docs/api Docs/licenses Docs/manual Docs/shadows Docs/vbo-update Docs/*html Docs/*gif Docs/*.css

%files samples
%config(noreplace) %_datadir/OGRE/samples.cfg
%_bindir/SampleBrowser
%_libdir/OGRE/Samples

%changelog
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
