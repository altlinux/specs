Name: python3-module-voluptuous-openapi
Version: 0.4.0
Release: alt1

Summary: Convert voluptuous schemas to OpenAPI Schema object
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/voluptuous-openapi
VCS: https://github.com/home-assistant-libs/voluptuous-openapi

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
%pyproject_deps_resync_check_pipreqfile requirements_test.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/voluptuous_openapi
%python3_sitelibdir/voluptuous_openapi-%version.dist-info

%changelog
* Fri Jun 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.0-alt1
- 0.4.0 released

* Tue Feb 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.0-alt1
- 0.3.0 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.6-alt1
- 0.0.6 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.4-alt1
- 0.0.4 released
