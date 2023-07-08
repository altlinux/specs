Name:          nanoflann
Version:       1.3.1
Release:       alt1
Summary:       Library for Nearest Neighbor (NN) search with KD-trees
License:       BSD-2-Clause
Group:         Sciences/Mathematics
Url:           https://github.com/jlblancoc/nanoflann
Vcs:           https://github.com/jlblancoc/nanoflann.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Source1:       FindNanoFlann.cmake
Patch:         patch.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: eigen3

%description
nanoflann: a C++11 header-only library for Nearest Neighbor (NN) search with
KD-trees of datasets with different topologies: R2, R3 (point clouds), SO(2)
and SO(3) (2D and 3D rotation groups). No support for approximate NN is
provided. nanoflann does not require compiling or installing. You just need to
#include <nanoflann.hpp> in your code.

This library is a fork of the flann library (git) by Marius Muja and
David G. Lowe, and born as a child project of MRPT. Following the original
license terms, nanoflann is distributed under the BSD license. Please, for bugs
use the issues button or fork and open a pull request.


%package       devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      %{name} = %EVR

%description   devel
%summary.

%package       examples
Group:         Sciences/Mathematics
Summary:       Executble examples for %name

Requires:      %{name} = %EVR

%description   examples
%summary.



%prep
%setup
%patch

%build
%cmake -DINSTALL_EXAMPLES_DIR:STRING=%_libdir/%name/examples/
%cmake_build

%install
%cmakeinstall_std
install -Dm644 %SOURCE1 %buildroot%_datadir/cmake/Modules/FindNanoFlann.cmake

%files
%doc README*

%files         examples
%_libdir/%name/examples/

%files         devel
%_includedir/%{name}.hpp
%_libdir/cmake/%{name}/
%_pkgconfigdir/%{name}.pc
%_datadir/cmake/Modules/*.cmake
   
%changelog
* Mon Aug 17 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- initial build for Sisyphus
