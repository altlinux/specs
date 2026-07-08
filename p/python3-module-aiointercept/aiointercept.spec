Name: python3-module-aiointercept
Version: 0.1.8
Release: alt1

Summary: Mock aiohttp HTTP requests by routing them through a real aiohttp.web
License: MIT
Group: Development/Python
URL: https://pypi.org/project/aiointercept
VCS: https://github.com/Polandia94/aiointercept

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
export PBR_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup tests

%build
export PBR_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
# some are online
%pyproject_run_pytest -m "not network" -o=addopts= tests

%files
%python3_sitelibdir/aiointercept
%python3_sitelibdir/aiointercept-%version.dist-info

%changelog
* Wed Jul 08 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.8-alt1
- 0.1.8 released

