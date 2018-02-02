# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20150613.1.1.1.1
%define oname zope.contentprovider

%def_with python3

Name: python-module-%oname
Version: 4.0.1
#Release: alt1.dev0.git20150613.1.1
Summary: Content Provider Framework for Zope Templates
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.contentprovider/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-zope.event python-module-zope.location
#BuildPreReq: python-module-zope.publisher python-module-zope.schema
#BuildPreReq: python-module-zope.tales python-module-zope.browserpage
#BuildPreReq: python-module-zope.testing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-zope.event python3-module-zope.location
#BuildPreReq: python3-module-zope.publisher python3-module-zope.schema
#BuildPreReq: python3-module-zope.tales python3-module-zope.browserpage
#BuildPreReq: python3-module-zope.testing
%endif

%py_requires zope zope.component zope.event zope.interface zope.location
%py_requires zope.publisher zope.schema zope.tales

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-RestrictedPython python-module-persistent python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-transaction python-module-zope python-module-zope.browser python-module-zope.component python-module-zope.configuration python-module-zope.contenttype python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.i18n python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.location python-module-zope.pagetemplate python-module-zope.proxy python-module-zope.publisher python-module-zope.schema python-module-zope.security python-module-zope.tal python-module-zope.tales python-module-zope.traversing python-module-zope.untrustedpython python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python3 python3-base python3-module-pytz python3-module-setuptools python3-module-transaction python3-module-zope python3-module-zope.browser python3-module-zope.component python3-module-zope.configuration python3-module-zope.contenttype python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18n python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.location python3-module-zope.pagetemplate python3-module-zope.proxy python3-module-zope.publisher python3-module-zope.schema python3-module-zope.security python3-module-zope.tal python3-module-zope.tales python3-module-zope.traversing
BuildRequires: python-module-setuptools python-module-zope.browserpage python-module-zope.testing python3-module-pytest python3-module-zope.browserpage python3-module-zope.testing rpm-build-python3

%description
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

%package -n python3-module-%oname
Summary: Content Provider Framework for Zope Templates
Group: Development/Python3
%py3_requires zope zope.component zope.event zope.interface zope.location
%py3_requires zope.publisher zope.schema zope.tales

%description -n python3-module-%oname
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

%package -n python3-module-%oname-tests
Summary: Tests for zope.contentprovider
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.browserpage zope.testing

%description -n python3-module-%oname-tests
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

This package contains tests for zope.contentprovider.

%package tests
Summary: Tests for zope.contentprovider
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.browserpage zope.testing

%description tests
This package provides a framework to develop componentized Web GUI
applications. Instead of describing the content of a page using a single
template or static system of templates and METAL macros, content
provider objects are dynamically looked up based on the
setup/configuration of the application.

This package contains tests for zope.contentprovider.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.1-alt1.dev0.git20150613.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.dev0.git20150613.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.dev0.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt1.dev0.git20150613.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev0.git20150613
- Version 4.0.1.dev0
- Enabled check

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus

