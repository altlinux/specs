%define oname z3c.layout
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: HTML layout engine
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.layout/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface zope.schema zope.component
%py_requires zope.app.publisher zope.contentprovider zope.viewlet
%py_requires plone.memoize lxml

%description
This package implements a page rendering model based on a static HTML
document that is made dynamic from the outside by mapping content
provider definitions to locations in the HTML document tree. This is
called a "layout".

The component architecture is utilized to provide extension points that
allow wide application. Two-phase rendering is supported using the
zope.contentprovider rendering scheme (update/render).

Static resources, as referenced by the HTML document (images,
stylesheets and javascript files) are included carbon copy and published
as browser resources (see zope.app.publisher.browser).

%package tests
Summary: Tests for HTML layout engine
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package implements a page rendering model based on a static HTML
document that is made dynamic from the outside by mapping content
provider definitions to locations in the HTML document tree. This is
called a "layout".

The component architecture is utilized to provide extension points that
allow wide application. Two-phase rendering is supported using the
zope.contentprovider rendering scheme (update/render).

Static resources, as referenced by the HTML document (images,
stylesheets and javascript files) are included carbon copy and published
as browser resources (see zope.app.publisher.browser).

This package contains tests for HTML layout engine.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

