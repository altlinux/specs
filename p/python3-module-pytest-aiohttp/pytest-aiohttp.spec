%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-aiohttp
%define mod_name pytest_aiohttp

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.5
Release: alt1
Summary: pytest plugin for aiohttp support
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pytest-aiohttp/
VCS: https://github.com/aio-libs/pytest-aiohttp
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
# tests require aiohttp.test_utils
BuildRequires: python3-module-aiohttp-tests
%endif

%description
pytest plugin for aiohttp support

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Dec 08 2023 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1
- 1.0.4 -> 1.0.5.

* Thu Feb 09 2023 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- 0.3.0 -> 1.0.4.

* Sat May 22 2021 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- new version (0.3.0) with rpmgs script
- cleanup spec

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt2
- Updated build dependencies.

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.1.3-alt1
- Initial build for ALT Linux Sisyphus.
