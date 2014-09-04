%define oname bullet
%def_disable demo
%def_disable static

Name: %{oname}3
Version: 2.83
Release: alt1.alpha

Summary: Professional 3D collision detection library
License: Zlib
Group: System/Libraries
Url: http://www.bulletphysics.com

# https://github.com/bulletphysics/bullet3.git
Source: %name-%version.tar

BuildRequires: cmake gcc-c++ libGL-devel libGLUT-devel libICE-devel
BuildPreReq: libXi-devel libXmu-devel libXres-devel libxshmfence-devel
BuildPreReq: libxcbutil-image-devel libXtst-devel libXcomposite-devel
BuildPreReq: libXcursor-devel libXdamage-devel libXdmcp-devel
BuildPreReq: libXft-devel libXinerama-devel libxkbfile-devel
BuildPreReq: libXpm-devel libXrandr-devel libXScrnSaver-devel
BuildPreReq: libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildPreReq: libGLEW-devel

%description
Bullet is a professional open source multi-threaded 3D Collision
Detection and Rigid Body Dynamics Library for games and animation.

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
Conflicts: lib%oname-devel

%description -n lib%name-devel
Development headers for bullet 3D collision library.

%package -n lib%name-devel-static
Summary: Static library for bullet
Group: Development/C
Conflicts: lib%oname-devel-static

%description -n lib%name-devel-static
Static library for bullet

%prep
%setup
subst 's/-L@LIB_DESTINATION@/-L@LIB_INSTALL_DIR@/' %oname.pc.cmake

%build
%cmake \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
		-DCMAKE_STRIP:FILEPATH="/bin/echo" \
    -DINSTALL_LIBS=ON \
    -DBUILD_EXTRAS=ON \
		-DINSTALL_EXTRA_LIBS:BOOL=ON \
		-DUSE_CUSTOM_VECTOR_MATH:BOOL=ON \
		-DUSE_DOUBLE_PRECISION:BOOL=ON \
    -DINCLUDE_INSTALL_DIR=%_includedir/%oname \
		-DBUILD_BULLET2_DEMOS:BOOL=OFF \
    %{?_disable_demo:-DBUILD_DEMOS=OFF} \
    %{?_disable_static:-DBUILD_SHARED_LIBS=ON}

%cmake_build

%install
%cmakeinstall_std

%if_enabled demo
demos=`ls -1 *Demo`
for i in $demos AllBulletDemos ContinuousConvexCollision BulletDino Raytracer UserCollisionAlgorithm; do
    install -m 755 $i %buildroot%_bindir/%name-$i
done

%files demo
%_bindir/%name-*
%endif

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc readme.txt docs/*
%_libdir/pkgconfig/%oname.pc
%_includedir/*
%_libdir/cmake/%oname
%if_disabled static
%_libdir/*.so
%else
%files -n lib%name-devel-static
%_libdir/*.a
%endif #static

%changelog
* Thu Sep 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.83-alt1.alpha
- Initial build for Sisyphus

