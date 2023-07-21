%define _unpackaged_files_terminate_build 1
%define pypi_name importcheck

# check disabled due to hard-coded test-data in the package
%def_without check

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: A tool to check all modules can be correctly imported
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/importcheck/
Vcs: https://github.com/python-coincidence/importcheck

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

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
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 0.5.0-alt1
- Updated to 0.5.0.

* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- initial build for Sisyphus

