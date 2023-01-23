Name: python3-module-bluetooth-data-tools
Version: 0.3.1
Release: alt1

Summary: Tools for converting bluetooth data and packets
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/bluetooth-data-tools/

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
%python3_sitelibdir/bluetooth_data_tools
%python3_sitelibdir/bluetooth_data_tools-%version.dist-info

%changelog
* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

