Name: python3-module-aiogithubapi
Version: 26.0.0
Release: alt1

Summary: Asynchronous Python client for the GitHub API
License: MIT
Group: Development/Python
URL: https://pypi.org/project/aiogithubapi
VCS: https://github.com/ludeeus/aiogithubapi

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
sed -ri '/^version\s+=/ s,"[^"]+,"%version,' pyproject.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/aiogithubapi
%python3_sitelibdir/aiogithubapi-%version.dist-info

%changelog
* Wed Apr 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 26.0.0-alt1
- 26.0.0 released
