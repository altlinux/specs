Name: python3-module-astral
Version: 3.2
Release: alt3

Summary: Python calculations for the position of the sun and moon.
License: APL
Group: Development/Python
URL: https://pypi.org/project/astral
VCS: https://github.com/sffjunkie/astral

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
This is astral -- a Python module which calculates:
* times for various positions of the sun: dawn, sunrise, solar noon, sunset,
  dusk, solar elevation, solar azimuth and rahukaalam.
* the phase of the moon.

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
%pyproject_run_pytest

%files
%python3_sitelibdir/astral
%python3_sitelibdir/astral-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2-alt3
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.2-alt2.1
- Demodernized packaging.

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2-alt2
- freshen packaging

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2-alt1
- 3.2 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.1-alt1
- initial
