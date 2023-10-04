%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-datadir

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.0
Release: alt1

Summary: pytest plugin for manipulating test data directories and files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-datadir/
Vcs: https://github.com/gabrielcnr/pytest-datadir

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
pytest plugin for manipulating test data directories and files.

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
%pyproject_run_pytest

%files
%doc README.md AUTHORS
%python3_sitelibdir/pytest_datadir/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Oct 04 2023 Anton Zhukharev <ancieg@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Wed May 10 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- New version.

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.3.1-alt1
- initial build for Sisyphus

