Name: python3-module-asyncinotify
Version: 4.4.0
Release: alt1.1

Summary: A simple optionally-async python inotify library
License: MPL-2.0
Group: Development/Python
URL: https://pypi.org/project/asyncinotify
VCS: https://github.com/ProCern/asyncinotify

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%description
%summary

%prep
%setup

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
