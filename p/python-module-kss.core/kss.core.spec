%define mname kss
%define oname %mname.core
Name: python-module-%oname
Version: 1.6.5
Release: alt1
Summary: KSS (Kinetic Style Sheets) core framework
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/kss.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.browserresource
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.contenttype
BuildPreReq: python-module-zope.datetime
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.component-tests

%add_python_req_skip concatresource
%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zope.browserpage zope.browserresource zope.component
%py_requires zope.configuration zope.contenttype zope.datetime
%py_requires zope.event zope.interface zope.lifecycleevent zope.location
%py_requires zope.pagetemplate zope.publisher zope.schema zope.security
%py_requires zope.site zope.testing zope.traversing

%description
KSS is an Ajax framework that allows UI development without writing any
Javascript. It uses style sheets with CSS-compliant syntax to declare
and bind dynamic behaviors in the browser. The engine supports a set of
generic DOM-like commands; they are computed on the server and sent back
to manipulate the HTML page.

%package demos
Summary: Demos for %oname
Group: Development/Python
Requires: %name = %EVR

%description demos
KSS is an Ajax framework that allows UI development without writing any
Javascript. It uses style sheets with CSS-compliant syntax to declare
and bind dynamic behaviors in the browser. The engine supports a set of
generic DOM-like commands; they are computed on the server and sent back
to manipulate the HTML page.

This package contains demos for %oname.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing

%description tests
KSS is an Ajax framework that allows UI development without writing any
Javascript. It uses style sheets with CSS-compliant syntax to declare
and bind dynamic behaviors in the browser. The engine supports a set of
generic DOM-like commands; they are computed on the server and sent back
to manipulate the HTML page.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 kss/__init__.py \
	%buildroot%python_sitelibdir/kss/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/core/plugins/core/demo
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/*/tests*
%exclude %python_sitelibdir/%mname/*/*/*/test
%exclude %python_sitelibdir/%mname/*/*/*/*/*/testing
%exclude %python_sitelibdir/%mname/__init__.py*

%files demos
%python_sitelibdir/%mname/core/plugins/core/demo

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/tests*
%python_sitelibdir/%mname/*/*/*/test
%python_sitelibdir/%mname/*/*/*/*/*/testing

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt1
- Initial build for Sisyphus

