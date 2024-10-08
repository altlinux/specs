%define _unpackaged_files_terminate_build 1
%define pypi_name click-didyoumean
%define mod_name click_didyoumean

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1
Summary: Enable git-like did-you-mean feature in click
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/click-didyoumean/
Vcs: https://github.com/click-contrib/click-didyoumean
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Enable git-like did-you-mean feature in click.

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
# see .github/workflows/cicd.yml
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 08 2024 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1
- 0.0.3 -> 0.3.1.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.0.3-alt2
- initial build for ALT Sisyphus

