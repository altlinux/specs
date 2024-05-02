Name: python3-module-bluetooth-auto-recovery
Version: 1.4.2
Release: alt1

Summary: Recover bluetooth adapters that are in an stuck state
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bluetooth-auto-recovery/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(pyric)
BuildRequires: python3(btsocket)
BuildRequires: python3(usb_devices)
BuildRequires: python3(async_timeout)
BuildRequires: python3(bluetooth_adapters)

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/bluetooth_auto_recovery
%python3_sitelibdir/bluetooth_auto_recovery-%version.dist-info

%changelog
* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.2-alt1
- 1.4.2 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- 1.2.3 released

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2
- fixed ftbfs

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.2-alt1
- 1.1.2 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt1
- 1.0.3 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.6-alt1
- 0.3.6 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.3-alt1
- 0.3.3 released
