%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-pretty
%define mod_name pytest_pretty

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: pytest plugin for pretty printing the test summary
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-pretty/
Vcs: https://github.com/samuelcolvin/pytest-pretty

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
Opinionated pytest plugin to make output slightly easier to read and
errors easy to find and fix.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat May 20 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Initial build for ALT Sisyphus.

