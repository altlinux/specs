%define _unpackaged_files_terminate_build 1
%define pypi_name sphinx_design
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt2
Summary: A sphinx extension for designing beautiful, view size responsive web components
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sphinx_design
Vcs: https://github.com/executablebooks/sphinx-design
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
# tests/conftest.py
BuildRequires: python3-module-sphinx-tests
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.6.0-alt2
- Mapped PyPI name to distro's one.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.2.0 -> 0.6.0.

* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.2.0-alt1
- Autobuild version bump to 0.2.0

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.0.1-alt1
- Initial version for ALT
