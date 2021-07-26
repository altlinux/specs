%define _unpackaged_files_terminate_build 1
%define oname aioxmlrpc

Name: python3-module-%oname
Version: 0.3
Release: alt2
Summary: XML-RPC for asyncio
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/aioxmlrpc/

# https://github.com/mardiros/aioxmlrpc.git
Source0: https://pypi.python.org/packages/71/83/471ca57441a412193b7824ac55cebf8dd12421d9176e5d2ab60d128aed46/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires asyncio aiohttp

BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-chardet

%description
Asyncio version of the standard lib xmlrpc.

Currently only aioxmlrpc.client, which works like xmlrpc.client but with
coroutine is implemented.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Asyncio version of the standard lib xmlrpc.

Currently only aioxmlrpc.client, which works like xmlrpc.client but with
coroutine is implemented.

This package contains tests for %oname.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.3-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20141112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20141112.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141112
- Initial build for Sisyphus

