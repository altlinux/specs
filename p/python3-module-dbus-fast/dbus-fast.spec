Name: python3-module-dbus-fast
Version: 2.12.0
Release: alt1

Summary: Python library for DBus
License: MIT
Group: Development/Python
Url: https://pypi.org/project/sensor-state-data

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3(pytest)

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/dbus_fast
%python3_sitelibdir/dbus_fast-%version.dist-info

%changelog
* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.12.0-alt1
- 2.12.0 released

* Thu Sep 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.95.2-alt1
- 1.95.2 released

* Thu Sep 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.94.1-alt1
- 1.94.1 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.91.4-alt1
- 1.91.4 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.86.0-alt1
- 1.86.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.85.0-alt1
- 1.85.0 released

* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.84.1-alt1
- 1.84.1 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.82.0-alt1
- 1.82.0 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.61.1-alt1
- 1.61.1 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released
