Name: python3-module-abi3info
Version: 2025.11.29
Release: alt1

Summary: Python abi3 info
License: MIT
Group: Development/Python
Url: https://pypi.org/project/abi3info
VCS: https://github.com/woodruffw/abi3info

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
%pyproject_deps_resync_check_depgroup test

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test

%files
%python3_sitelibdir/abi3info
%python3_sitelibdir/abi3info-%version.dist-info

%changelog
* Mon Dec 01 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.11.29-alt1
- 2025.11.29 released

* Wed Nov 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.11.18-alt1
- 2025.11.18 released

* Thu Oct 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.4.29-alt1
- initial
