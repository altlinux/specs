%define oname gabbi

%def_with python3

Summary: Declarative HTTP testing library
Name: python-module-%oname
Version: 1.34.0
Release: alt1.1
Url: https://github.com/cdent/gabbi
Source: %oname-%version.tar.gz
License: Apache
Group: Development/Python

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools python-module-pbr
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-pbr
%endif

%description
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Declarative HTTP testing library
Group: Development/Python3

%description -n python3-module-%oname
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version
%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.34.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.34.0-alt1
- initial build
