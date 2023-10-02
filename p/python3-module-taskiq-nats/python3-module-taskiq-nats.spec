%define _unpackaged_files_terminate_build 1
%define pypi_name taskiq-nats
%define mod_name taskiq_nats

# tests require running NATS server
%def_without check

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1

Summary: NATS broker for taskiq
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/project/taskiq-nats/
Vcs: https://github.com/taskiq-python/taskiq-nats

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter autoflake
%add_pyproject_deps_check_filter wemake-python-styleguide
%add_pyproject_deps_check_filter yesqa
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Taskiq-nats is a plugin for taskiq that adds NATS broker.

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

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Wed Jun 14 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- New version.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.0-alt1
- Initial build for ALT Sisyphus.

