%define _unpackaged_files_terminate_build 1
#based on fedora spec
Name: pybind11
Version: 2.13.3
Release: alt1

Summary: Seamless operability between C++11 and Python
License: BSD-3-Clause
Group: Development/Other

Url: https://github.com/pybind/pybind11
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: boost-devel
BuildRequires: catch-devel
BuildRequires: ccmake
BuildRequires: cmake
BuildRequires: eigen3
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: python3-module-pytest
BuildRequires: python3-module-setuptools

# These are only needed for the checks
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-scipy
BuildRequires: eigen3-devel
BuildRequires: ctest

%package devel
Summary: %summary
Group: Development/Other
# For dir ownership
Requires: cmake

%package -n python3-module-%name
Summary: %summary
Group: Development/Python3
Requires: %name-devel = %EVR

%define base_description \
pybind11 is a lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create Python bindings of existing C++ code. Tutorial and reference documentation is provided at http://pybind11.readthedocs.org/en/master

%description
%base_description

%description devel
%base_description

This package contains the development headers for pybind11.

%description -n python3-module-%name
%base_description

This package contains the Python 3 files.

%prep
%setup

# Dropped dependency on distutils (for python3.12)
sed -i 's/distutils.ccompiler/setuptools._distutils.ccompiler/' pybind11/setup_helpers.py
sed -i 's/distutils.errors/setuptools._distutils.errors/' pybind11/setup_helpers.py

%build
%define _cmake__builddir python3/BUILD
mkdir -p python3
%cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=%_bindir/python3
%cmake_build

%python3_build_debug

%install
%define _cmake__builddir python3/BUILD
%cmake_install
# Force install to arch-ful directories instead.
PYBIND11_USE_CMAKE=true %python3_install "--install-purelib" "%python3_sitelibdir"

rm -rf %buildroot%_includedir/python*

mkdir -p %buildroot%_pkgconfigdir
mv %buildroot%_datadir/pkgconfig/* %buildroot%_pkgconfigdir/

%check
%ifarch %e2k
export SKIP_E2K=1
%endif
%define _cmake__builddir python3/BUILD/tests
%cmake_build --target check

%files devel
%doc README.rst LICENSE docs/*
%_includedir/%name
%_datadir/cmake/%name
%_bindir/%name-config
%_pkgconfigdir/*

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version-*.egg-info

%changelog
* Wed Aug 14 2024 Anton Vyatkin <toni@altlinux.org> 2.13.3-alt1
- New version 2.13.3.

* Thu Jun 27 2024 Anton Vyatkin <toni@altlinux.org> 2.13.1-alt1
- New version 2.13.1.

* Sun Oct 29 2023 Anton Vyatkin <toni@altlinux.org> 2.11.1-alt3
- NMU: fixed replacement of distutils.

* Sat Oct 28 2023 Anton Vyatkin <toni@altlinux.org> 2.11.1-alt2
- NMU: Dropped dependency on distutils.

* Wed Aug 23 2023 Ivan A. Melnikov <iv@altlinux.org> 2.11.1-alt1
- New version

* Tue Nov 01 2022 Michael Shigorin <mike@altlinux.org> 2.9.2-alt2
- E2K: drop the kludge

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 2.9.2-alt1
- New version

* Fri Oct 29 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.8.1-alt1
- New version

* Wed Aug 18 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.7.1-alt1
- New version

* Tue Jul 27 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.7.0-alt1
- New version

* Wed Jun 23 2021 Michael Shigorin <mike@altlinux.org> 2.6.2-alt2
- E2K: drop c++ hacks, update ones for tests

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 2.6.2-alt1.1
- NMU: spec: adapted to new cmake macros.

* Mon Feb 01 2021 Nikolai Kostrigin <nickel@altlinux.org> 2.6.2-alt1
- New version

* Thu Dec 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.6.1-alt1
- New version
- Spec: update files section for devel subpackage

* Mon Apr 06 2020 Nikolai Kostrigin <nickel@altlinux.org> 2.5.0-alt1
- New version
- Fix license

* Thu Apr 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.4.3-alt2
- Build requires fixed.

* Mon Oct 28 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.4.3-alt1
- New version
- Spec: quit building Python2 module package

* Thu Oct 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.2-alt2
- Added hack for build on e2k.
- Introduced strong inter-package dependencies.

* Tue Oct 01 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.4.2-alt1
- New version

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 2.3.0-alt2
- Fixed testing against Pytest 5.

* Thu Aug 08 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.3.0-alt1
- New version

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 2.2.4-alt3
- Added missing dep on `numpy.testing`.

* Tue Jun 04 2019 Stanislav Levin <slev@altlinux.org> 2.2.4-alt2
- Fixed Pytest4.x compatibility errors.

* Mon Oct 08 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.2.4-alt1
- New version
- Remove ubt

* Fri Jun 29 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.2.3-alt2
- Fix build: add python(3)-module-setuptools build requirement

* Fri Jun 15 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.2.3-alt1
- New version
- Remove patches due to upstream application

* Sat Apr 28 2018 Nikolai Kostrigin <nickel@altlinux.org> 2.2.2-alt1
- Initial build
