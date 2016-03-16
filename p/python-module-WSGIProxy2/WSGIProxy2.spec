%define oname WSGIProxy2

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 0.4.3
Release: alt1.dev0.git20141227.1.1
Summary: A WSGI Proxy with various http client backends
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/WSGIProxy2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gawel/WSGIProxy2.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-webob python-module-six
#BuildPreReq: python-module-restkit python-module-http-parser
#BuildPreReq: python-module-urllib3 python-module-requests
#BuildPreReq: python-module-webtest python-module-nose
#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-webob python3-module-six
#BuildPreReq: python3-module-restkit python3-module-http-parser
#BuildPreReq: python3-module-urllib3 python3-module-requests
#BuildPreReq: python3-module-webtest python3-module-nose
#BuildPreReq: python3-module-coverage
%endif

%py_provides wsgiproxy
Conflicts: python-module-wsgiproxy

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: libgpg-error python-base python-devel python-module-BeautifulSoup4 python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-dns python-module-enum34 python-module-genshi python-module-greenlet python-module-html5lib python-module-http-parser python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-psycopg2 python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-socketpool python-module-sphinx python-module-sphinx_rtd_theme python-module-urllib3 python-module-waitress python-module-webob python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-dns python3-module-enum34 python3-module-genshi python3-module-greenlet python3-module-html5lib python3-module-ndg-httpsclient python3-module-ntlm python3-module-psycopg2 python3-module-pycparser python3-module-setuptools python3-module-waitress
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-nose python-module-objects.inv python-module-pytest python-module-requests python-module-restkit python-module-webtest python3-module-chardet python3-module-coverage python3-module-nose python3-module-pytest python3-module-restkit python3-module-urllib3 python3-module-webtest rpm-build-python3 time

%description
A WSGI Proxy with various http client backends.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A WSGI Proxy with various http client backends.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A WSGI Proxy with various http client backends
Group: Development/Python3
%py3_provides wsgiproxy
Conflicts: python3-module-wsgiproxy

%description -n python3-module-%oname
A WSGI Proxy with various http client backends.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A WSGI Proxy with various http client backends.

This package contains tests for %oname.

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

export PYTHONPATH=$PWD
%make -C docs html

%check
nosetests -vv
#if_with python3
%if 0
pushd ../python3
nosetests3 -vv
popd
%endif

%files
%doc *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.3-alt1.dev0.git20141227.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1.dev0.git20141227.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.dev0.git20141227
- Version 0.4.3.dev0

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.dev0.git20131221
- Initial build for Sisyphus

