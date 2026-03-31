%define _unpackaged_files_terminate_build 1
%define pypi_name pep8-naming

Name: python3-module-%pypi_name
Version: 0.15.1
Release: alt1

Summary: Check PEP-8 naming conventions, plugin for flake8
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pep8-naming/
VCS: https://github.com/PyCQA/pep8-naming

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/pep8ext_naming.py
%python3_sitelibdir/__pycache__/pep8ext_naming*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Mar 30 2026 Denis Rastyogin <gerben@altlinux.org> 0.15.1-alt1
- Initial build for ALT Sisyphus.
