%define _unpackaged_files_terminate_build 1
%def_enable check

%define pypi_name bashlex

Name: python3-module-%pypi_name
Version: 0.18
Release: alt1

Summary: Python parser for bash
License: GPL-3.0-or-later
Group: Development/Python3
URL: https://pypi.org/project/bashlex
VCS: https://github.com/idank/bashlex

Source: %name-%version-%release.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_enabled check
BuildRequires: python3(pytest)
%endif

%description
bashlex is a Python port of the parser used internally by GNU bash.

For the most part it's transliterated from C, the major differences are:
1. it does not execute anything
2. it is reentrant
3. it generates a complete AST

%prep
%setup -n %name-%version-%release

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir_noarch/bashlex
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Nov 20 2026 Arseny Maslennikov <arseny@altlinux.org> 0.18-alt1
- Initial build for ALT Sisyphus.
