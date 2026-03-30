Name: python3-module-reedsolo
Version: 2.0.5
Release: alt2

Summary: Reed-Solomon codec in python
License: MIT
Group: Development/Python
URL: https://pypi.org/project/reedsolo
VCS: https://github.com/tomerfiliba/reedsolomon

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
%pyproject_deps_resync_check_tox tox.ini testenv

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/reedsolo.py
%python3_sitelibdir/*/reedsolo*.pyc
%python3_sitelibdir/reedsolo-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.5-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.0.5-alt1.1
- Demodernized packaging.

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.5-alt1
- 2.0.5 released

* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released

* Mon Dec 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.4-alt1
- initial
