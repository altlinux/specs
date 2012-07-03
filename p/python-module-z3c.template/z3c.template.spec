%define oname z3c.template
Name: python-module-%oname
Version: 1.4.0
Release: alt1
Summary: A package implementing advanced Page Template patterns
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.template/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.configuration zope.interface
%py_requires zope.pagetemplate zope.publisher zope.schema z3c.ptcompat

%description
This package allows you to register templates independently from view
code.

In Zope 3, when registering a browser:page both presentation and
computation are registered together. Unfortunately the registration
tangles presentation and computation so tightly that it is not possible
to re-register a different template depending on context. (You can
override the whole registration but this is not the main point of this
package.)

With z3c.template the registration is split up between the view and the
template and allows to differentiate the template based on the skin
layer and the view.

In addition this package lays the foundation to differentiate between
templates that provide specific presentation templates and generic
layout templates.

%package tests
Summary: Tests for package implementing advanced Page Template patterns
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing lxml z3c.pt

%description tests
This package allows you to register templates independently from view
code.

In Zope 3, when registering a browser:page both presentation and
computation are registered together. Unfortunately the registration
tangles presentation and computation so tightly that it is not possible
to re-register a different template depending on context. (You can
override the whole registration but this is not the main point of this
package.)

With z3c.template the registration is split up between the view and the
template and allows to differentiate the template based on the skin
layer and the view.

In addition this package lays the foundation to differentiate between
templates that provide specific presentation templates and generic
layout templates.

This package contains tests for package implementing advanced Page
Template patterns.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

