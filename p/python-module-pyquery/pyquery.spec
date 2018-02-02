%define oname pyquery

%def_with python3

Name: python-module-%oname
Version: 1.2.9
Release: alt1.1.1.1
Summary: A jquery-like library for python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyquery
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-cssselect
#BuildPreReq: python-module-webob python-module-lxml
#BuildPreReq: python-module-unittest2 python-module-restkit
#BuildPreReq: python-module-requests python-module-webtest
#BuildPreReq: python-module-nose python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-cssselect
#BuildPreReq: python3-module-webob python3-module-lxml
#BuildPreReq: python3-module-unittest2 python3-module-restkit
#BuildPreReq: python3-module-requests python3-module-webtest
#BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname
%py_requires lxml cssselect restkit webob requests

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: libgpg-error python-base python-devel python-module-BeautifulSoup4 python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-dns python-module-enum34 python-module-genshi python-module-greenlet python-module-html5lib python-module-http-parser python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-lxml python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-psycopg2 python-module-pyasn1 python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-socketpool python-module-sphinx python-module-sphinx_rtd_theme python-module-traceback2 python-module-urllib3 python-module-waitress python-module-webob python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-module-BeautifulSoup4 python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-dns python3-module-enum34 python3-module-genshi python3-module-greenlet python3-module-html5lib python3-module-http-parser python3-module-linecache2 python3-module-lxml python3-module-ndg-httpsclient python3-module-ntlm python3-module-psycopg2 python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-socketpool python3-module-traceback2 python3-module-urllib3 python3-module-waitress python3-module-webob xz
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-nose python-module-objects.inv python-module-requests python-module-restkit python-module-setuptools python-module-unittest2 python-module-webtest python3-module-coverage python3-module-nose python3-module-requests python3-module-restkit python3-module-setuptools python3-module-unittest2 python3-module-webtest rpm-build-python3 time

%description
pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. I just liked the jquery API and I missed it in python
so I told myself "Hey let's make jquery in python". This is the result.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. I just liked the jquery API and I missed it in python
so I told myself "Hey let's make jquery in python". This is the result.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. I just liked the jquery API and I missed it in python
so I told myself "Hey let's make jquery in python". This is the result.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: A jquery-like library for python
Group: Development/Python3
%py3_provides %oname
%py3_requires lxml cssselect restkit webob requests

%description -n python3-module-%oname
pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. I just liked the jquery API and I missed it in python
so I told myself "Hey let's make jquery in python". This is the result.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test -v
nosetests3 -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.9-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.9-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.9-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.9-alt1
- Version 1.2.9
- Enabled check

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.8-alt1
- Initial build for Sisyphus

