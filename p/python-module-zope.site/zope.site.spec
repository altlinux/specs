# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.dev0.git20150608.1.1.1.1
%define oname zope.site

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 4.0.1
#Release: alt2.dev0.git20150608.1.1
Summary: Local registries for zope component architecture
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.site/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-%oname-tests
#BuildPreReq: python-module-zope.annotation python-module-zope.container-tests
#BuildPreReq: python-module-zope.security python-module-zope.event
#BuildPreReq: python-module-zope.lifecycleevent python-module-zope.location
#BuildPreReq: python-module-zope.testing python-module-zope.traversing-tests
#BuildPreReq: python-module-zope.component-tests
#BuildPreReq: python-module-zope.size
#BuildPreReq: python-module-ZODB-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-%oname-tests
#BuildPreReq: python3-module-zope.annotation python3-module-zope.container-tests
#BuildPreReq: python3-module-zope.security python3-module-zope.event
#BuildPreReq: python3-module-zope.lifecycleevent python3-module-zope.location
#BuildPreReq: python3-module-zope.testing python3-module-zope.traversing-tests
#BuildPreReq: python3-module-zope.component-tests
#BuildPreReq: python3-module-zope.size python3-module-zodbpickle
#BuildPreReq: python3-module-ZODB-tests
#BuildPreReq: python3-module-zope.filerepresentation
%endif

%py_requires zope.annotation zope.container zope.security
%py_requires zope.component zope.event zope.interface
%py_requires zope.lifecycleevent zope.location

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-ZEO python-module-ZODB python-module-cffi python-module-cryptography python-module-enum34 python-module-extras python-module-linecache2 python-module-mimeparse python-module-numpy python-module-pbr python-module-persistent python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-subunit python-module-testtools python-module-traceback2 python-module-transaction python-module-twisted-core python-module-unittest2 python-module-zc python-module-zc.lockfile python-module-zdaemon python-module-zodbpickle python-module-zope python-module-zope.annotation python-module-zope.browser python-module-zope.browserpage python-module-zope.component python-module-zope.configuration python-module-zope.container python-module-zope.contenttype python-module-zope.dottedname python-module-zope.event python-module-zope.exceptions python-module-zope.filerepresentation python-module-zope.hookable python-module-zope.i18n python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.lifecycleevent python-module-zope.location python-module-zope.pagetemplate python-module-zope.proxy python-module-zope.publisher python-module-zope.schema python-module-zope.security python-module-zope.site python-module-zope.size python-module-zope.tal python-module-zope.tales python-module-zope.testing python-module-zope.testrunner python-module-zope.traversing python-module-zope.untrustedpython python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-xml python3 python3-base python3-module-BTrees python3-module-ZEO python3-module-ZODB python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-persistent python3-module-pip python3-module-pycparser python3-module-pytz python3-module-setuptools python3-module-transaction python3-module-unittest2 python3-module-zc.lockfile python3-module-zdaemon python3-module-zope python3-module-zope.annotation python3-module-zope.browser python3-module-zope.component python3-module-zope.configuration python3-module-zope.container python3-module-zope.contenttype python3-module-zope.dottedname python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18n python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.lifecycleevent python3-module-zope.location python3-module-zope.proxy python3-module-zope.publisher python3-module-zope.schema python3-module-zope.security python3-module-zope.tal python3-module-zope.tales python3-module-zope.testing python3-module-zope.traversing
BuildRequires: python-module-ZODB-tests python-module-setuptools python-module-zope.component-tests python-module-zope.container-tests python-module-zope.site-tests python-module-zope.traversing-tests python3-module-html5lib python3-module-pytest python3-module-zope.filerepresentation python3-module-zope.pagetemplate python3-module-zope.site python3-module-zope.size python3-module-zope.testrunner rpm-build-python3

%description
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

%package -n python3-module-%oname
Summary: Local registries for zope component architecture
Group: Development/Python3
%py3_requires zope.annotation zope.container zope.security
%py3_requires zope.component zope.event zope.interface
%py3_requires zope.lifecycleevent zope.location

%description -n python3-module-%oname
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

%package -n python3-module-%oname-tests
Summary: Tests for zope.site
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.configuration zope.testing

%description -n python3-module-%oname-tests
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

This package contains tests for zope.site.

%package tests
Summary: Tests for zope.site
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.configuration zope.testing

%description tests
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

This package contains tests for zope.site.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
export PYTHONPATH=$PWD/src
python setup.py test -v
#if_with python3
%if 0
pushd ../python3
export PYTHONPATH=$PWD/src
python3 setup.py test -v
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.1-alt2.dev0.git20150608.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt2.dev0.git20150608.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt2.dev0.git20150608.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt2.dev0.git20150608.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2.dev0.git20150608
- Enabled check

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev0.git20150608
- Version 4.0.1.dev0

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.2-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt1
- Initial build for Sisyphus

