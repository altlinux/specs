%define oname webtest

%def_with python3

Name: python-module-%oname
Version: 2.0.19
Release: alt1.dev0.git20150724.1
Summary: Helper to test WSGI applications
License: MIT
Group: Development/Python
Url: http://webtest.pythonpaste.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/Pylons/webtest.git
Source: WebTest-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-Pygments
#BuildPreReq: python-module-BeautifulSoup4 python-module-webob
#BuildPreReq: python-module-waitress
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: libgpg-error python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-html5lib python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-BeautifulSoup4 python-module-alabaster python-module-docutils python-module-objects.inv python-module-waitress python-module-webob python3-module-html5lib python3-module-sphinx rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python3-module-sphinx python3-module-Pygments
%endif

%description
This wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

This provides convenient full-stack testing of applications written
with any WSGI-compatible framework.

This is based on ``paste.fixture.TestApp``.

%package pickles
Summary: Pickles for WebTest
Group: Development/Python

%description pickles
This wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

This provides convenient full-stack testing of applications written
with any WSGI-compatible framework.

This is based on ``paste.fixture.TestApp``.

This package contains pickles for WebTest.

%if_with python3
%package -n python3-module-%oname
Summary: Helper to test WSGI applications (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

This provides convenient full-stack testing of applications written
with any WSGI-compatible framework.

This is based on ``paste.fixture.TestApp``.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

# for docs
export PYTHONPATH=%buildroot%python_sitelibdir
make -C docs pickle SPHINXBUILD=sphinx-build
make -C docs html SPHINXBUILD=sphinx-build

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc docs/_build/html/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.19-alt1.dev0.git20150724.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.19-alt1.dev0.git20150724
- New snapshot

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.19-alt1.dev0.git20150208
- Version 2.0.19.dev0

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.16-alt1.dev0.git20140629
- Version 2.0.16.dev0

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.11-alt1.dev0.git20131122
- Version 2.0.11.dev0

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 2.0-alt1
- Version 2.0

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.hg20120506
- Version 1.3.4
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.hg20111208
- Version 1.3.3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt2.hg20110422.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2.hg20110422
- New snapshot

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2.hg20101112
- Version 1.2.3

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2.hg20100723
- New snapshot (svn -> hg)

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20090922.1
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20090922
- Initial build for Sisyphus
