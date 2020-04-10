%define oname gabbi

Name: python3-module-%oname
Version: 1.34.0
Release: alt2

Summary: Declarative HTTP testing library
License: Apache
Group: Development/Python3
Url: https://github.com/cdent/gabbi

BuildArch: noarch

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

%description
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.34.0-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.34.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.34.0-alt1
- initial build
