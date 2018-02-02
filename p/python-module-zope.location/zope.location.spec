# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.dev0.git20150128.1.1.1.1
%define oname zope.location

%def_with python3

Name: python-module-%oname
Version: 4.0.4
#Release: alt2.dev0.git20150128.1.1
Summary: Zope Location
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.location/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.location.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-repoze.sphinx.autointerface
#BuildPreReq: python-module-zope.interface-tests
#BuildPreReq: python-module-zope.schema-tests
#BuildPreReq: python-module-zope.proxy-tests
#BuildPreReq: python-module-zope.configuration-tests
#BuildPreReq: python-module-zope.component-tests
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-zope.copy-tests
#BuildPreReq: python-module-%oname-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-zope.interface
#BuildPreReq: python3-module-zope.schema
#BuildPreReq: python3-module-zope.proxy
#BuildPreReq: python3-module-zope.configuration-tests
#BuildPreReq: python3-module-zope.component
#BuildPreReq: python3-module-nose
#BuildPreReq: python3-module-coverage
#BuildPreReq: python3-module-zope.copy-tests
#BuildPreReq: python3-module-%oname-tests
%endif

%py_requires zope zope.interface zope.schema zope.component zope.proxy
%py_requires zope.configuration

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-PyStemmer python-module-Pygments python-module-ZODB python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mimeparse python-module-numpy python-module-pbr python-module-persistent python-module-pyasn1 python-module-pytest python-module-pytz python-module-repoze python-module-repoze.sphinx python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-transaction python-module-twisted-core python-module-unittest2 python-module-zc.lockfile python-module-zdaemon python-module-zope python-module-zope.component python-module-zope.configuration python-module-zope.copy python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.location python-module-zope.proxy python-module-zope.schema python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools python3-module-zope python3-module-zope.component python3-module-zope.configuration python3-module-zope.copy python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.location python3-module-zope.proxy python3-module-zope.schema python3-module-zope.testing
BuildRequires: python-module-ZEO python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-repoze.sphinx.autointerface python-module-setuptools python-module-zope.location-tests python-module-zope.testrunner python3-module-coverage python3-module-nose python3-module-setuptools python3-module-zope.location-tests rpm-build-python3 time

%description
In Zope3, location are special objects that has a structural location.

%package -n python3-module-%oname
Summary: Zope Location
Group: Development/Python3
%py3_requires zope zope.interface zope.schema zope.component zope.proxy
%py3_requires zope.configuration

%description -n python3-module-%oname
In Zope3, location are special objects that has a structural location.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Location
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.configuration.tests zope.copy.tests

%description -n python3-module-%oname-tests
In Zope3, location are special objects that has a structural location.

This package contains tests for Zope Location.

%package tests
Summary: Tests for Zope Location
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.configuration.tests zope.copy.tests

%description tests
In Zope3, location are special objects that has a structural location.

This package contains tests for Zope Location.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt2.dev0.git20150128.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.dev0.git20150128.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.dev0.git20150128.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt2.dev0.git20150128.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2.dev0.git20150128
- New snapshot

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev.git20141027
- New snapshot

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev.git20140319
- Version 4.0.4dev

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1
- Version 3.9.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus

