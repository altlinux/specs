Name: python3-module-casttube
Version: 0.2.1
Release: alt3

Summary: Python CHromecast API
License: MIT
Group: Development/Python
URL: https://pypi.org/project/casttube
VCS: https://github.com/ur1katz/casttube

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

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/casttube
%python3_sitelibdir/casttube-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt3
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt2.1
- Demodernized packaging.

* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt2
- moved to pyproject

* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- initial
