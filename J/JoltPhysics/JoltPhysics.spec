%define _unpackaged_files_terminate_build 1

%define abiver 5.6
%define libname libJolt%{abiver}

Name:    JoltPhysics
Version: 5.6.0
Release: alt1

Summary: A multi core friendly rigid body physics and collision detection library
License: MIT
Group:   System/Libraries
URL:     https://github.com/jrouwe/JoltPhysics

Source: %name-%version.tar
Patch:  JoltPhysics-soname.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

ExclusiveArch: x86_64 aarch64

%description
A multi core friendly rigid body physics and collision detection library.
Suitable for games and VR applications.

%package -n %libname
Summary: Shared library for %name
Group:   System/Libraries

%description -n %libname
A multi core friendly rigid body physics and collision detection library.
Suitable for games and VR applications.

%package -n libJolt-devel
Summary: Development files for %name
Group:   Development/C++
Requires: %libname = %EVR

%description -n libJolt-devel
Development files for %name: headers, CMake config and the unversioned
library link used for building dependent applications.

%prep
%setup
%patch -p1

%build
%cmake -S Build \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_SHARED_LIBS=ON \
	-DOBJECT_LAYER_BITS=32 \
	-DTARGET_HELLO_WORLD=OFF \
	-DTARGET_PERFORMANCE_TEST=OFF \
	-DTARGET_SAMPLES=OFF \
	-DTARGET_UNIT_TESTS=OFF \
	-DTARGET_VIEWER=OFF
%cmake_build

%install
%cmake_install
# Public Jolt/Physics/Hair/HairSettings.h includes Jolt/Shaders/HairStructs.h,
# but upstream installs only HairWrapper.h; add the missing shader headers
install -Dm644 Jolt/Shaders/HairStructs.h %buildroot%_includedir/Jolt/Shaders/HairStructs.h
install -Dm644 Jolt/Shaders/ShaderCore.h %buildroot%_includedir/Jolt/Shaders/ShaderCore.h

%files -n %{libname}
%doc LICENSE README.md
%_libdir/libJolt.so.%{abiver}*

%files -n libJolt-devel
%_includedir/Jolt
%_libdir/cmake/Jolt
%_libdir/libJolt.so

%changelog
* Wed Nov 11 2026 Sergey Palcheh <minergenon@altlinux.org> 5.6.0-alt1
- Initial build for Sisyphus
