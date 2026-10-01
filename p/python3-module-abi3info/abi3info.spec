%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-abi3info
Version: 2026.9.25
Release: alt1
Summary: Python abi3 info
License: MIT
Group: Development/Python
Url: https://pypi.org/project/abi3info
VCS: https://github.com/woodruffw/abi3info
BuildArch: noarch
Source0: %name-%version.tar
Source1: pyproject_deps.json
Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

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
* Thu Oct 01 2026 Stanislav Levin <slev@altlinux.org> 2026.9.25-alt1
- 2025.11.29 -> 2026.9.25

* Mon Dec 01 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.11.29-alt1
- 2025.11.29 released

* Wed Nov 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.11.18-alt1
- 2025.11.18 released

* Thu Oct 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.4.29-alt1
- initial
