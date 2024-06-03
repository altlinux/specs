%define pypi_name pytest-mypy

%def_without check

Name:    python3-module-%pypi_name
Version: 0.10.3
Release: alt1

Summary: Mypy static type checker plugin for Pytest

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pytest-mypy
VCS:     https://github.com/realpython/pytest-mypy

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-attrs
BuildRequires: python3-module-mypy
BuildRequires: python3-module-filelock
BuildRequires: python3-module-pexpect
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
%doc LICENSE *.rst *.md
%python3_sitelibdir/pytest_mypy.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/pytest_mypy-%version.dist-info

%changelog
* Mon Jun 03 2024 Grigory Ustinov <grenka@altlinux.org> 0.10.3-alt1
- Initial build for Sisyphus.
