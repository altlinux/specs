%define oname aioes

%def_disable check

Name: python3-module-%oname
Version: 0.7.2
Release: alt1
Summary: Elasticsearch integration with asyncio
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/aioes/

# https://github.com/aio-libs/aioes.git
Source0: https://pypi.python.org/packages/4a/36/742ba7c8d7f52aa6a9cea2ab802054c33241f1389a2883630efbc02b9925/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires asyncio aiohttp

BuildRequires: python3-module-nose python3-module-urllib3 python3-pyflakes

%description
aioes is a asyncio compatible library for working with ElasticSearch.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test
python3-pep8 .
python3-pyflakes .
nosetests3 -s -v tests
python3 cmp.py

%files
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Mon Aug 09 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.2-alt1
- Build new version.

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt2
- Drop python2 support.

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20141228.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.git20141228.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141228
- Initial build for Sisyphus

