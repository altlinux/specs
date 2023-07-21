%define _unpackaged_files_terminate_build 1
%define pypi_name coverage-pyver-pragma
%define mod_name coverage_pyver_pragma

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.2
Release: alt1

Summary: Plugin for Coverage.py to selectively ignore branches depending on the Python version
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/coverage-pyver-pragma/
Vcs: https://github.com/python-coincidence/coverage_pyver_pragma

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
BuildRequires: python3-module-coverage
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt1
- initial build for Sisyphus

