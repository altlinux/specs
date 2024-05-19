%define oname typeguard

%def_without check

Name: python3-module-typeguard
Version: 4.2.1
Release: alt1
Summary: Run-time type checker for Python
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/typeguard
VCS: https://github.com/agronholm/typeguard

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-mypy
%endif

%description
This library provides run-time type checking for functions
defined with PEP 484 argument (and return) type annotations.

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
%doc LICENSE README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 4.2.1-alt1
- Automatically updated to 4.2.1.

* Tue Jan 18 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.3-alt1
- Initial build for ALT.
