%define oname z3c.layout

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt3
Summary: HTML layout engine
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.layout/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

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

%package -n python3-module-%oname
Summary: HTML layout engine
Group: Development/Python3
%py3_requires zope.interface zope.schema zope.component
%py3_requires zope.app.publisher zope.contentprovider zope.viewlet
%py3_requires plone.memoize lxml

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for HTML layout engine
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing

%description -n python3-module-%oname-tests
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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

