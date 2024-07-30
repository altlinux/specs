%define pypi_name flexcache

%def_with check

Name:    python3-module-%pypi_name
Version: 0.3
Release: alt1

Summary: An robust and extensible package to cache on disk the result of expensive calculations

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/flexcache
VCS:     https://github.com/hgrecco/flexcache

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Jul 30 2024 Grigory Ustinov <grenka@altlinux.org> 0.3-alt1
- Initial build for Sisyphus.
