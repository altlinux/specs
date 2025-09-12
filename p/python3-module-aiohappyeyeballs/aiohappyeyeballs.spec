%define _unpackaged_files_terminate_build 1
%define pypi_name aiohappyeyeballs
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.6.1
Release: alt2
Summary: Happy Eyeballs
License: PSF-2.0
Group: Development/Python
Url: https://pypi.org/project/aiohappyeyeballs/
Vcs: https://github.com/aio-libs/aiohappyeyeballs
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
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
%pyproject_run_pytest -vra -o=addopts=''

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 12 2025 Stanislav Levin <slev@altlinux.org> 2.6.1-alt2
- Fixed FTBFS (pytest-asyncio 1.1.0).

* Tue May 27 2025 Stanislav Levin <slev@altlinux.org> 2.6.1-alt1
- 2.4.4 -> 2.6.1.

* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.4-alt1
- 2.4.4 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.3-alt1
- 2.4.3 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.0-alt1
- 2.4.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.2-alt1
- 2.3.2 released

