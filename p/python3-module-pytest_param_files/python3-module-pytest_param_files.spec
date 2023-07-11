%define pypi_name pytest_param_files
%define alt_name pytest-param-files

%def_with check

Name:    python3-module-%pypi_name
Version: 0.3.5
Release: alt2

Summary: Create pytest parametrize decorators from external files
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pytest_param_files/
VCS:     https://github.com/chrisjsewell/pytest-param-files

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra testing
%pyproject_builddeps_metadata_extra linkify
%endif

Provides: python3-module-%alt_name

BuildArch: noarch

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

%description
A small package to generate parametrized pytests from external files.

%prep
%setup -n %pypi_name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject
%pyproject_run_pytest -ra tests

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 11 2023 Andrey Limachko <liannnix@altlinux.org> 0.3.5-alt2
- add providing python3-module-pytest-param-files
- build with rpm-build-pyproject

* Sun Jul 09 2023 Andrey Limachko <liannnix@altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus
