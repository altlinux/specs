Name: python3-module-bleak-retry-connector
Version: 3.1.3
Release: alt1

Summary: A connector for Bleak Client
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bleak-retry-connector/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(bleak)
BuildRequires: python3(bluetooth_adapters)

%description
Bleak is a GATT client software, capable of connecting to BLE devices
acting as GATT servers. It is designed to provide a asynchronous,
cross-platform Python API to connect and communicate with e.g. sensors.

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
%python3_sitelibdir/bleak_retry_connector
%python3_sitelibdir/bleak_retry_connector-%version.dist-info

%changelog
* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.3-alt1
- 3.1.3 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- 3.0.2 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.13.0-alt1
- 2.13.0 released

* Mon Nov  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.2-alt1
- 2.8.2 released
