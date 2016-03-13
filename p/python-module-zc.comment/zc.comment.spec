%define oname zc.comment

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt3.1
Summary: A simple package to support a list of comments for an object
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.comment/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.interface zope.component zope.schema
%py_requires zope.cachedescriptors zope.app.zapi zope.app.pagetemplate
%py_requires zope.annotation zope.lifecycleevent zope.i18nmessageid
%py_requires zope.event zope.publisher zope.security ZODB3 pytz

%description
The comment package is a simple way to add comments to any IAnnotatable
Zope content. The datetime and current principals are stamped on to the
comment. The comment body is currently simply unicode text but intended
to be html snippets ("rich text") at a later date.

The inclusion of current principals requires an interaction, which is
what we need to set up before we can use the system here.

%package -n python3-module-%oname
Summary: A simple package to support a list of comments for an object
Group: Development/Python3
%py3_requires zope.interface zope.component zope.schema
%py3_requires zope.cachedescriptors zope.app.zapi zope.app.pagetemplate
%py3_requires zope.annotation zope.lifecycleevent zope.i18nmessageid
%py3_requires zope.event zope.publisher zope.security ZODB3 pytz

%description -n python3-module-%oname
The comment package is a simple way to add comments to any IAnnotatable
Zope content. The datetime and current principals are stamped on to the
comment. The comment body is currently simply unicode text but intended
to be html snippets ("rich text") at a later date.

The inclusion of current principals requires an interaction, which is
what we need to set up before we can use the system here.

%package -n python3-module-%oname-tests
Summary: Tests for zc.comment
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.testbrowser
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The comment package is a simple way to add comments to any IAnnotatable
Zope content. The datetime and current principals are stamped on to the
comment. The comment body is currently simply unicode text but intended
to be html snippets ("rich text") at a later date.

This package contains tests for zc.comment.

%package tests
Summary: Tests for zc.comment
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.testbrowser
%py_requires zope.testing

%description tests
The comment package is a simple way to add comments to any IAnnotatable
Zope content. The datetime and current principals are stamped on to the
comment. The comment body is currently simply unicode text but intended
to be html snippets ("rich text") at a later date.

This package contains tests for zc.comment.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

