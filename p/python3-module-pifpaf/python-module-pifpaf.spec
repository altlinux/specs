%define oname pifpaf

Summary: Suite of tools and fixtures to manage daemons for testing
Name: python3-module-%oname
Version: 3.1.5
Release: alt2
Url: https://pypi.org/project/pifpaf
Source: %oname-%version.tar.gz
Patch: remove-distutils-for-python-3.12.patch
License: Apache-2.0
Group: Development/Python3

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr
BuildRequires: python3-module-cliff
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-six
BuildRequires: python3-module-fixtures

%add_python3_req_skip swift.common

%description
Pifpaf is a suite of fixtures and a command-line tool that allows to start
and stop daemons for a quick throw-away usage. This is typically useful when
needing these daemons to run integration testing. It originaly evolved from
its precussor overtest.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version
%patch -p2

%build
export LANG=en_US.UTF-8
%python3_build

%install
export LANG=en_US.UTF-8
%python3_install

%files
%doc README.rst
%_bindir/pifpaf
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Tue Dec 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.5-alt2
- Drop dependency on distutils.

* Wed May 12 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.5-alt1
- Build new version.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Build new version.
- Fix license.

* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt2
- Build without python2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- initial build
