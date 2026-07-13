Name:    python3-module-pytest-test-groups
Version: 1.2.1
Release: alt1

Summary: Pytest plugin to split tests in groups
License: MIT
Group: Development/Python
URL: https://pypi.org/project/pytest-test-groups
VCS: https://github.com/mark-adams/pytest-test-groups

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/pytest_test_groups
%python3_sitelibdir/pytest_test_groups-%version.dist-info

%changelog
* Mon Jul 13 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.1-alt1
- 1.2.1 released

