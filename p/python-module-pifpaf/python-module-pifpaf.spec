%define oname pifpaf

%def_with python3

Summary: Suite of tools and fixtures to manage daemons for testing
Name: python-module-%oname
Version: 1.3.1
Release: alt1.1
Url: https://github.com/jd/pifpaf
Source: %oname-%version.tar.gz
License: Apache
Group: Development/Python

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools python-module-pbr
BuildRequires: python-module-cliff
BuildRequires: python-module-jinja2
BuildRequires: python-module-six
BuildRequires: python-module-fixtures

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-pbr
BuildRequires: python3-module-cliff
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-six
BuildRequires: python3-module-fixtures
%endif

%description
Pifpaf is a suite of fixtures and a command-line tool that allows to start
and stop daemons for a quick throw-away usage. This is typically useful when
needing these daemons to run integration testing. It originaly evolved from
its precussor overtest.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Suite of tools and fixtures to manage daemons for testing
Group: Development/Python3

%description -n python3-module-%oname
Pifpaf is a suite of fixtures and a command-line tool that allows to start
and stop daemons for a quick throw-away usage. This is typically useful when
needing these daemons to run integration testing. It originaly evolved from
its precussor overtest.


%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip swift.common

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
mv %buildroot%_bindir/pifpaf %buildroot%_bindir/pifpaf-3
popd
%endif

%python_install

%files
%doc README.rst
%_bindir/pifpaf
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%_bindir/pifpaf-3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- initial build
