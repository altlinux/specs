%define oname sqltap

%def_with python3

Name: python-module-%oname
Version: 0.3.6
Release: alt1.git20150127.1.1
Summary: Profiling and introspection for applications using sqlalchemy
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/sqltap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/inconshreveable/sqltap.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-SQLAlchemy python-module-mako
#BuildPreReq: python-module-nose python-modules-sqlite3
#BuildPreReq: python-module-werkzeug
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-SQLAlchemy python3-module-mako
#BuildPreReq: python3-module-nose python3-modules-sqlite3
#BuildPreReq: python3-module-werkzeug
%endif

%py_provides %oname
%py_requires sqlalchemy mako werkzeug

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-beaker python-module-cssselect python-module-ecdsa python-module-ed25519 python-module-genshi python-module-jinja2 python-module-lingua python-module-nss python-module-polib python-module-pycrypto python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-beaker python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-lingua python3-module-polib python3-module-pycrypto python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-zope python3-module-zope.interface
BuildRequires: python-module-docutils python-module-html5lib python-module-mako python-module-nose python-module-setuptools-tests python3-module-html5lib python3-module-mako python3-module-nose python3-module-setuptools-tests python3-module-sphinx rpm-build-python3

%description
sqltap is a library that allows you to profile and introspect the
queries that your application makes using SQLAlchemy.

sqltap helps you quickly understand:

* how many times a sql query is executed
* how much time your sql queries take
* where your application is issuing sql queries from

%package -n python3-module-%oname
Summary: Profiling and introspection for applications using sqlalchemy
Group: Development/Python3
%py3_provides %oname
%py3_requires sqlalchemy mako werkzeug

%description -n python3-module-%oname
sqltap is a library that allows you to profile and introspect the
queries that your application makes using SQLAlchemy.

sqltap helps you quickly understand:

* how many times a sql query is executed
* how much time your sql queries take
* where your application is issuing sql queries from

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md doc/source/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md doc/source/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt1.git20150127.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt1.git20150127.1
- NMU: Use buildreq for BR.

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20150127
- Version 0.3.6

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20141222
- Initial build for Sisyphus

