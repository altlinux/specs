Name: python3-module-wsproto
Version: 1.3.2
Release: alt1

Summary: Python WebSocket implementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/wsproto
VCS: https://github.com/python-hyper/wsproto

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
%pyproject_deps_resync_check_depgroup testing

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/wsproto
%python3_sitelibdir/wsproto-%version.dist-info

%changelog
* Fri Nov 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.2-alt1
- 1.3.2 released

* Wed Nov 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.1-alt1
- 1.3.1 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- 1.1.0 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial
