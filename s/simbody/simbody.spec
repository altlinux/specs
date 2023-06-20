Name:    simbody
Version: 3.7
Release: alt1

Summary: High-performance C++ multibody dynamics/physics library for simulating articulated biomechanical and mechanical systems
License: Apache-2.0
Group:   Sciences/Mathematics
Url:     https://github.com/simbody/simbody

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libfreeglut-devel
BuildRequires: liblapack-devel
BuildRequires: libGL-devel

%description
Simbody is a high-performance, open-source toolkit for science- and
engineering-quality simulation of articulated mechanisms, including
biomechanical structures such as human and animal skeletons, mechanical systems
like robots, vehicles, and machines, and anything else that can be described as
a set of rigid bodies interconnected by joints, influenced by forces and
motions, and restricted by constraints. Simbody includes a multibody dynamics
library for modeling motion in generalized/internal coordinates in O(n) time.
This is sometimes called a Featherstone-style physics engine.

%package -n lib%name
Summary: Library of %name
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%{name}-devel
%summary

%package examples
Summary: Examples of %name
Group: Development/Documentation

%description examples
%summary

%package docs
Summary: Documentation for %name
Group: Development/Documentation

%description docs
%summary

%prep
%setup

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files -n lib%name
%doc README.md
%_libdir/*.so.*

%files -n lib%{name}-devel
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/%name

%files examples
%_libdir/%name/examples
%_defaultdocdir/%name/examples

%files docs
%_defaultdocdir/%name/*.*

%changelog
* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 3.7-alt1
- Initial build for Sisyphus
