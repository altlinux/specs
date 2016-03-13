%define oname z3c.template

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.a2.1
Summary: A package implementing advanced Page Template patterns
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.template/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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

%package -n python3-module-%oname
Summary: A package implementing advanced Page Template patterns
Group: Development/Python3
%py3_requires zope.component zope.configuration zope.interface
%py3_requires zope.pagetemplate zope.publisher zope.schema z3c.ptcompat

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for package implementing advanced Page Template patterns
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing lxml z3c.pt

%description -n python3-module-%oname-tests
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

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a2
- Version 2.0.0a2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

