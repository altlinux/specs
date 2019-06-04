#based on fedora spec
Name: pybind11
Version: 2.2.4
Release: alt2

Summary: Seamless operability between C++11 and Python
License: BSD-style
Group: Development/Other
Url: https://github.com/pybind/pybind11

Source0: %name-%version.tar
Patch0: pybind11-2.2.4-compatibility-with-pytest-4.0-fix-1670.patch

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu May 10 2018
BuildRequires: boost-devel-headers
BuildRequires: catch-devel
BuildRequires: ccmake
BuildRequires: eigen3
BuildRequires: gcc-c++
BuildRequires: python-module-scipy
BuildRequires: python3-dev
BuildRequires: python3-module-pytest
BuildRequires: python3-module-setuptools
BuildRequires: python-module-setuptools

# These are only needed for the checks
BuildRequires: python-module-pytest
BuildRequires: python-module-numpy
BuildRequires: python3-module-numpy
BuildRequires: python3-module-scipy
BuildRequires: eigen3-devel
BuildRequires: ctest

%package devel
Summary: %summary
Group: Development/Other
# For dir ownership
Requires: cmake

%package -n python-module-%name
Summary: %summary
Group: Development/Python
Requires: %name-devel = %version-%release

%package -n python3-module-%name
Summary: %summary
Group: Development/Python3
Requires: %name-devel = %version-%release

%define base_description \
pybind11 is a lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create Python bindings of existing C++ code. Tutorial and reference documentation is provided at http://pybind11.readthedocs.org/en/master

%description
%base_description

%description devel
%base_description

This package contains the development headers for pybind11.

%description -n python-module-%name
%base_description

This package contains the Python 2 files.

%description -n python3-module-%name
%base_description

This package contains the Python 3 files.

%prep
%setup
%patch0 -p1

%build
for py in python python3; do
    mkdir $py
    cd $py
    %cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=%_bindir/$py ../..
    %cmake_build
    cd ..
done
%python_build_debug
%python3_build_debug

%install
%makeinstall_std -C python/BUILD
# Force install to arch-ful directories instead.
PYBIND11_USE_CMAKE=true %python_install "--install-purelib" "%python_sitelibdir"
PYBIND11_USE_CMAKE=true %python3_install "--install-purelib" "%python3_sitelibdir"

rm -rf %buildroot%_includedir/python*

%check
make -C python/BUILD/tests check -j$NPROCS
make -C python3/BUILD/tests check -j$NPROCS

%files devel
%doc README.md CONTRIBUTING.md LICENSE ISSUE_TEMPLATE.md docs/*
%_includedir/%name
%_datadir/cmake/%name

%files -n python-module-%name
%python_sitelibdir/%name
%python_sitelibdir/%name-%version-*.egg-info

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version-*.egg-info

%changelog
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
