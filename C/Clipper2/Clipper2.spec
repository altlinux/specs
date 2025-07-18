%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define soname 1

Name: Clipper2
Version: 1.5.4
Release: alt1
Summary: Open source freeware library for clipping and offsetting lines and polygons
License: BSL-1.0
Group: Graphics
Url: https://www.angusj.com/clipper2/
Vcs: https://github.com/AngusJohnson/Clipper2.git

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
The Clipper library performs line & polygon clipping - intersection,
union, difference & exclusive-or, and line & polygon offsetting. The
library is based on Vatti's clipping algorithm.

%package -n lib%name%{soname}
Summary: Open source freeware library for clipping and offsetting lines and polygons
Group: System/Libraries

%description -n lib%name%{soname}
The Clipper library performs line & polygon clipping - intersection,
union, difference & exclusive-or, and line & polygon offsetting. The
library is based on Vatti's clipping algorithm.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++

%description -n lib%name-devel
The Clipper library performs line & polygon clipping - intersection,
union, difference & exclusive-or, and line & polygon offsetting. The
library is based on Vatti's clipping algorithm.

This package contains development files of %name.

%prep
%setup

%build
pushd CPP
%cmake \
	-DCMAKE_STRIP:FILEPATH="/bin/true" \
	-DCLIPPER2_UTILS=OFF \
	-DCLIPPER2_EXAMPLES=OFF \
	-DCLIPPER2_TESTS=OFF \
	-DBUILD_SHARED_LIBS=ON
%cmake_build
popd

%install
pushd CPP
%cmake_install
popd

%files -n lib%name%{soname}
%doc README.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/clipper2
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/clipper2

%changelog
* Fri Jul 18 2025 L.A. Kostis <lakostis@altlinux.ru> 1.5.4-alt1
- Initial build for ALTLinux.
