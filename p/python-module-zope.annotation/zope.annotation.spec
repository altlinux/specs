# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20150613.1.1.1.1
%define oname zope.annotation

%def_with python3

Name: python-module-%oname
Version: 4.4.2
#Release: alt1.dev0.git20150613.1.1
Summary: Object annotation mechanism
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.annotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zope.location python-module-zope.proxy
#BuildPreReq: python-module-ZODB3 python-module-zope.testrunner
#BuildPreReq: python-module-zope.testing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-zope.location python3-module-zope.proxy
#BuildPreReq: python3-module-ZODB3 python3-module-zope.testrunner
#BuildPreReq: python3-module-zope.testing
%endif

%py_requires zope.interface zope.component zope.location zope.proxy
%py_requires ZODB3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-BTrees python-module-ZODB python-module-cffi python-module-cryptography python-module-enum34 python-module-extras python-module-linecache2 python-module-mimeparse python-module-numpy python-module-pbr python-module-persistent python-module-pyasn1 python-module-pytest python-module-serial python-module-setuptools python-module-six python-module-subunit python-module-testtools python-module-traceback2 python-module-transaction python-module-twisted-core python-module-unittest2 python-module-zc.lockfile python-module-zdaemon python-module-zodbpickle python-module-zope python-module-zope.component python-module-zope.configuration python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.proxy python-module-zope.schema python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-xml python3 python3-base python3-module-BTrees python3-module-ZODB python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-extras python3-module-genshi python3-module-linecache2 python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-persistent python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-subunit python3-module-testtools python3-module-traceback2 python3-module-transaction python3-module-unittest2 python3-module-zc.lockfile python3-module-zdaemon python3-module-zope python3-module-zope.component python3-module-zope.configuration python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.proxy python3-module-zope.schema python3-module-zope.testing
BuildRequires: python-module-ZEO python-module-setuptools python-module-zope.location python-module-zope.testrunner python3-module-ZEO python3-module-html5lib python3-module-setuptools python3-module-zope.location python3-module-zope.testrunner rpm-build-python3

%description
This package provides a mechanism to store additional information about
objects without need to modify object class.

%package -n python3-module-%oname
Summary: Object annotation mechanism
Group: Development/Python3
%py3_requires zope.interface zope.component zope.location zope.proxy
%py3_requires ZODB3

%description -n python3-module-%oname
This package provides a mechanism to store additional information about
objects without need to modify object class.

%package -n python3-module-%oname-tests
Summary: Tests for zope.annotation
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package provides a mechanism to store additional information about
objects without need to modify object class.

This package contains tests for zope.annotation.

%package tests
Summary: Tests for zope.annotation
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides a mechanism to store additional information about
objects without need to modify object class.

This package contains tests for zope.annotation.

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
%if_with python3
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.2-alt1.dev0.git20150613.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.2-alt1.dev0.git20150613.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.2-alt1.dev0.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.4.2-alt1.dev0.git20150613.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.2-alt1.dev0.git20150613
- Version 4.4.2.dev0
- Enabled check

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1
- Version 4.4.1

* Sat Dec 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1
- Version 4.3.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt3
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt2
- Avoid requirement on ZODB3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Version 4.2.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

