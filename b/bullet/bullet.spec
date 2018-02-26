%def_disable demo
%def_disable static
%if "%_lib" == "lib64"
%define LIB_SUFFIX="64"
%else
%define LIB_SUFFIX=""
%endif

Name: bullet
Version: 2.77
Release: alt1.2
License: Zlib
Summary: Professional 3D collision detection library
Group: System/Libraries
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Url: http://www.bulletphysics.com
Source: http://bullet.googlecode.com/files/%name-%version.tar
Patch: %name-%version-alt-changes.patch

# Automatically added by buildreq on Fri Sep 18 2009
BuildRequires: cmake gcc-c++ libGL-devel libfreeglut-devel xorg-xf86vidmodeproto-devel

%description
Bullet is a professional open source multi-threaded
3D Collision Detection and Rigid Body Dynamics Library
for games and animation.

%package demo
Summary: A demo programs using bullet library
Group: Graphics
Requires: lib%name = %version-%release

%description demo
A demo programs using bullet library.

%package -n lib%name
Summary: Professional 3D collision detection library
Group: System/Libraries

%description -n lib%name
Bullet 3D Game Multiphysics Library provides state of the art
collision detection, soft body and rigid body dynamics.

* Used by many game companies in AAA titles on Playstation 3,
  XBox 360, Nintendo Wii and PC
* Modular extendible C++ design with hot-swap of most components
* Optimized back-ends with multi-threaded support for Playstation 3
  Cell SPU and other platforms
* Discrete and continuous collision detection (CCD)
* Swept collision queries
* Ray casting with custom collision filtering
* Generic convex support (using GJK), capsule, cylinder, cone, sphere,
  box and non-convex triangle meshes.
* Rigid body dynamics including constraint solvers, generic
  constraints, ragdolls, hinge, ball-socket
* Support for constraint limits and motors
* Soft body support including cloth, rope and deformable
* Bullet is integrated into Blender 3D and provides a Maya Plugin
* Supports import and export into COLLADA 1.4 Physics format
* Support for dynamic deformation of non-convex triangle meshes, by
  refitting the acceleration structures

The Library is free for commercial use and open source
under the ZLib License.

%package -n lib%name-devel
Summary: Development headers for bullet
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development headers for bullet 3D collision library.

%package -n lib%name-devel-static
Summary: Static library for bullet
Group: Development/C

%description -n lib%name-devel-static
Static library for bullet

%prep
%setup -q -n %name-%version
%patch -p1

%build
%add_optflags -fpermissive
%cmake \
		-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
		-DCMAKE_C_FLAGS:STRING="%optflags" \
		-DCMAKE_CXX_FLAGS:STRING="%optflags" \
    -DINSTALL_LIBS=ON \
    -DCMAKE_SKIP_RPATH:BOOL=yes \
    -DCMAKE_SKIP_RPATH:BOOL=yes \
    -DBUILD_EXTRAS=OFF \
    %{?_disable_demo:-DBUILD_DEMOS=OFF} \
    %{?_disable_static:-DBUILD_SHARED_LIBS=ON}

%make_build -C BUILD

%install
%make install DESTDIR=%buildroot -C BUILD

%if_enabled demo
#BasicDemo TerrainDemo VehicleDemo CcdPhysicsDemo ColladaDemo SoftDemo AllBulletDemos MultiThreadedDemo
demos=`ls -1 *Demo`
for i in $demos AllBulletDemos ContinuousConvexCollision BulletDino Raytracer UserCollisionAlgorithm; do
    install -m 755 $i %buildroot%_bindir/bullet-$i
done

%files demo
%_bindir/%name-*
%endif

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc AUTHORS README LICENSE ChangeLog NEWS VERSION *.pdf
%_libdir/pkgconfig/%name.pc
%_includedir/*
%if_disabled static
%_libdir/*.so
%else
%files -n lib%name-devel-static
%_libdir/*.a
%endif #static

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.77-alt1.2
- Fixed build

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.77-alt1.1
- Rebuilt for debuginfo

* Wed Dec 08 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.77-alt1
- New release

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.76-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun Feb 28 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.76-alt1
- New release

* Sun Nov 08 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.75-alt5
- Fix build. Remove rpm-build-compat from BuildRequires

* Tue Sep 15 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.75-alt4
- Change configure system (ALT #21574)
- Not build by default lib%name-devel-static

* Sat Sep 12 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.75-alt3
- Release
- Rename lib%name-static to lib%name-devel-static

* Mon Jul 06 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.75-alt2.rc3
- Fix requires

* Sun Jun 21 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.75-alt1.rc3
- Build for ALT
