# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1.1.1
%define oname zope.pagetemplate

%def_with python3

Name: python-module-%oname
Version: 4.2.1
#Release: alt1.1.1
Summary: Zope Page Templates
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.pagetemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zope.component python-module-zope.security
#BuildPreReq: python-module-zope.tales python-module-zope.proxy
#BuildPreReq: python-module-zope.untrustedpython
#BuildPreReq: python-module-zope.i18n python-module-zope.i18nmessageid
#BuildPreReq: python-module-zope.traversing python-module-zope.testing
#BuildPreReq: python-module-zope.component-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-zope.component python3-module-zope.security
#BuildPreReq: python3-module-zope.tales python3-module-zope.proxy
#BuildPreReq: python3-module-zope.i18n python3-module-zope.i18nmessageid
#BuildPreReq: python3-module-zope.traversing python3-module-zope.testing
#BuildPreReq: python3-module-zope.component-tests
%endif

%py_requires zope zope.interface zope.component zope.security zope.tales
%py_requires zope.tal zope.i18n zope.i18nmessageid zope.traversing
%py_requires zope.untrustedpython

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-RestrictedPython python-module-ZEO python-module-ZODB python-module-cffi python-module-cryptography python-module-enum34 python-module-mimeparse python-module-numpy python-module-pbr python-module-persistent python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-transaction python-module-twisted-core python-module-unittest2 python-module-zc.lockfile python-module-zdaemon python-module-zope python-module-zope.browser python-module-zope.component python-module-zope.configuration python-module-zope.contenttype python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.i18n python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.location python-module-zope.proxy python-module-zope.publisher python-module-zope.schema python-module-zope.security python-module-zope.tal python-module-zope.testing python-module-zope.testrunner python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytz python3-module-setuptools python3-module-transaction python3-module-unittest2 python3-module-zope python3-module-zope.browser python3-module-zope.component python3-module-zope.configuration python3-module-zope.contenttype python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18n python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.location python3-module-zope.proxy python3-module-zope.publisher python3-module-zope.schema python3-module-zope.security python3-module-zope.tal python3-module-zope.testing
BuildRequires: python-module-setuptools python-module-zope.component-tests python-module-zope.tales python-module-zope.traversing python-module-zope.untrustedpython python3-module-html5lib python3-module-pytest python3-module-zope.tales python3-module-zope.testrunner python3-module-zope.traversing rpm-build-python3

%description
Page Templates provide an elegant templating mechanism that achieves a
clean separation of presentation and application logic while allowing
for designers to work with templates in their visual editing tools
(FrontPage, Dreamweaver, GoLive, etc.).

%package -n python3-module-%oname
Summary: Zope Page Templates
Group: Development/Python3
%py3_requires zope zope.interface zope.component zope.security zope.tales
%py3_requires zope.tal zope.i18n zope.i18nmessageid zope.traversing

%description -n python3-module-%oname
Page Templates provide an elegant templating mechanism that achieves a
clean separation of presentation and application logic while allowing
for designers to work with templates in their visual editing tools
(FrontPage, Dreamweaver, GoLive, etc.).

%package -n python3-module-%oname-tests
Summary: Tests for Page Templates
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.proxy zope.security

%description -n python3-module-%oname-tests
Page Templates provide an elegant templating mechanism that achieves a
clean separation of presentation and application logic while allowing
for designers to work with templates in their visual editing tools
(FrontPage, Dreamweaver, GoLive, etc.).

This package contains tests for Page Templates.

%package tests
Summary: Tests for Page Templates
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.proxy zope.security

%description tests
Page Templates provide an elegant templating mechanism that achieves a
clean separation of presentation and application logic while allowing
for designers to work with templates in their visual editing tools
(FrontPage, Dreamweaver, GoLive, etc.).

This package contains tests for Page Templates.

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
python setup.py test -v
#if_with python3
%if 0
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.1-alt1.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.2.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1
- Enabled check

* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2
- Added necessary requirements

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

