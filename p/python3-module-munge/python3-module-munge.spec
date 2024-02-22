%define _unpackaged_files_terminate_build 1
%define pypi_name munge

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Data manipulation library and client
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/munge/
Vcs: https://github.com/20c/munge

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pytest-filedata
%add_pyproject_deps_check_filter tox-gh-actions
%pyproject_builddeps_metadata_extra yaml
%pyproject_builddeps_metadata_extra toml
%pyproject_builddeps_metadata_extra tomlkit
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
%doc README.md CHANGELOG.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Feb 22 2024 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- Built for ALT Sisyphus.

