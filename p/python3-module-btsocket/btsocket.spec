Name: python3-module-btsocket
Version: 0.3.0
Release: alt1

Summary: A Python library to interact with Bluez Bluetooth Management API on Linux.
License: MIT
Group: Development/Python
Url: https://pypi.org/project/btsocket/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/btsocket
%python3_sitelibdir/btsocket-%version.dist-info

%changelog
* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.0-alt1
- 0.3.0 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- 0.2.0 released
