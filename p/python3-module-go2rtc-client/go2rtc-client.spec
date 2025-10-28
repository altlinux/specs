Name: python3-module-go2rtc-client
Version: 0.2.1
Release: alt1

Summary: Asynchronous Python client for go2rtc
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/go2rtc-client
VCS: https://github.com/home-assistant-libs/python-go2rtc-client

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
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o=addopts= tests

%files
%python3_sitelibdir/go2rtc_client
%python3_sitelibdir/go2rtc_client-%version.dist-info

%changelog
* Fri Oct 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.2-alt1
- 0.1.2 released

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.0-alt1
- 0.1.0 released

