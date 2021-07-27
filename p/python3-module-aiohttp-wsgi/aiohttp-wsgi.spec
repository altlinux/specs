%define oname aiohttp-wsgi

%def_disable check

Name: python3-module-%oname
Version: 0.6.3
Release: alt2
Summary: WSGI adapter for aiohttp
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/aiohttp-wsgi/

# https://github.com/etianen/aiohttp-wsgi.git
Source0: https://pypi.python.org/packages/72/ff/21ac6cde48057c92cfc7076c1d9281560c0b586dfc90838bdce6e2bc4e08/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides aiohttp_wsgi
%py3_requires aiohttp

BuildRequires: python3-module-coverage python3-module-nose python3-module-pytest

%description
aiohttp-wsgi is a WSGI adapter for aiohttp.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
aiohttp-wsgi is a WSGI adapter for aiohttp.

This package contains tests for %oname.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v --cover-package=aiohttp_wsgi --cover-erase --with-coverage

%files
%doc *.rst
%python3_sitelibdir/*

#%files -n python3-module-%oname-tests
#python3_sitelibdir/*/test*
#python3_sitelibdir/*/*/test*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt2
- Drop python2 support.

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150331.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150331.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150331
- Initial build for Sisyphus

