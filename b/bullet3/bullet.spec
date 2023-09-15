%define _unpackaged_files_terminate_build 1

%define oname bullet
%def_disable demo

Name: bullet3
Version: 3.25
Release: alt2

Summary: Professional 3D collision detection library

License: Zlib
Group: System/Libraries
Url: http://www.bulletphysics.com
VCS: https://github.com/bulletphysics/bullet3.git

Source: %name-%version.tar

# patch from https://svnweb.mageia.org/packages/cauldron/bullet/current/SOURCES/bullet-3.24-fix-bullet-config.cmake.patch?revision=1919697&view=markup
Patch0: bullet-3.24-fix-bullet-config.cmake.patch

Patch1: bullet-3.24-use-system-libs.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libICE-devel
BuildRequires: pkgconfig(freeglut)
BuildRequires: pkgconfig(tinyxml2)
BuildRequires: pkgconfig(libglvnd)

%description
Bullet is a professional open source multi-threaded 3D Collision
Detection and Rigid Body Dynamics Library for games and animation.

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

%package -n lib%name-extras
Summary: Extra libraries for %name
Group: System/Libraries
License: Zlib and LGPLv2+

%description -n lib%name-extras
Extra libraries for %name.

%package -n lib%name-extras-devel
Summary: Development files for %name extras
Group: Development/C
License: Zlib and LGPLv2+
Requires: lib%name-extras = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-extras-devel
Development headers and libraries for %name extra libraries.

%prep
%setup
%autopatch -p1

%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -print0 -name '*.cpp' -o -name '*.hpp' -o -name '*.cc' -o -name '*.h' |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

rm -rv build3/*.{bat,exe}
rm -rv build3/*osx*
rm -rv build3/premake*
rm -rv {data/,examples/}

%build
%cmake \
    -DBUILD_BULLET_ROBOTICS_EXTRA=OFF \
    -DBUILD_BULLET_ROBOTICS_GUI_EXTRA=OFF \
    -DBUILD_EXTRAS=ON \
    -DBUILD_OBJ2SDF_EXTRA=OFF \
    -DBUILD_UNIT_TESTS=OFF \
    -DCLSOCKET_DEP_ONLY=ON \
    -DCLSOCKET_SHARED=ON \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_STRIP:FILEPATH="/bin/echo" \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DINSTALL_EXTRA_LIBS=ON \
    -DINSTALL_LIBS=ON \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DUSE_CUSTOM_VECTOR_MATH=ON \
    -DUSE_DOUBLE_PRECISION=ON \
    -DINCLUDE_INSTALL_DIR=%_includedir/%oname \
%if_disabled demo
    -DBUILD_BULLET2_DEMOS=OFF \
    -DBUILD_CPU_DEMOS=OFF} \
    -DBUILD_DEMOS=OFF \
    -DBUILD_OPENGL_DEMOS=OFF \
%endif
    -DBUILD_SHARED_LIBS=ON \
%nil

%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc README.md LICENSE.txt AUTHORS.txt
%_libdir/libBullet3Collision.so.*
%_libdir/libBullet3Common.so.*
%_libdir/libBullet3Dynamics.so.*
%_libdir/libBullet3Geometry.so.*
%_libdir/libBullet3OpenCL_clew.so.*
%_libdir/libBulletCollision.so.*
%_libdir/libBulletDynamics.so.*
%_libdir/libBulletInverseDynamics.so.*
%_libdir/libBulletSoftBody.so.*
%_libdir/libLinearMath.so.*

%files -n lib%name-devel
%dir %_includedir/%oname
%_includedir/%oname/*.h
%_includedir/%oname/Bullet3Collision
%_includedir/%oname/Bullet3Common
%_includedir/%oname/Bullet3Dynamics
%_includedir/%oname/Bullet3Geometry
%_includedir/%oname/Bullet3OpenCL
%_includedir/%oname/BulletCollision
%_includedir/%oname/BulletDynamics
%_includedir/%oname/BulletInverseDynamics
%_includedir/%oname/BulletSoftBody
%_includedir/%oname/InverseDynamics
%_includedir/%oname/LinearMath
%_libdir/libBullet3Collision.so
%_libdir/libBullet3Common.so
%_libdir/libBullet3Dynamics.so
%_libdir/libBullet3Geometry.so
%_libdir/libBullet3OpenCL_clew.so
%_libdir/libBulletCollision.so
%_libdir/libBulletDynamics.so
%_libdir/libBulletInverseDynamics.so
%_libdir/libBulletSoftBody.so
%_libdir/libLinearMath.so
%_pkgconfigdir/bullet.pc
%_libdir/cmake/%oname

%files -n lib%name-extras
%_libdir/libConvexDecomposition.so.*
%_libdir/libGIMPACTUtils.so.*
%_libdir/libHACD.so.*
%_libdir/libBulletFileLoader.so.*
%_libdir/libBullet2FileLoader.so.*
%_libdir/libBulletInverseDynamicsUtils.so.*
%_libdir/libBulletWorldImporter.so.*
%_libdir/libBulletXmlWorldImporter.so.*

%files -n lib%name-extras-devel
%_includedir/%oname/ConvexDecomposition
%_includedir/%oname/GIMPACTUtils
%_includedir/%oname/HACD
%_includedir/%oname/BulletFileLoader
%_includedir/%oname/Bullet2FileLoader
%_includedir/%oname/BulletWorldImporter
%_includedir/%oname/BulletXmlWorldImporter
%_libdir/libConvexDecomposition.so
%_libdir/libGIMPACTUtils.so
%_libdir/libHACD.so
%_libdir/libBulletFileLoader.so
%_libdir/libBullet2FileLoader.so
%_libdir/libBulletInverseDynamicsUtils.so
%_libdir/libBulletWorldImporter.so
%_libdir/libBulletXmlWorldImporter.so

%changelog
* Fri Sep 15 2023 Mikhail Tergoev <fidel@altlinux.org> 3.25-alt2
- revert to git

* Thu Aug 10 2023 Mikhail Tergoev <fidel@altlinux.org> 3.25-alt1
- move to tarball
- new version (3.25) with rpmgs script
- added patch from mageia for fix build stuntrally (ALT bug: 47193)
- added patch for use system libs
- update BR
- added extra binaries

* Tue Apr 05 2022 Artyom Bystrov <arbars@altlinux.org> 2.89-alt1
- Update to version 2.89

* Wed Oct 30 2019 Michael Shigorin <mike@altlinux.org> 2.88-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24

* Tue Oct 08 2019 Konstantin Rybakov <kastet@altlinux.org> 2.88-alt1
- Updated to upstream version 2.88

* Thu Sep 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.83-alt1.alpha
- Initial build for Sisyphus

