%define _unpackaged_files_terminate_build 1
%define pypi_name pipcl
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 13
Release: alt1
Summary: Python packaging operations for use by a setup.py
License: AGPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/pipcl/
Vcs: https://github.com/ArtifexSoftware/pipcl.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Python packaging operations, including PEP-517 support, for use by a setup.py script.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# These tests run pip install and require Internet access.
%pyproject_run_pytest -vra \
    --ignore=tests/test_change_versions.py \
    --ignore=tests/test_doctest.py \
    --ignore=tests/test_lint.py \
    --ignore=tests/test_project.py

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 24 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 13-alt1
- Initial build for ALT.
