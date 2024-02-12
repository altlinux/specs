%define oname gabbi

Name: python3-module-%oname
Version: 2.7.2
Release: alt1

Summary: Declarative HTTP testing library
License: Apache
Group: Development/Python3
Url: https://github.com/cdent/gabbi

BuildArch: noarch

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
BuildRequires: python3-module-yaml
BuildRequires: python3-module-urllib3 >= 1.26.9
BuildRequires: python3-module-certifi
BuildRequires: python3-module-jsonpath-rw-ext >= 1.0.0
BuildRequires: python3-module-wsgi_intercept >= 1.9.3
BuildRequires: python3-module-colorama

%description
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form.

%package tests
Summary: Tests for %oname
Group: Development/Python3
BuildRequires: python3-module-stestr
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-hacking
BuildRequires: python3-module-sphinx
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
export PBR_VERSION=%version
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Feb 12 2024 Ilfat Aminov <aminov@altlinux.org> 2.7.2-alt1
- 2.7.2

* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.34.0-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.34.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.34.0-alt1
- initial build
