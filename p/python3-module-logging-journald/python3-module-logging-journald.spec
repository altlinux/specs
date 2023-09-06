%define _unpackaged_files_terminate_build 1
%define pypi_name logging-journald
%define mod_name logging_journald

# build aiomisc first
%def_without check

Name: python3-module-%pypi_name
Version: 0.6.6
Release: alt1

Summary: Pure python logging handler for writing logs to the journald using native protocol
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/logging-journald/
Vcs: https://github.com/mosquito/logging-journald

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
%summary.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md COPYING
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/__pycache__/%mod_name.*.pyc

%changelog
* Wed Sep 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.6.6-alt1
- Updated to 0.6.6.
- Distributed under MIT license.

* Sun May 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.6.4-alt1
- Initial build for ALT Sisyphus.

