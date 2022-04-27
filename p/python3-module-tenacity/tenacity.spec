%define oname tenacity

%def_with check

Name: python3-module-%oname
Version: 8.0.1
Release: alt1

Summary: Retrying library

Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/tenacity

# Cant be build from github=(
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tornado
BuildRequires: python3-module-typeguard
%endif

%description
Tenacity is an Apache 2.0 licensed general-purpose
retrying library, written in Python, to simplify the task
of adding retry behavior to just about anything.
It originates from a fork of Retrying

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3

%files
%python3_sitelibdir/*

%changelog
* Mon Apr 25 2022 Grigory Ustinov <grenka@altlinux.org> 8.0.1-alt1
- Build new version.
- Build with check.

* Thu May 27 2021 Grigory Ustinov <grenka@altlinux.org> 4.12.0-alt2
- Drop python2 support.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 4.12.0-alt1
- 4.12.0

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- initial build

