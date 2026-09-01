Name: python3-module-transmission-rpc
Version: 7.0.12
Release: alt1

Summary: Transmission JSON RPC wrapper
License: MIT
Group: Development/Python
URL: https://pypi.org/project/transmission-rpc
VCS: https://github.com/trim21/transmission-rpc

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_check_filter pytest-github-actions-annotate-failures
%pyproject_builddeps_build
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k 'not test_groups and not test_real_'

%files
%python3_sitelibdir/transmission_rpc
%python3_sitelibdir/transmission_rpc-%version.dist-info

%changelog
* Tue Sep 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 7.0.12-alt1
- 0.7.12 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 7.0.11-alt1
- 7.0.11 released

* Wed Jun 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 7.0.8-alt1
- 7.0.8 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.0.3-alt1
- 7.0.3 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.5-alt1
- 4.1.5 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.4.0-alt1
- 3.4.0 released
