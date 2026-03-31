%define _unpackaged_files_terminate_build 1
%define pypi_name pip-requirements-parser

Name: python3-module-%pypi_name
Version: 32.0.1
Release: alt1

Summary: Library for parsing pip requirements files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pip-requirements-parser/
VCS: https://github.com/aboutcode-org/pip-requirements-parser

BuildArch: noarch
Source: %name-%version.tar
Patch: 0001-Set-a-proper-fallback-version-in-setuptools_scm-for-.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/packaging_legacy_version.py
%python3_sitelibdir/__pycache__/packaging_legacy_version*
%python3_sitelibdir/pip_requirements_parser.py
%python3_sitelibdir/__pycache__/pip_requirements_parse*

%changelog
* Fri Mar 27 2026 Denis Rastyogin <gerben@altlinux.org> 32.0.1-alt1
- Initial build for ALT Sisyphus.
