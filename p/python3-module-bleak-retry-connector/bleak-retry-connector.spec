Name: python3-module-bleak-retry-connector
Version: 2.13.0
Release: alt1

Summary: A connector for Bleak Client
License: MIT
Group: Development/Python
Url: https://pypi.org/project/bleak-retry-connector/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
Bleak is a GATT client software, capable of connecting to BLE devices
acting as GATT servers. It is designed to provide a asynchronous,
cross-platform Python API to connect and communicate with e.g. sensors.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/bleak_retry_connector
%python3_sitelibdir/bleak_retry_connector-%version.dist-info

%changelog
* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.13.0-alt1
- 2.13.0 released

* Mon Nov  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.2-alt1
- 2.8.2 released
