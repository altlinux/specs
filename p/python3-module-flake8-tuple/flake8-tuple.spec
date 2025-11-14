%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-tuple
%define mod_name flake8_tuple

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.1
Release: alt1

Summary: Check code for one-element tuple

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/flake8-tuple/
Vcs: https://github.com/ar4s/flake8_tuple

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-ddt
BuildRequires: python3-module-six
BuildRequires: python3-module-autopep8
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pre-commit
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.rst
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir_noarch/%mod_name.py
%python3_sitelibdir_noarch/%{pyproject_distinfo %mod_name}

%changelog
* Tue Sep 2 2025 Timofei Fedotov <sovtouch@altlinux.org> 0.4.1-alt1
- Initial build for ALT Sisyphus.
