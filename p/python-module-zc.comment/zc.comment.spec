%define oname zc.comment
Name: python-module-%oname
Version: 0.1.0
Release: alt2.1
Summary: A simple package to support a list of comments for an object
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.comment/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

