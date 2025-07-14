%define _unpackaged_files_terminate_build 1
%define pypi_name aiosignal
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1
Summary: A project to manage callbacks in asyncio projects
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiosignal/
Vcs: https://github.com/aio-libs/aiosignal
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
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/wheel.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# see for details .github/workflows/ci-cd.yml
%pyproject_run_pytest -vra -o=addopts=''

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 14 2025 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.2 -> 1.4.0.

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.2-alt1
- 1.3.2 released

* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

