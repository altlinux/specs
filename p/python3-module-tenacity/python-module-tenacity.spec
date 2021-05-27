%define oname tenacity

Name: python3-module-%oname
Version: 4.12.0
Release: alt2
Summary: Retrying library
Group: Development/Python3
License: Apache-2.0
Url: https://github.com/jd/tenacity
Source: %oname-%version.tar.gz
Patch: tenacity-fix-py2.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-pbr
BuildRequires: python3-module-monotonic >= 0.6

%description
Tenacity is an Apache 2.0 licensed general-purpose
retrying library, written in Python, to simplify the task
of adding retry behavior to just about anything.
It originates from a fork of Retrying

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version
%patch -p1

# Remove bundled egg-info
rm -rf %oname.egg-info

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Thu May 27 2021 Grigory Ustinov <grenka@altlinux.org> 4.12.0-alt2
- Drop python2 support.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 4.12.0-alt1
- 4.12.0

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- initial build

