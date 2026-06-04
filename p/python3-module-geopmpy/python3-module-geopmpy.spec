%global prj_name geopmpy

Name: python3-module-%prj_name
Version: 3.2.2.0.300.aaf9
Release: alt1

Summary: Python 3 bindings for GEOPM runtime library
Group: System/Configuration/Other
License: BSD-3-Clause

URL: https://geopm.github.io
VCS: https://github.com/geopm/geopm.git
Source0: %name-%version.tar
ExclusiveArch: x86_64

BuildRequires: gcc
BuildRequires: rpm-build-python3
BuildRequires: python3-module-cffi
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-geopmdpy >= 3.2.1
BuildRequires: python3-module-cycler
BuildRequires: python3-module-pandas
BuildRequires: python3-module-natsort
BuildRequires: python3-module-tables
BuildRequires: python3-module-yaml
BuildRequires: libgeopm-devel >= 3.2.1
BuildRequires: libgeopmd-devel >= 3.2.1
# for tests
BuildRequires: libblosc2-devel
BuildRequires: python3-module-tables-tests
BuildRequires: /proc
Requires: geopmd

%description
Python 3 interface to GEOPM (Global Extensible Open Power Manager) runtime
library. Provides high-level Python API for power and energy management,
performance monitoring, and hardware optimization on heterogeneous systems.
Includes tools for data analysis and visualization of power management metrics.

%prep
%setup -q -n %name-%version

pushd %prj_name
# Hardcode a PEP 440 compliant version for setuptools_scm.
# The RPM Version (3.2.2.0.300.aaf9) is not a valid Python version,
# causing setuptools_scm to fail with InvalidVersion during build.
# Remove this line when upgrading to the next upstream release where
# %version will be PEP 440 compliant again.
echo 3.2.2 > %prj_name/VERSION
popd

%build
pushd %prj_name
%pyproject_build
popd

%install
pushd %prj_name
%pyproject_install
popd

%check
pushd %prj_name
python3 -m unittest discover -s test -p 'Test*.py' -v
popd

%files
%doc README.md LICENSE-BSD-3-Clause
%python3_sitelibdir/_libgeopm_py_cffi.abi3.so
%python3_sitelibdir/%prj_name
%python3_sitelibdir/%prj_name-*.dist-info/
%_bindir/geopmlaunch

%changelog
* Thu Jun 04 2026 Danila Skachedubov <skachedubov@altlinux.org> 3.2.2.0.300.aaf9-alt1
- interim build with all upstream fixes from dev branch after v3.2.2
- fixed infinite loop in HDF5 cache generation
- fixed TestIO.py and other test corrections from upstream

* Wed Mar 04 2026 Danila Skachedubov <skachedubov@altlinux.org> 3.2.2-alt2
- added blosc2 for test

* Fri Jan 16 2026 Danila Skachedubov <skachedubov@altlinux.org> 3.2.2-alt1
- first build for ALT
