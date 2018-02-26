%define oname zc.sourcefactory
Name: python-module-%oname
Version: 0.7.0
Release: alt2.1
Summary: An easy way to create custom Zope 3 sources
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.sourcefactory/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc ZODB3 zope.intid zope.browser zope.component
%py_requires zope.dublincore zope.interface zope.proxy zope.publisher
%py_requires zope.schema

%description
Source factories are used to simplify the creation of sources for
certain standard cases.

Sources split up the process of providing input fields with choices for
users into several components: a context binder, a source class, a terms
class, and a term class.

This is the correct abstraction and will fit many complex cases very
well. To reduce the amount of work to do for some standard cases, the
source factories allow users to define only the business relevant code
for getting a list of values, getting a token and a title to display.

%package tests
Summary: Tests for zc.sourcefactory
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.app.testing zope.keyreference
%py_requires zope.app.zcmlfiles

%description tests
Source factories are used to simplify the creation of sources for
certain standard cases.

Sources split up the process of providing input fields with choices for
users into several components: a context binder, a source class, a terms
class, and a term class.

This is the correct abstraction and will fit many complex cases very
well. To reduce the amount of work to do for some standard cases, the
source factories allow users to define only the business relevant code
for getting a list of values, getting a token and a title to display.

This package contains tests for zc.sourcefactory.

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

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

