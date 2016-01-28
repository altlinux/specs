%define oname zope.ptresource

%def_with python3

Name: python-module-%oname
Version: 4.0.1
Release: alt1.dev0.git20150613.1
Summary: Page template resource plugin for zope.browserresource
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.ptresource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.ptresource.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zope.browserresource
#BuildPreReq: python-module-zope.pagetemplate
#BuildPreReq: python-module-zope.publisher python-module-zope.security
#BuildPreReq: python-module-zope.testing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zope.browserresource
#BuildPreReq: python3-module-zope.pagetemplate
#BuildPreReq: python3-module-zope.publisher python3-module-zope.security
#BuildPreReq: python3-module-zope.testing
%endif

%py_requires zope.browserresource zope.interface zope.pagetemplate
%py_requires zope.publisher zope.security

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-RestrictedPython python-module-persistent python-module-pluggy python-module-py python-module-pytz python-module-setuptools python-module-six python-module-transaction python-module-zope python-module-zope.browser python-module-zope.component python-module-zope.configuration python-module-zope.contenttype python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.i18n python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.location python-module-zope.proxy python-module-zope.publisher python-module-zope.schema python-module-zope.security python-module-zope.tal python-module-zope.tales python-module-zope.traversing python-module-zope.untrustedpython python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python3 python3-base python3-module-pytz python3-module-setuptools python3-module-transaction python3-module-zope python3-module-zope.browser python3-module-zope.component python3-module-zope.configuration python3-module-zope.contenttype python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18n python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.location python3-module-zope.proxy python3-module-zope.publisher python3-module-zope.schema python3-module-zope.security python3-module-zope.tal python3-module-zope.tales python3-module-zope.traversing
BuildRequires: python-module-pytest python-module-zope.browserresource python-module-zope.pagetemplate python-module-zope.testing python3-module-pytest python3-module-zope.browserresource python3-module-zope.pagetemplate python3-module-zope.testing rpm-build-python3 time

%description
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

%package -n python3-module-%oname
Summary: Page template resource plugin for zope.browserresource
Group: Development/Python3
%py3_requires zope.browserresource zope.interface zope.pagetemplate
%py3_requires zope.publisher zope.security

%description -n python3-module-%oname
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

%package -n python3-module-%oname-tests
Summary: Tests for zope.ptresource
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

This package contains tests for zope.ptresource.

%package tests
Summary: Tests for zope.ptresource
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package is at present not reusable without depending on a large
chunk of the Zope Toolkit and its assumptions. It is maintained by the
Zope Toolkit project.

This package provides a "page template" resource class, a resource which
content is processed with Zope Page Templates engine before returning to
client.

The resource factory class is registered for "pt", "zpt" and "html" file
extensions in package's configure.zcml file.

This package contains tests for zope.ptresource.

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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%check
py.test -vv src/zope/ptresource/tests.py
#if_with python3
%if 0
pushd ../python3
py.test-%_python3_version -vv src/zope/ptresource/tests.py
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
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt1.dev0.git20150613.1
- NMU: Use buildreq for BR.

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev0.git20150613
- Version 4.0.1.dev0
- Enabled check

* Sat Dec 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus

