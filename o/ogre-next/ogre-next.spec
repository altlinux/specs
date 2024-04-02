%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define oname OGRE-Next
%set_verify_elf_method strict,rpath=relaxed,unresolved=relaxed
%set_fixup_method skip

Name: ogre-next
Version: 2.3.3
Release: alt4
Summary: Object-Oriented Graphics Rendering Engine 
# CC-BY-SA is for devel docs
License: MIT
Group: System/Libraries
Url: https://ogrecave.github.io/ogre-next/api/latest/

# https://github.com/OGRECave/ogre
Source: %name-%version.tar
Patch0: 0001-fix-ogre-next-version.patch

BuildRequires: gcc-c++ cmake
BuildRequires: zziplib-devel libfreetype-devel libgtk+2-devel libois-devel openexr-devel cppunit-devel
BuildRequires: doxygen graphviz texi2html libtbb-devel boost-devel
BuildRequires: libXaw-devel libXrandr-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel
BuildRequires: libXinerama-devel libXi-devel libXpm-devel libXv-devel libXxf86misc-devel xorg-xf86miscproto-devel
BuildRequires: libXxf86vm-devel libXext-devel libGLU-devel libfreeimage-devel tinyxml-devel
BuildRequires: libharfbuzz-devel libGLES-devel libpoco-devel
BuildRequires: libGLEW-devel rapidjson-devel 
BuildRequires: libSDL2-devel
BuildRequires: libgtest-devel
BuildRequires: libpugixml-devel
BuildRequires: libfreetype-devel
BuildRequires: zlib-devel
Conflicts: ogre

ExclusiveArch: x86_64

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
Conflicts: libogre

%description -n lib%name
Ogre is a complete object-oriented 3D rendering engine. It supports
different rendering subsystems but only the OpenGL system is useful
for Linux.

This package contains the Ogre library and plugins.

%package -n lib%name-devel
Summary: Object-oriented Graphics Rendering Engine (development files)
Group: Development/C
Requires: lib%name = %EVR
Conflicts: libogre-devel

%set_fixup_method skip

%description -n lib%name-devel
Ogre is a complete object-oriented 3D rendering engine. It supports
different rendering subsystems but only the OpenGL system is useful
for Linux.

This package contains the headers needed to develop with Ogre.

%package %name-devel-doc
Summary: Ogre development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: ogre-devel-doc

%description %name-devel-doc
This package contains the Ogre API documentation and the Ogre development
manual. Install this package if you want to develop programs that use Ogre.

%package samples
Summary: Ogre samples executables and media
Group: Development/Other
Requires: %name = %EVR
Conflicts: ogre-samples

%description samples
This package contains the compiled (not the source) sample applications coming
with Ogre.  It also contains some media (meshes, textures,...) needed by these
samples.

%prep
%setup

%patch0 -p1

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
	-DOGRE_LIB_DIRECTORY=%_lib \
	-DOGRE_INSTALL_SAMPLES=ON \
	-DOGRE_USE_NEW_PROJECT_NAME=ON \
	-DOGRE_BUILD_TESTS=ON \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DOpenGL_GL_PREFERENCE=GLVND \
	-DOGRE_SIMD_NEON:BOOL=FALSE \
	%nil

%cmake_build

%install
%cmakeinstall_std

# cmake macros should be in the cmake directory, not an Ogre directory
mkdir -p %buildroot%_datadir/cmake/Modules
mv %buildroot%_libdir/%oname/cmake/* %buildroot%_datadir/cmake/Modules

%files
%doc AUTHORS
%_bindir/Ogre*
%_bindir/Test_*
%dir %_datadir/%oname
%config(noreplace) %_datadir/%oname/plugins.cfg
%config(noreplace) %_datadir/%oname/resources.cfg
%config(noreplace) %_datadir/%oname/tests.cfg
%config(noreplace) %_datadir/%oname/HiddenAreaMeshVr.cfg
%config(noreplace) %_datadir/%oname/plugins_tools.cfg
%config(noreplace) %_datadir/%oname/resources2.cfg

%_datadir/%oname/Media

%files -n lib%name
%dir %_libdir/%oname
%_libdir/libOgre*.so.*
%_libdir/%oname/*.so*

%files  -n lib%name-devel
%_libdir/libOgre*.so
%_libdir/pkgconfig/*
%_datadir/cmake/Modules
%_includedir/%oname

#files %name-devel-doc
%_datadir/%oname/docs

%files samples
%_bindir/Sample_*

%changelog
* Mon Apr  1 2024 Artyom Bystrov <arbars@altlinux.org> 2.3.3-alt4
- test build

* Tue Jan 30 2024 Artyom Bystrov <arbars@altlinux.org> 2.3.3-alt3
- Fixed version for pkgconfig files

* Mon Jan 29 2024 Artyom Bystrov <arbars@altlinux.org> 2.3.3-alt2
- Getting back pkgconfig files

* Mon Jan 15 2024 Artyom Bystrov <arbars@altlinux.org> 2.3.3-alt1
- Initial build
