%define pypi_name pytest_param_files
%define alt_name pytest-param-files

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1
Summary: Create pytest parametrize decorators from external files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest_param_files/
VCS: https://github.com/chrisjsewell/pytest-param-files
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Provides: python3-module-%alt_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
A small package to generate parametrized pytests from external files.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Sep 02 2024 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.3.5 -> 0.6.0.

* Tue Jul 11 2023 Andrey Limachko <liannnix@altlinux.org> 0.3.5-alt2
- add providing python3-module-pytest-param-files
- build with rpm-build-pyproject

* Sun Jul 09 2023 Andrey Limachko <liannnix@altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus
