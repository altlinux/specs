%define oname zope.security

%def_with python3

Name: python-module-%oname
Version: 4.0.4
Release: alt1.dev0.git20150602.1.1
Summary: Zope Security Framework
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.security/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.security.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zope.proxy
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-repoze.sphinx.autointerface
#BuildPreReq: python-module-zope.i18nmessageid
#BuildPreReq: python-module-zope.schema python-module-zope.location
#BuildPreReq: python-module-zope.configuration
#BuildPreReq: python-module-zope.testing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-zope.proxy
%endif

Requires: python-module-zope.i18nmessageid
%py_requires zope.component zope.interface zope.location zope.proxy
%py_requires zope.schema zope.configuration

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-persistent python-module-pytz python-module-repoze python-module-repoze.sphinx python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope python-module-zope.component python-module-zope.configuration python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.proxy python-module-zope.schema python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-zope python3-module-zope.interface
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-repoze.sphinx.autointerface python-module-zope.location python-module-zope.testing python3-devel python3-module-setuptools python3-module-zope.proxy rpm-build-python3 time

%description
The Security framework provides a generic mechanism to implement
security policies on Python objects.

%package -n python3-module-%oname
Summary: Zope Security Framework
Group: Development/Python3
Requires: python3-module-zope.i18nmessageid
%py3_requires zope.component zope.interface zope.location zope.proxy
%py3_requires zope.schema zope.configuration

%description -n python3-module-%oname
The Security framework provides a generic mechanism to implement
security policies on Python objects.

%package -n python3-module-%oname-examples
Summary: Examples for Zope Security Framework
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-examples
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains examples for Zope Security Framework.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Security Framework
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains tests for Zope Security Framework.

%package pickles
Summary: Pickles for Zope Security Framework
Group: Development/Python

%description pickles
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains pickles for Zope Security Framework.

%package docs
Summary: Documentation for Zope Security Framework
Group: Development/Documentation
BuildArch: noarch

%description docs
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains documentation for Zope Security Framework.

%package tests
Summary: Tests for Zope Security Framework
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains tests for Zope Security Framework.

%package examples
Summary: Examples for Zope Security Framework
Group: Development/Python
Requires: %name = %version-%release

%description examples
The Security framework provides a generic mechanism to implement
security policies on Python objects.

This package contains examples for Zope Security Framework.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
touch src/zope/security/examples/__init__.py
cp -fR src/zope/security/examples \
	%buildroot%python_sitelibdir/zope/security/
install -p -m644 src/zope/security/*.zcml \
	%buildroot%python_sitelibdir/zope/security/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 src/zope/security/*.zcml \
	%buildroot%python3_sitelibdir/zope/security/
popd
%endif

export PYTHONPATH=$PWD/src
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/examples
%dir %python_sitelibdir/%oname
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/*/test*

%files examples
%python_sitelibdir/*/*/examples

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/*/examples
%endif

%changelog
* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150602.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150602.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150602
- Version 4.0.4.dev0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2.dev.git20140319
- Python 3: moved examples into separate package

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.dev.git20140319
- Version 4.0.2dev
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git20130709
- Version 4.0.1dev

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3.b2.dev0.git20130327
- Version 4.0.0b2.dev0

* Thu Jan 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.bzr20120517
- Added necessary .zcml files (ALT #28301)

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.bzr20120517
- Version 4.0.0dev

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.3-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1
- Version 3.8.3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus

