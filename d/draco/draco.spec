Name:    draco
Version: 1.5.6
Release: alt1

Summary: Draco is a library for compressing and decompressing 3D geometric meshes and point clouds. It is intended to improve the storage and transmission of 3D graphics
License: Apache-2.0
Group:   Other
Url:     https://github.com/google/draco

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++

%description
Draco is a library for compressing and decompressing 3D geometric meshes and
point clouds. It is intended to improve the storage and transmission of 3D
graphics.

Draco was designed and built for compression efficiency and speed. The code
supports compressing points, connectivity information, texture coordinates,
color information, normals, and any other generic attributes associated with
geometry. With Draco, applications using 3D graphics can be significantly
smaller without compromising visual fidelity. For users, this means apps can
now be downloaded faster, 3D graphics in the browser can load quicker, and VR
and AR scenes can now be transmitted with a fraction of the bandwidth and
rendered quickly.

Draco is released as C++ source code that can be used to compress 3D graphics
as well as C++ and Javascript decoders for the encoded data.

%package -n lib%name
Summary: Library for draco
Group: System/Libraries

%description -n lib%name
%summary.

%package -n lib%name-devel
Summary: Development files for draco
Requires: lib%name = %EVR
Group: Development/C++
 
%description -n lib%name-devel
%summary.

%prep
%setup

%build
%cmake -GNinja -Wno-dev \
       -DBUILD_SHARED_LIBS=ON \
       -DDRACO_TESTS=OFF

%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
# Remove static library
rm -f %buildroot%_libdir/*.a

%files
%doc AUTHORS README.md
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/*.so
%_libdir/lib%name.so
%_datadir/cmake/%name/
%_libdir/pkgconfig/%name.pc

%changelog
* Mon Oct 30 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.6-alt1
- Initial build for Sisyphus.
