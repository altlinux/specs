%define _unpackaged_files_terminate_build 1
%define pypi_name pypi-json
%define mod_name pypi_json

# tests require the Internet connection
%def_without check

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: PyPI JSON API client library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pypi-json/
Vcs: https://github.com/repo-helper/pypi-json

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
* Wed Aug 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- initial build for Sisyphus

