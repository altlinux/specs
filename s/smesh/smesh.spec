%def_without netgen

Name:     smesh
Version:  8.3.0.4
Release:  alt2

Summary:  OpenCascade based MESH framework
License:  LGPL-2.1
Group:    System/Libraries
Url:      https://github.com/LaughlinResearch/SMESH

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch1:   smesh-install.patch
Patch2:   smesh-alt-return-type.patch
Patch3:   smesh-alt-link-with-dl.patch
Patch4:   smesh-alt-cmake-pathes.patch
Patch5:   smesh-alt-vtk-compat.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-polygon-devel
BuildRequires: opencascade-devel
BuildRequires: libvtk-devel
%if_with netgen
BuildRequires: libnetgen-devel netgen
%endif
BuildRequires: fontconfig-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: libnetcdf-devel
BuildRequires: libxml2-devel
BuildRequires: doxygen graphviz

%description
A complete OpenCascade based MESH framework. Note this is not the
original SALOME SMESH project but an effort to create a standalone mesh
framework based on the existing one from SALOME project. This is a fork
of the salomesmesh project available at:
http://sourceforge.net/projects/salomesmesh/ (Original project by Fotis
Soutis). This fork is intended for a use in the pythonocc project.

%package -n libsmesh
Summary: An extension to oce, provides advanced meshing features
Group:    System/Libraries

%description -n libsmesh
A complete OpenCascade based MESH framework. Note this is not the
original SALOME SMESH project but an effort to create a standalone mesh
framework based on the existing one from SALOME project. This is a fork
of the salomesmesh project available at:
http://sourceforge.net/projects/salomesmesh/ (Original project by Fotis
Soutis). This fork is intended for a use in the pythonocc project.

%package -n libsmesh-devel
Summary: Development files for libsmesh
Group: Development/C++
Requires: libsmesh = %EVR

%description -n libsmesh-devel
Development files and headers for libsmesh.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%cmake -GNinja \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DSMESH_TESTING=ON \
       -DENABLE_NETGEN=%{?_with_netgen:ON}%{!?_with_netgen:OFF}
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%files -n libsmesh
%doc README.md
%_libdir/*.so.*

%files -n libsmesh-devel
%_libdir/*.so
%_includedir/*
%_libdir/cmake/SMESHConfig.cmake

%changelog
* Wed May 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 8.3.0.4-alt2
- Rebuilt with VTK-9.0.1.

* Fri Jun 26 2020 Andrey Cherepanov <cas@altlinux.org> 8.3.0.4-alt1
- New version.

* Sat May 09 2020 Andrey Cherepanov <cas@altlinux.org> 8.3.0.3-alt1
- New version.
- New upstream https://github.com/LaughlinResearch/SMESH.
- Fix License tag according to SPDX.
- Build with opencascade instead of obsoleted OCE.

* Thu Apr 26 2018 Andrey Cherepanov <cas@altlinux.org> 6.7.6-alt1
- Initial build for Sisyphus
