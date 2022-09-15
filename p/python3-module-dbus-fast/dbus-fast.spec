Name: python3-module-dbus-fast
Version: 1.4.0
Release: alt1

Summary: Python library for DBus
License: MIT
Group: Development/Python
Url: https://pypi.org/project/sensor-state-data

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
%python3_sitelibdir/dbus_fast
%python3_sitelibdir/dbus_fast-%version.dist-info

%changelog
* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released
