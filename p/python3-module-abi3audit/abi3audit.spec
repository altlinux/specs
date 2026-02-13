%define _unpackaged_files_terminate_build 1
%define pypi_name abi3audit
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.26
Release: alt1
Summary: Python abi3 consistency scanner
License: MIT
Group: Development/Python
Url: https://pypi.org/project/abi3audit/
VCS: https://github.com/pypa/abi3audit
BuildArch: noarch
Source0: %name-%version.tar
Source1: pyproject_deps.json
Patch0: %name-%version-alt.patch
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
%autopatch -p1
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
%pyproject_run_pytest -vra

%files
%_bindir/abi3audit
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Feb 13 2026 Stanislav Levin <slev@altlinux.org> 0.0.26-alt1
- 0.0.24 -> 0.0.26.

* Wed Nov 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.24-alt1
- 0.0.24 released

* Mon Nov 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.23-alt1
- 0.0.23 released

* Thu Oct 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.22-alt1
- initial
