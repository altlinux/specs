%define _unpackaged_files_terminate_build 1
%define pypi_name xdoctest
%define module_name xdoctest

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.2
Release: alt1
Summary: Doctest runner with AST parsing and pytest plugin integration
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/xdoctest/
Vcs: https://github.com/Erotemic/xdoctest.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Xdoctest executes doctests embedded in Google-style or classic docstrings,
replacing Python's builtin doctest with an AST-based parser.
It integrates with pytest, offers a concise CLI for discovering and
running doctests across your code base, and provides colorful, configurable
reports.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%_bindir/%module_name
%python3_sitelibdir_noarch/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jun 26 2026 Aleksandr A. Voyt <sobue@altlinux.org> 1.3.2-alt1
- 1.3.0 -> 1.3.2

* Thu Nov 06 2025 Aleksandr A. Voyt <sobue@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0

* Thu Apr 17 2025 Aleksandr A. Voyt <sobue@altlinux.org> 1.2.0-alt1
- Initial build
