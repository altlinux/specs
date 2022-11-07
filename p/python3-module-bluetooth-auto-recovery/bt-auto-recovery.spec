Name: python3-module-bluetooth-auto-recovery
Version: 0.3.6
Release: alt1

Summary: Recover bluetooth adapters that are in an stuck state
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bluetooth-auto-recovery/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/bluetooth_auto_recovery
%python3_sitelibdir/bluetooth_auto_recovery-%version.dist-info

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.6-alt1
- 0.3.6 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.3-alt1
- 0.3.3 released
