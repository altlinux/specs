%define oname autobahn

%def_with python3

Name: python-module-%oname
Version: 17.7.1
Release: alt1.1
Summary: WebSocket & WAMP for Python/Twisted
License: Apache License 2.0
Group: Development/Python
Url: https://github.com/tavendo/AutobahnPython

# https://github.com/tavendo/AutobahnPython.git
Source: %name-%version.tar

BuildRequires: inkscape
BuildRequires: python-module-alabaster python-module-boto python-module-html5lib python-module-msgpack python-module-objects.inv
BuildRequires: python-module-scour python-module-setuptools python-module-snappy python-module-sphinx-bootstrap-theme
BuildRequires: python-module-sphinxcontrib-spelling python-module-taschenmesser python-module-trollius python-module-twisted-logger
BuildRequires: python-module-twisted-web python-module-ujson python-module-wsaccel
BuildRequires: python-module-txaio-tests python-module-unittest2 python-module-mock python-module-trollius-tests
BuildRequires(pre): rpm-macros-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-cryptography python3-module-pygobject3 python3-module-serial python3-module-setuptools python3-module-snappy python3-module-zope
BuildRequires: python3-module-txaio-tests python3-module-unittest2 python3-module-mock python3-module-trollius-tests
BuildRequires: python3-module-pytest
%endif

%py_requires twisted.internet twisted.web twisted.words

%description
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

%package tests
Summary: Tests for Autobahn
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-twisted-core-test

%description tests
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

This package contains tests for Autobahn.

%package pickles
Summary: Pickles for Autobahn
Group: Development/Python

%description pickles
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

This package contains pickles for Autobahn.

%package docs
Summary: Documentation and examples for Autobahn
Group: Development/Documentation

%description docs
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

This package contains documentation and examples for Autobahn.

%if_with python3
%package -n python3-module-%oname
Summary: WebSocket & WAMP for Python3/Twisted
Group: Development/Python3
%py3_requires twisted.internet twisted.web twisted.words

%description -n python3-module-%oname
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

%package -n python3-module-%oname-tests
Summary: Tests for Autobahn
Group: Development/Python3
Requires: python3-module-%oname = %EVR
Requires: python3-module-twisted-core-test

%description -n python3-module-%oname-tests
Autobahn WebSockets for Python provides an implementation of the
WebSockets protocol which can be used to build WebSockets clients and
servers.

This package contains tests for Autobahn.
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
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

export PYTHONPATH=$PWD
pushd docs
make html pickle
popd

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

cp -fR docs/build/pickle \
	%buildroot%python_sitelibdir/%oname/

%check
PYTHONPATH=$(pwd) py.test --pyargs autobahn

%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) py.test3 --pyargs autobahn
popd
%endif

%files
%doc *.md *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test
#exclude %python_sitelibdir/twisted/plugins/__init__.py*

%files tests
%python_sitelibdir/*/*/test

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html examples

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test
#exclude %python3_sitelibdir/twisted/plugins/__init__.py

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 17.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 17.7.1-alt1
- Updated to upstream version 17.7.1.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.5-alt1.git20150111.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.5-alt1.git20150111.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.5-alt1.git20150111.1
- NMU: Use buildreq for BR.

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.git20150111
- Version 0.9.5

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3.3-alt1.git20141115
- Version 0.9.3-3

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20141110
- Version 0.9.3

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20141025
- Version 0.9.2
- Enabled testing

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.10-alt2.git20140710
- Moved tests into separate package

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.10-alt1.git20140710
- Version 0.8.10

* Tue Nov 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.git20131123
- Version 0.6.5

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20130826
- Version 0.6.2

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.14-alt2.git20130210
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.14-alt1.git20130210.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.14-alt1.git20130210
- Version 0.5.14

* Sat Sep 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.8-alt1.git20120920
- Version 0.5.8

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20120523
- Initial build for Sisyphus

