%define _unpackaged_files_terminate_build 1
%define pypi_name Quart
%define pypi_nname quart
%define mod_name %pypi_nname

%def_with check

Name: python3-module-%pypi_nname
Version: 0.19.6
Release: alt1
Summary: A Python ASGI web microframework with the same API as Flask
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/quart
Vcs: https://github.com/pallets/quart/
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
Quart is an async Python web microframework. Using Quart you can,
- render and serve HTML templates,
- write (RESTful) JSON APIs,
- serve WebSockets,
- stream request and response data,
- do pretty much anything over the HTTP or WebSocket protocols.

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
%_bindir/quart
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon May 20 2024 Stanislav Levin <slev@altlinux.org> 0.19.6-alt1
- 0.19.5 -> 0.19.6.

* Wed Apr 03 2024 Stanislav Levin <slev@altlinux.org> 0.19.5-alt1
- 0.19.4 -> 0.19.5.

* Mon Feb 05 2024 Stanislav Levin <slev@altlinux.org> 0.19.4-alt1
- Initial build for Sisyphus.
