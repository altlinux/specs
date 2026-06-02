%define _unpackaged_files_terminate_build 1

%def_with check

Name: pybind11
Version: 3.0.4
Release: alt1

Summary: Seamless operability between C++11 and Python
License: BSD-3-Clause
Group: Development/Other

Url: https://github.com/pybind/pybind11
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: boost-devel
BuildRequires: catch-devel
BuildRequires: ccmake
BuildRequires: cmake
BuildRequires: eigen3-devel
BuildRequires: gcc-c++
BuildRequires: python3-module-scikit-build-core

# These are only needed for the checks
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-scipy
BuildRequires: eigen3-devel
BuildRequires: ctest
%endif

%package devel
Summary: %summary
Group: Development/Other
# For dir ownership
Requires: cmake
# headers include <Python.h> via conduit/wrap_include_python_h.h
Requires: python3-devel

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
# tests/exo_planet_c_api.cpp needs -fno-exceptions
sed -i 's/GNU|Intel/LCC|&/' tests/CMakeLists.txt

# Dropped dependency on distutils (for python3.12)
sed -i 's/distutils.ccompiler/setuptools._distutils.ccompiler/' pybind11/setup_helpers.py
sed -i 's/distutils.errors/setuptools._distutils.errors/' pybind11/setup_helpers.py

%build
%pyproject_build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DPYBIND11_TEST=ON \
	-DPYTHON_EXECUTABLE=%_bindir/python3
%cmake_build

%install
%pyproject_install
%cmake_install

# remove duplicated header files from sitelibs but link to common dirs as some
# packages expect them to be in the sitelib where pybind11.get_include() reports them.
rm -rf %buildroot%python3_sitelibdir/pybind11/include/pybind11
ln -s %_includedir/pybind11 %buildroot%python3_sitelibdir/pybind11/include/pybind11
# same for cmake files: pybind11.get_cmake_dir()
rm -r %buildroot%python3_sitelibdir/pybind11/share/cmake/pybind11
ln -s %_datadir/cmake/pybind11 %buildroot%python3_sitelibdir/pybind11/share/cmake/pybind11
# same for pkgconfig
rm %buildroot%python3_sitelibdir/pybind11/share/pkgconfig/pybind11.pc
ln -s %_datadir/pkgconfig/pybind11.pc %buildroot%python3_sitelibdir/pybind11/share/pkgconfig/pybind11.pc

%check
%ifarch %e2k
export SKIP_E2K=1
%endif
export PYTHONPATH=$PWD/noarch-alt-linux/tests
pushd noarch-alt-linux/tests
py.test-3
popd

%files devel
%doc README.rst LICENSE docs/*
%_includedir/%name
%_datadir/cmake/%name
%_bindir/%name-config
%_datadir/pkgconfig/%name.pc

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version.dist-info

%changelog
* Tue Jun 02 2026 Anton Vyatkin <toni@altlinux.org> 3.0.4-alt1
- New version 3.0.4 (Closes: #46642).

* Thu May 14 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt4
- NMU: devel: add missing Requires: python3-devel (closes: 59135)

* Thu May 07 2026 Michael Shigorin <mike@altlinux.org> 3.0.2-alt3
- spec: -fno-exceptions for lcc as well (ilyakurdyukov@)

* Sat Mar 28 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt2
- fix shared_ptr downcast with virtual inheritance (GCC 14, upstream PR 6014)

* Thu Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1.1
- NMU: fix BuildRequires: eigen3 -> eigen3-devel

* Tue Feb 17 2026 Anton Vyatkin <toni@altlinux.org> 3.0.2-alt1
- New version 3.0.2.

* Tue Oct 28 2025 Anton Vyatkin <toni@altlinux.org> 3.0.1-alt1
- New version 3.0.1.

* Sat Sep 14 2024 Anton Vyatkin <toni@altlinux.org> 2.13.6-alt1
- New version 2.13.6.

* Fri Aug 23 2024 Anton Vyatkin <toni@altlinux.org> 2.13.5-alt1
- New version 2.13.5.

* Thu Aug 15 2024 Anton Vyatkin <toni@altlinux.org> 2.13.4-alt1
- New version 2.13.4.

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
