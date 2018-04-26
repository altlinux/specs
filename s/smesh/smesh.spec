Name:     smesh
Version:  6.7.6
Release:  alt1

Summary:  An extension to oce, provides advanced meshing features
License:  LGPLv2
Group:    System/Libraries
Url:      https://github.com/tpaviot/smesh

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: OCE-devel
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

%package -n libsmesh-doc
Summary: Development documentation for libsmesh
Group: Development/Documentation
Requires: libsmesh = %EVR
BuildArch: noarch

%description -n libsmesh-doc
Development documentation for libsmesh.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DSMESH_TESTING=ON \
%cmake_build all doc

%install
%cmakeinstall_std

%files -n libsmesh
%doc README.md
%_libdir/*.so.*

%files -n libsmesh-devel
%_libdir/*.so
%_includedir/*

%files -n libsmesh-doc
%_datadir/doc/smesh/html

%changelog
* Thu Apr 26 2018 Andrey Cherepanov <cas@altlinux.org> 6.7.6-alt1
- Initial build for Sisyphus
