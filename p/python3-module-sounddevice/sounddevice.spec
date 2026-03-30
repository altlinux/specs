Name: python3-module-sounddevice
Version: 0.5.5
Release: alt2

Summary: Python PortAudio bindings
License: MIT
Group: Development/Python
URL: https://pypi.org/project/sounddevice
VCS: https://github.com/spatialaudio/python-sounddevice

Source: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
This Python module provides bindings for the PortAudio library and a few
convenience functions to play and record NumPy_ arrays containing audio signals

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/_sounddevice.py
%python3_sitelibdir/sounddevice.py
%python3_sitelibdir/*/*sounddevice.*
%python3_sitelibdir/sounddevice-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.5-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.5.5-alt1.1
- Demodernized packaging.

* Fri Feb 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.5-alt1
- 0.5.5 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.3-alt1
- 0.5.3 released

* Thu Sep 04 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.2-alt1
- 0.5.2 released

* Thu Jan 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.1-alt1
- 0.5.1 released

* Thu Sep 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.0-alt1
- 0.5.0 released

* Tue Jun 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.6-alt1
- 0.4.6 released

* Fri Jan 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.5-alt1
- 0.4.5 released
