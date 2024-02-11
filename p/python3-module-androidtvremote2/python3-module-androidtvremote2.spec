%define _unpackaged_files_terminate_build 1
%define module_name androidtvremote2

Name: python3-module-%module_name
Version: 0.0.14
Release: alt1
Summary: A Python library implementing the Android TV Remote protocol v2
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/tronikos/androidtvremote2
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
A Python library for interacting with Android TV using
the Android TV Remote protocol v2. This is the same protocol
the Google TV mobile app is using. It doesn't require ADB
or enabling developer tools on the Android TV device. It only
requires the Android TV Remote Service that comes pre-installed
on most Android TV devices.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %module_name}
%exclude %python3_sitelibdir/demo.py
%exclude %python3_sitelibdir/__pycache__/demo.*.pyc

%changelog
* Sun Feb 11 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.0.14-alt1
- Initial build for ALT.

