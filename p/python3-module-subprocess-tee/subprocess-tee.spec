%define _unpackaged_files_terminate_build 1
%define pypi_name subprocess-tee
%define mod_name subprocess_tee

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.2
Release: alt1
Summary: Subprocess-tee
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/subprocess-tee
Vcs: https://github.com/pycontribs/subprocess-tee
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged yet
%add_pyproject_deps_check_filter pytest-plus
%add_pyproject_deps_check_filter molecule
%pyproject_builddeps_metadata_extra test
%endif

%description
This package provides a drop-in alternative to subprocess.run that captures the
output while still printing it in real-time, just the way tee does.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# molecule is not packaged yet
%pyproject_run_pytest -ra -Wignore --deselect='test/test_func.py::test_molecule'

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 18 2024 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1
- 0.4.1 -> 0.4.2.

* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus.
