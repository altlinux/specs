Name: python3-module-habluetooth
Version: 2.8.0
Release: alt1

Summary: High availability Bluetooth
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/habluetooth/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry-core)
BuildRequires: python3(setuptools)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(bleak)
BuildRequires: python3(bleak_retry_connector)
BuildRequires: python3(bluetooth_adapters)
BuildRequires: python3(bluetooth_auto_recovery)
BuildRequires: python3(bluetooth_data_tools)
BuildRequires: python3(typing_extensions)
BuildRequires: python3(async_interrupt)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/habluetooth
%python3_sitelibdir/habluetooth-%version.dist-info

%changelog
* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.8.0-alt1
- 2.8.0 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.2-alt1
- 2.4.2 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released
