%define pypi_name pytest-doctestplus

%def_with check

Name:    python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Pytest plugin providing advanced doctest features
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/pytest-doctestplus
VCS:     https://github.com/scientific-python/pytest-doctestplus

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-pytest-remotedata
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
This package contains a plugin for the pytest framework that provides
advanced doctest support and enables the testing of various text files, such
as reStructuredText (".rst"), markdown (".md"), and TeX (".tex").

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests --doctest-plus --doctest-rst -k "not test_remote_data_url"

%files
%doc *.rst
%python3_sitelibdir/pytest_doctestplus
%python3_sitelibdir/%{pyproject_distinfo pytest_doctestplus}

%changelog
* Tue Nov 26 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.
- Built with check.

* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus.
