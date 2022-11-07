Name: python3-module-bluetooth-adapters
Version: 0.6.0
Release: alt1

Summary: Tools to enumerate and find Bluetooth Adapters
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/bluetooth-adapters/

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
%python3_sitelibdir/bluetooth_adapters
%python3_sitelibdir/bluetooth_adapters-%version.dist-info

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released
