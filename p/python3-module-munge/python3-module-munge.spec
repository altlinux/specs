%define _unpackaged_files_terminate_build 1
%define pypi_name munge
%define import_name munge

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.1
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
%add_pyproject_deps_check_filter ctl
%add_pyproject_deps_check_filter pytest-filedata
%add_pyproject_deps_check_filter tox-gh-actions
%add_pyproject_deps_check_filter tmpl
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

# Fix version up (upstream forgets that frequently)
sed -i 's/^version = ".*"/version = "%version"/' pyproject.toml

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md CHANGELOG.md
%_bindir/munge
%python3_sitelibdir/%import_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 16 2025 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- Updated to 1.4.1.

* Thu Feb 22 2024 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- Built for ALT Sisyphus.

