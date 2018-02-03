%define oname aiohttp_jinja2

%def_without python2
%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.13.0
Release: alt1.1
Summary: jinja2 template renderer for aiohttp.web
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiohttp_jinja2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiohttp_jinja2.git
Source0: https://pypi.python.org/packages/79/fc/925fc60d87d38f0d6dcb7b538b7064b15b508d688a2fa6cf8e400c192308/aiohttp-jinja2-%{version}.tar.gz
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-asyncio python-module-aiohttp
#BuildPreReq: python-module-jinja2 python-module-nose
#BuildPreReq: python-module-ipdb python-module-coverage
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-asyncio python3-module-aiohttp
#BuildPreReq: python3-module-jinja2 python3-module-nose
#BuildPreReq: python3-module-ipdb python3-module-coverage
%endif

%py_provides %oname
%py_requires asyncio aiohttp jinja2

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: ipython3 python-base python3 python3-base python3-module-Pygments python3-module-asyncio python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-django python3-module-dns python3-module-docutils python3-module-enum34 python3-module-future python3-module-genshi python3-module-greenlet python3-module-gunicorn python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-markupsafe python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-paste python3-module-pexpect python3-module-psycopg2 python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: python3-module-aiohttp python3-module-coverage python3-module-html5lib python3-module-ipdb python3-module-jinja2-tests python3-module-nose python3-module-notebook python3-module-setuptools rpm-build-python3

%description
jinja2 template renderer for aiohttp.web.

%package -n python3-module-%oname
Summary: jinja2 template renderer for aiohttp.web
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp jinja2

%description -n python3-module-%oname
jinja2 template renderer for aiohttp.web.

%prep
%setup -q -n aiohttp-jinja2-%{version}

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

rm -f requirements-dev.txt

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
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

