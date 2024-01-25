Name:          meshsdfilter
Version:       0.0.1
Release:       alt0.gitb814112
Summary:       Static/Dynamic Filter for Mesh Geometry
License:       BSD-3-Clause
Group:         Sciences/Mathematics
Url:           https://github.com/bldeng/MeshSDFilter
Vcs:           https://github.com/bldeng/MeshSDFilter.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Source1:       FindMeshSDFilter.cmake
Patch:         patch.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: eigen3
BuildRequires: openmesh-devel

%description
This code implements the mesh normal filtering algorithm from
the following paper:

- Juyong Zhang, Bailin Deng, Yang Hong, Yue Peng, Wenjie Qin, Ligang Liu.
  Static/Dynamic Filtering for Mesh Geometry. arXiv:1712.03574.


%package       devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      %{name} = %EVR
Requires:      cmake
Requires:      gcc-c++
Requires:      eigen3
Requires:      openmesh-devel

%description   devel
This code implements the mesh normal filtering algorithm from
the following paper:

- Juyong Zhang, Bailin Deng, Yang Hong, Yue Peng, Wenjie Qin, Ligang Liu.
  Static/Dynamic Filtering for Mesh Geometry. arXiv:1712.03574.


%prep
%setup
%autopatch

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
install -Dm644 %SOURCE1 %buildroot%_datadir/cmake/Modules/FindMeshSDFilter.cmake

%files
%doc README*
%_bindir/*

%files         devel
%_includedir/%{name}/
%_datadir/cmake/Modules/

%changelog
* Thu Jan 25 2024 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt0.gitb814112
- initial build for Sisyphus
