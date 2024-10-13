%define _unpackaged_files_terminate_build 1
%define pypi_name logging-journald
%define mod_name logging_journald

# broken tests
%def_without check

Name: python3-module-%pypi_name
Version: 0.6.9
Release: alt1

Summary: Pure python logging handler for writing logs to the journald using native protocol
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/logging-journald/
Vcs: https://github.com/mosquito/logging-journald

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md COPYING
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/__pycache__/%mod_name.*.pyc

%changelog
* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.9-alt1
- Updated to 0.6.9.

* Mon Feb 12 2024 Anton Zhukharev <ancieg@altlinux.org> 0.6.7-alt1
- Updated to 0.6.7.

* Wed Sep 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.6.6-alt1
- Updated to 0.6.6.
- Distributed under MIT license.

* Sun May 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.6.4-alt1
- Initial build for ALT Sisyphus.

