%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-yeelight
Version: 0.7.14
Release: alt1
Summary: A Python library for controlling YeeLight WiFi RGB bulbs.
License: BSD-2-Clause
Group: Development/Python3
Url: https://gitlab.com/stavros/python-yeelight
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-future
BuildRequires: python3-module-ifaddr
%endif

%description
Simple Python library that allows you to control YeeLight WiFi RGB LED
bulbs through your LAN.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/yeelight
%python3_sitelibdir/%{pyproject_distinfo yeelight}

%changelog
* Tue Feb 13 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.14-alt1
- Initial build for ALT.
