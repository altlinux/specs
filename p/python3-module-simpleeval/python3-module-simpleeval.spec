%define pypi_name simpleeval

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.4
Release: alt1

Summary: Simple Safe Sandboxed Extensible Expression Evaluator for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/simpleeval
Vcs: https://github.com/danthedeckie/simpleeval

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v

%files
%doc README.*
%python3_sitelibdir/__pycache__/simpleeval*.pyc
%python3_sitelibdir/simpleeval.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 11 2026 Anton Vyatkin <toni@altlinux.org> 1.0.4-alt1
- New version 1.0.4.

* Tue Apr 29 2025 Anton Vyatkin <toni@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus.
