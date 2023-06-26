%define _unpackaged_files_terminate_build 1
%define pypi_name confu

%def_with check

Name: python3-module-%pypi_name
Version: 1.8.0
Release: alt1

Summary: Configuration validation and generation
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/confu/
Vcs: https://github.com/20c/confu

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter ctl
%add_pyproject_deps_check_filter pymdgen
%add_pyproject_deps_check_filter tmpl
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

%check
%pyproject_run_pytest -vra

%files
%doc CHANGELOG.md LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 26 2023 Anton Zhukharev <ancieg@altlinux.org> 1.8.0-alt1
- Initial build for ALT Sisyphus.

