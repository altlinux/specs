%define _unpackaged_files_terminate_build 1
%define pypi_name quart-trio
%define mod_name quart_trio

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.1
Release: alt2
Summary: A Quart extension to provide trio support
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/quart-trio
Vcs: https://github.com/pgjones/quart-trio/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Quart-Trio is an extension for Quart to support the Trio event loop. This is an
alternative to using the asyncio event loop present in the Python standard
library and supported by default in Quart.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.11.1-alt2
- Fixed FTBFS (trio 0.25.0).

* Tue Feb 06 2024 Stanislav Levin <slev@altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus.
