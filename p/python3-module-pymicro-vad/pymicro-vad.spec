Name: python3-module-pymicro-vad
Version: 2.0.1
Release: alt2

Summary: Voice activity detector for Python
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/pymicro-vad
VCS: https://github.com/rhasspy/pymicro-vad

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%python3_set_limited_api 3.9

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements_dev.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addpots= tests

%files
%python3_sitelibdir/micro_vad_cpp.*
%python3_sitelibdir/pymicro_vad
%python3_sitelibdir/pymicro_vad-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.1-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1.1
- Demodernized packaging.

* Thu Feb 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.1-alt1
- 2.0.1 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released
