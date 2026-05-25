Name: python3-module-cached-ipaddress
Version: 1.1.1
Release: alt1

Summary: Cache construction of ipaddress objects
License: MIT
Group: Development/Python
URL: https://pypi.org/project/cached-ipaddress
VCS: https://github.com/bdraco/cached-ipaddress

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%python3_set_limited_api 3.12

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o=addopts= tests

%files
%python3_sitelibdir/cached_ipaddress
%python3_sitelibdir/cached_ipaddress-%version.dist-info

%changelog
* Mon May 25 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.1-alt1
- 1.1.1 released

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.1-alt2
- fixed runtime deps

* Thu Oct 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.1-alt1
- 1.0.1 released

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.8.0-alt2
- added propcache as runtime dep

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.8.0-alt1
- 0.8.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.0-alt1
- 0.5.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released
