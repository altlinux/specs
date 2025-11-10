%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-archon
%define module_name pytest_archon

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.7
Release: alt1
Summary: Rule your architecture like a real developer
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-archon
Vcs: https://github.com/jwbargsten/pytest-archon.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

%description
Pytest plugin pytest-archon lets you define and enforce
architectural dependency rules in Python code.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.md
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 06 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.0.7-alt1
- 0.0.6 -> 0.0.7

* Thu Apr 17 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.0.6-alt1
- Initial build
