%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    devel
%def_enable    examples

Name:          nanoflann
Version:       1.10.1.4.1
Release:       alt0.1
Summary:       Library for Nearest Neighbor (NN) search with KD-trees
License:       BSD-2-Clause
Group:         Sciences/Mathematics
Url:           https://github.com/jlblancoc/nanoflann
Vcs:           https://github.com/jlblancoc/nanoflann.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: eigen3

%description
nanoflann: a C++11 header-only library for Nearest Neighbor (NN) search with
KD-trees of datasets with different topologies: R2, R3 (point clouds), SO(2) and
SO(3) (2D and 3D rotation groups). No support for approximate NN is provided.
nanoflann does not require compiling or installing. You just need to #include
<nanoflann.hpp> in your code.

This library is a fork of the flann library (git) by Marius Muja and David G.
Lowe, and born as a child project of MRPT. Following the original license terms,
nanoflann is distributed under the BSD license. Please, for bugs use the issues
button or fork and open a pull request.


%if_enabled    examples
%package       examples
Version:       1.10.1.4.1
Release:       alt0.1
Summary:       Library for Nearest Neighbor (NN) search with KD-trees examples
Group:         Sciences/Mathematics

Requires:      nanoflann = %EVR

%description   examples
Library for Nearest Neighbor (NN) search with KD-trees examples.

nanoflann: a C++11 header-only library for Nearest Neighbor (NN) search with
KD-trees of datasets with different topologies: R2, R3 (point clouds), SO(2) and
SO(3) (2D and 3D rotation groups). No support for approximate NN is provided.
nanoflann does not require compiling or installing. You just need to #include
<nanoflann.hpp> in your code.

This library is a fork of the flann library (git) by Marius Muja and David G.
Lowe, and born as a child project of MRPT. Following the original license terms,
nanoflann is distributed under the BSD license. Please, for bugs use the issues
button or fork and open a pull request.
%endif


%if_enabled    devel
%package       devel
Version:       1.10.1.4.1
Release:       alt0.1
Summary:       Library for Nearest Neighbor (NN) search with KD-trees development files
Group:         Development/Other

Requires:      nanoflann = %EVR

%description   devel
Library for Nearest Neighbor (NN) search with KD-trees development files.

nanoflann: a C++11 header-only library for Nearest Neighbor (NN) search with
KD-trees of datasets with different topologies: R2, R3 (point clouds), SO(2) and
SO(3) (2D and 3D rotation groups). No support for approximate NN is provided.
nanoflann does not require compiling or installing. You just need to #include
<nanoflann.hpp> in your code.

This library is a fork of the flann library (git) by Marius Muja and David G.
Lowe, and born as a child project of MRPT. Following the original license terms,
nanoflann is distributed under the BSD license. Please, for bugs use the issues
button or fork and open a pull request.
%endif


%prep
%setup

%build
%cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%doc README*

%files         examples
%_libdir/%name/examples/

%if_enabled    devel
%files         devel
%_includedir/%{name}.hpp
%_pkgconfigdir/%{name}.pc
%_datadir/cmake/%{name}/*.cmake
%endif

%changelog
* Wed Jul 08 2026 Pavel Skrylev <majioa@altlinux.org> 1.10.1.4.1-alt0.1
- ^ 1.3.1 -> 1.10.1p4.1 (closes ALT #59761)

* Mon Aug 17 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- initial build for Sisyphus
