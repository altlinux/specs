%define pypi_name astropy

%def_without check

Name:    python3-module-%pypi_name
Version: 7.1.1
Release: alt1

Summary: Astronomy and astrophysics core library

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/astropy
VCS:     https://github.com/astropy/astropy

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-extension-helpers
BuildRequires: python3-module-Cython
BuildRequires: libnumpy-py3-devel
BuildRequires: wcslib-devel
BuildRequires: libcfitsio-devel
BuildRequires: libexpat-devel

Source: %name-%version.tar

Patch: astropy-alt-remove-tests-dependency.patch

%description
%summary.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %pypi_name.

%prep
%setup
%patch -p1

%build
export CPATH="/usr/include/wcslib"
export ASTROPY_USE_SYSTEM_ALL=1
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export CPATH="/usr/include/wcslib"
export ASTROPY_USE_SYSTEM_ALL=1
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%_bindir/fits2bitmap
%_bindir/fitscheck
%_bindir/fitsdiff
%_bindir/fitsheader
%_bindir/fitsinfo
%_bindir/samp_hub
%_bindir/showtable
%_bindir/showtable-astropy
%_bindir/volint
%_bindir/wcslint
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%exclude %python3_sitelibdir/%pypi_name/tests
%exclude %python3_sitelibdir/%pypi_name/*/tests
%exclude %python3_sitelibdir/%pypi_name/*/*/tests
%exclude %python3_sitelibdir/%pypi_name/*/*/*/tests
%exclude %python3_sitelibdir/%pypi_name/*/*/*/*/tests

%files tests
%python3_sitelibdir/%pypi_name/tests
%python3_sitelibdir/%pypi_name/*/tests
%python3_sitelibdir/%pypi_name/*/*/tests
%python3_sitelibdir/%pypi_name/*/*/*/tests
%python3_sitelibdir/%pypi_name/*/*/*/*/tests

%changelog
* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 7.1.1-alt1
- Automatically updated to 7.1.1.

* Thu Jul 10 2025 Grigory Ustinov <grenka@altlinux.org> 7.1.0-alt1
- Automatically updated to 7.1.0.

* Sun Jul 06 2025 Grigory Ustinov <grenka@altlinux.org> 7.0.1-alt1
- Initial build for Sisyphus.
