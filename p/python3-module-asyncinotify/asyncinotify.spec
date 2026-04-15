Name: python3-module-asyncinotify
Version: 4.4.4
Release: alt1

Summary: A simple optionally-async python inotify library
License: MPL-2.0
Group: Development/Python
URL: https://pypi.org/project/asyncinotify
VCS: https://github.com/ProCern/asyncinotify

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

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
%pyproject_run -- python test.py

%files
%python3_sitelibdir/asyncinotify
%python3_sitelibdir/asyncinotify-%version.dist-info

%changelog
* Wed Apr 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.4.4-alt1
- 4.4.4 released

* Thu Apr 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.4.2-alt1
- 4.4.2 released

* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.4.0-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt1.1
- Demodernized packaging.

* Fri Feb 13 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.4.0-alt1
- 4.4.0 released

* Fri Nov 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.3.2-alt1
- 4.3.2 released

* Tue Nov 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.2.2-alt1
- 4.2.2 released

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.2.1-alt1
- 4.2.1 released
