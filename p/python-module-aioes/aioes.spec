%define oname aioes

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: Elasticsearch integration with asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aioes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aioes.git
Source0: https://pypi.python.org/packages/4a/36/742ba7c8d7f52aa6a9cea2ab802054c33241f1389a2883630efbc02b9925/%{oname}-%{version}.tar.gz
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-aiohttp
#BuildPreReq: python-module-nose pyflakes python-tools-pep8
#BuildPreReq: python-module-elasticsearch
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-aiohttp
#BuildPreReq: python3-module-nose python3-pyflakes python3-tools-pep8
#BuildPreReq: python3-module-elasticsearch
%endif

%py_provides %oname
%py_requires asyncio aiohttp

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-django python3-module-dns python3-module-enum34 python3-module-greenlet python3-module-gunicorn python3-module-ndg-httpsclient python3-module-ntlm python3-module-paste python3-module-psycopg2 python3-module-pycares python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-yaml python3-module-zope python3-module-zope.interface
BuildRequires: python3-module-nose python3-module-urllib3 python3-pyflakes python3-tools-pep8 rpm-build-python3

%description
aioes is a asyncio compatible library for working with ElasticSearch.

%package -n python3-module-%oname
Summary: Elasticsearch integration with asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp

%description -n python3-module-%oname
aioes is a asyncio compatible library for working with ElasticSearch.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
pep8 .
pyflakes .
nosetests -s -v tests
python cmp.py
%endif
%if_with python3
pushd ../python3
python3 setup.py test
python3-pep8 .
python3-pyflakes .
nosetests3 -s -v tests
python3 cmp.py
popd
%endif

%if_with python2
%files
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20141228.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.git20141228.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141228
- Initial build for Sisyphus

