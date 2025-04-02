%define _unpackaged_files_terminate_build 1
%define pypi_name diff-cover
%define mod_name diff_cover
%def_with check

Name: python3-module-%pypi_name
Version: 9.2.4
Release: alt1

Summary: Automatically find diff lines that need test coverage

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/diff-cover
VCS: https://github.com/Bachmann1234/diff_cover

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pylint
BuildRequires: python3-module-flake8
%endif

%description
Also finds diff lines that have violations (according to
tools such as pycodestyle, pyflakes, flake8, or pylint).

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
%doc CHANGELOG README.rst
%_bindir/diff-*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Apr 01 2025 Anastasia Doronina <swaggyglice@altlinux.org> 9.2.4-alt1
- Update to 9.2.4.

* Wed Feb 19 2025 Anastasia Doronina <swaggyglice@altlinux.org> 9.2.3-alt1
- Initial Build for Sisyphus.
