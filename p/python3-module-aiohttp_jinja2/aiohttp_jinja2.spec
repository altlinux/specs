%define oname aiohttp_jinja2

Name: python3-module-%oname
Epoch: 1
Version: 0.13.0
Release: alt3
Summary: jinja2 template renderer for aiohttp.web
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/aiohttp_jinja2/

# https://github.com/aio-libs/aiohttp_jinja2.git
Source0: https://pypi.python.org/packages/79/fc/925fc60d87d38f0d6dcb7b538b7064b15b508d688a2fa6cf8e400c192308/aiohttp-jinja2-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires asyncio aiohttp jinja2

BuildRequires: python3-module-aiohttp python3-module-coverage python3-module-html5lib python3-module-ipdb python3-module-nose python3-module-notebook

%description
jinja2 template renderer for aiohttp.web.

%prep
%setup -n aiohttp-jinja2-%{version}

%build
%python3_build

%install
%python3_install

rm -f requirements-dev.txt

%check
python3 setup.py test

%files
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 1:0.13.0-alt3
- Drop python2 support.

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.13.0-alt2
- drop excessive python3-module-jinja2-tests BR

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.13.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.13.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.4.1-alt1.git20150418.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.4.1-alt1.git20150418.1
- NMU: Use buildreq for BR.

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.4.1-alt1.git20150418
- Version 0.4.1

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2.1-alt1.git20150215
- Version 0.2.1

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.1-alt1.git20150108
- Version 0.0.1

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.a.git20141227
- Initial build for Sisyphus

