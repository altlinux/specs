%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject_hooks

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1
Summary: Wrappers to call pyproject.toml-based build backend hooks
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject_hooks
VCS: https://github.com/pypa/pyproject-hooks
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This is a low-level library for calling build-backends in pyproject.toml-based
project. It provides the basic functionality to help write tooling that
generates distribution files from Python projects.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 02 2024 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.0 -> 1.1.0.

* Thu Sep 14 2023 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Mapped PyPI name to distro's one.

* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
