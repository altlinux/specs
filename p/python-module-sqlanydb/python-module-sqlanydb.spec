%define _unpackaged_files_terminate_build 1
# -*- coding: utf-8 -*-
%define oname sqlanydb

%def_with python3

Name: python-module-%oname
Version: 1.0.8
Release: alt1
Epoch: 1
License: Apache
BuildArch: noarch
Group: Development/Python
Summary: Python interface for Sybase Anywhere DB
Summary(ru_RU.UTF-8): Интерфейс к БД Sybase Anywhere для Python

Url: http://code.google.com/p/sqlanydb/

Source0: https://pypi.python.org/packages/45/62/e0c80101e551fb16ca919cc80b1938ff225e0f20c3afdabf35d6ca79e52f/%{oname}-%{version}.tar.gz

Requires: python >= 2.4
Requires: libfreetds >= 0.64
Requires: python-module-egenix-mx-base

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
This a Google Code project providing a python interface to the
SQL Anywhere Database. This interface conforms to PEP 249.

%package -n python3-module-%oname
Summary: Python interface for Sybase Anywhere DB
Group: Development/Python3
Requires: libfreetds >= 0.64

%description -n python3-module-%oname
This a Google Code project providing a python interface to the
SQL Anywhere Database. This interface conforms to PEP 249.

%prep
%setup -q -n %{oname}-%{version}

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.0.6-alt1.git20140626.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.6-alt1.git20140626
- Version 1.0.6
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.0.2-alt1.1
- Rebuild with Python-2.7

* Sat Dec 18 2010 Alexey Morsov <swi@altlinux.ru> 1:1.0.2-alt1
- initial build for Sisyphus


