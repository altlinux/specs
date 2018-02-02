%define oname daiquiri

%def_with python3

Summary: Library to configure Python logging easily
Name: python-module-%oname
Version: 0.1.0
Release: alt1.1
Url: https://github.com/jd/daiquiri
Source: %oname-%version.tar.gz
License: Apache
Group: Development/Python

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools python-module-pbr
BuildRequires: python-module-six

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-pbr
BuildRequires: python3-module-six
%endif

%description
The daiquiri library provides an easy way to configure logging.
It also provides some custom formatters and handlers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Library to configure Python logging easily
Group: Development/Python3

%description -n python3-module-%oname
The daiquiri library provides an easy way to configure logging.
It also provides some custom formatters and handlers.


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
export LANG=en_US.UTF-8
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LANG=en_US.UTF-8
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- initial build
