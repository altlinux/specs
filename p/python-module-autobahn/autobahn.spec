%define oname autobahn

%def_with python3

Name: python-module-%oname
Version: 0.9.5
Release: alt1.git20150111.1.1
Summary: WebSocket & WAMP for Python/Twisted
License: Apache License 2.0
Group: Development/Python
Url: https://github.com/tavendo/AutobahnPython
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tavendo/AutobahnPython.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-trollius python-module-futures
#BuildPreReq: python-module-six python-module-zope.interface
#BuildPreReq: python-module-twisted-core-test python-module-twisted-web
#BuildPreReq: python-module-twisted-words python-module-wsaccel
#BuildPreReq: python-module-ujson python-module-snappy
#BuildPreReq: python-module-lz4 python-module-msgpack
#BuildPreReq: python-module-sphinx-devel scons python-module-boto
#BuildPreReq: python-module-taschenmesser python-module-scour
#BuildPreReq: python-module-sphinx-bootstrap-theme
#BuildPreReq: python-module-sphinxcontrib-spelling libenchant
#BuildPreReq: inkscape
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-Fabric python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-ecdsa python-module-enchant python-module-enum34 python-module-futures python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-pyasn1 python-module-pycrypto python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-sphinxcontrib python-module-twisted-core python-module-yaml python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-cffi python3-module-enum34 python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-zope.interface scons
BuildRequires: inkscape python-module-alabaster python-module-boto python-module-html5lib python-module-msgpack python-module-objects.inv python-module-scour python-module-setuptools-tests python-module-snappy python-module-sphinx-bootstrap-theme python-module-sphinxcontrib-spelling python-module-taschenmesser python-module-trollius python-module-twisted-logger python-module-twisted-web python-module-ujson python-module-wsaccel python3-module-cryptography python3-module-pygobject3 python3-module-serial python3-module-setuptools-tests python3-module-snappy python3-module-zope rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3 python3-module-asyncio
#BuildPreReq: python3-module-six python3-module-zope.interface
#BuildPreReq: python3-module-twisted-core-test python3-module-twisted-web
#BuildPreReq: python3-module-twisted-words python3-module-wsaccel
#BuildPreReq: python3-module-ujson python3-module-snappy
#BuildPreReq: python3-module-lz4 python3-module-msgpack
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
ln -s ../objects.inv doc/

%build
pushd %oname
%python_build_debug
popd

%if_with python3
pushd ../python3/%oname
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build_debug
popd
%endif

export PYTHONPATH=$PWD
pushd doc
sphinx-build -b pickle -d build/doctrees . build/pickle
scons
popd
mv doc/_build html

%install
pushd %oname
%python_install
popd

%if_with python3
pushd ../python3/%oname
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

cp -fR doc/build/pickle \
	%buildroot%python_sitelibdir/%oname/

%check
pushd %oname
python setup.py test
popd
%if_with python3
pushd ../python3/%oname
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test
#exclude %python_sitelibdir/twisted/plugins/__init__.py*

%files tests
%python_sitelibdir/*/*/test

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc html examples

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test
#exclude %python3_sitelibdir/twisted/plugins/__init__.py

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test
%endif

%changelog
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

