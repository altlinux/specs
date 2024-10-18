%define _unpackaged_files_terminate_build 1
%define pypi_name treelib
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.7.0
Release: alt1
Summary: A Python implementation of tree structure
License: %asl
Group: Development/Python
Url: https://pypi.org/project/treelib/
Vcs: https://github.com/caesar0301/treelib
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Tree implementation in python.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-t.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/python-package.yml
%pyproject_run_pytest -vra

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 18 2024 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.1 -> 1.7.0.

* Wed May 04 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.
