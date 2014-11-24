%define oname grok

%def_with python3

Name: python-module-%oname
Version: 1.11.3
Release: alt3
Summary: A Smashing Web Framework
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grok/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-zope.interface
BuildPreReq: python-module-zope.component python-module-martian
BuildPreReq: python-module-grokcore.component-tests
BuildPreReq: python-module-grokcore.content
BuildPreReq: python-module-grokcore.security-tests
BuildPreReq: python-module-grokcore.view-tests
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-grokcore.viewlet-tests
BuildPreReq: python-module-grokcore.formlib-tests
BuildPreReq: python-module-grokcore.layout
BuildPreReq: python-module-grokcore.annotation-tests
BuildPreReq: python-module-grokcore.site-tests
BuildPreReq: python-module-zope.filerepresentation
BuildPreReq: python-module-grokcore.message
BuildPreReq: python-module-grokcore.catalog
BuildPreReq: python-module-grokcore.json python-module-grokcore.rest
BuildPreReq: python-module-grokcore.xmlrpc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zope.interface
BuildPreReq: python-tools-2to3
%endif

%py_requires grokcore.annotation grokcore.component grokcore.content
%py_requires grokcore.formlib grokcore.json grokcore.message
%py_requires grokcore.rest grokcore.security grokcore.site
%py_requires grokcore.traverser grokcore.view grokcore.viewlet
%py_requires grokcore.view grokcore.xmlrpc martian pytz simplejson
%py_requires z3c.autoinclude zc.catalog ZODB3 zope.annotation
%py_requires zope.app.appsetup zope.app.publication zope.app.wsgi
%py_requires zope.browserpage zope.catalog zope.component zope.container
%py_requires zope.contentprovider zope.errorview zope.event
%py_requires zope.exceptions zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.intid zope.keyreference zope.lifecycleevent
%py_requires zope.location zope.login zope.password
%py_requires zope.principalregistry zope.publisher zope.schema
%py_requires zope.security zope.securitypolicy zope.site zope.traversing
%py_requires grokcore.layout zope.filerepresentation grokcore.catalog
%py_requires grokcore.component.testing grokcore.security.testing
%py_requires grokcore.view.testing grokcore.viewlet.testing
%py_requires grokcore.formlib.testing grokcore.annotation.testing
%py_requires grokcore.site.testing grok.testing

%description
Grok is a smashing web framework based on Zope Toolkit technology.

Grok uses the Component Architecture and builds on Zope concepts like
content objects (models), views, and adapters. Its simplicity lies in
using convention over configuration and sensible defaults when wiring
components together. That means neither a configuration language like
ZCML nor a lot of repetition are needed to create a web application with
grok.

%package -n python3-module-%oname
Summary: A Smashing Web Framework
Group: Development/Python3
%py3_requires grokcore.annotation grokcore.component grokcore.content
%py3_requires grokcore.formlib grokcore.json grokcore.message
%py3_requires grokcore.rest grokcore.security grokcore.site
%py3_requires grokcore.traverser grokcore.view grokcore.viewlet
%py3_requires grokcore.view grokcore.xmlrpc martian pytz simplejson
%py3_requires z3c.autoinclude zc.catalog ZODB3 zope.annotation
%py3_requires zope.app.appsetup zope.app.publication zope.app.wsgi
%py3_requires zope.browserpage zope.catalog zope.component zope.container
%py3_requires zope.contentprovider zope.errorview zope.event
%py3_requires zope.exceptions zope.i18n zope.i18nmessageid zope.interface
%py3_requires zope.intid zope.keyreference zope.lifecycleevent
%py3_requires zope.location zope.login zope.password
%py3_requires zope.principalregistry zope.publisher zope.schema
%py3_requires zope.security zope.securitypolicy zope.site zope.traversing
%py3_requires grokcore.layout zope.filerepresentation grokcore.catalog
%py3_requires grokcore.component.testing grokcore.security.testing
%py3_requires grokcore.view.testing grokcore.viewlet.testing
%py3_requires grokcore.formlib.testing grokcore.annotation.testing
%py3_requires grokcore.site.testing grok.testing

%description -n python3-module-%oname
Grok is a smashing web framework based on Zope Toolkit technology.

Grok uses the Component Architecture and builds on Zope concepts like
content objects (models), views, and adapters. Its simplicity lies in
using convention over configuration and sensible defaults when wiring
components together. That means neither a configuration language like
ZCML nor a lot of repetition are needed to create a web application with
grok.

%package -n python3-module-%oname-tests
Summary: Tests for grok
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires grokcore.view.testing grokcore.viewlet.testing
%py3_requires grokcore.component.testing grokcore.security.testing
%py3_requires grokcore.formlib.testing grokcore.annotation.testing
%py3_requires grokcore.site.testing

%description -n python3-module-%oname-tests
Grok is a smashing web framework based on Zope Toolkit technology.

Grok uses the Component Architecture and builds on Zope concepts like
content objects (models), views, and adapters. Its simplicity lies in
using convention over configuration and sensible defaults when wiring
components together. That means neither a configuration language like
ZCML nor a lot of repetition are needed to create a web application with
grok.

This package contains tests for grok.

%package tests
Summary: Tests for grok
Group: Development/Python
Requires: %name = %version-%release
%py_requires grokcore.view.testing grokcore.viewlet.testing
%py_requires grokcore.component.testing grokcore.security.testing
%py_requires grokcore.formlib.testing grokcore.annotation.testing
%py_requires grokcore.site.testing

%description tests
Grok is a smashing web framework based on Zope Toolkit technology.

Grok uses the Component Architecture and builds on Zope concepts like
content objects (models), views, and adapters. Its simplicity lies in
using convention over configuration and sensible defaults when wiring
components together. That means neither a configuration language like
ZCML nor a lot of repetition are needed to create a web application with
grok.

This package contains tests for grok.

%package pickles
Summary: Pickles for grok
Group: Development/Python

%description pickles
Grok is a smashing web framework based on Zope Toolkit technology.

Grok uses the Component Architecture and builds on Zope concepts like
content objects (models), views, and adapters. Its simplicity lies in
using convention over configuration and sensible defaults when wiring
components together. That means neither a configuration language like
ZCML nor a lot of repetition are needed to create a web application with
grok.

This package contains pickles for grok.

%package docs
Summary: Documentation for grok
Group: Development/Documentation

%description docs
Grok is a smashing web framework based on Zope Toolkit technology.

Grok uses the Component Architecture and builds on Zope concepts like
content objects (models), views, and adapters. Its simplicity lies in
using convention over configuration and sensible defaults when wiring
components together. That means neither a configuration language like
ZCML nor a lot of repetition are needed to create a web application with
grok.

This package contains documentation for grok.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
%make pickle
%make html
popd

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*test*
%exclude %python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/*test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*test*
%exclude %python3_sitelibdir/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*test*
%python3_sitelibdir/*/*/*test*
%endif

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.3-alt3
- Added necessary requirements

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.3-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.3-alt1
- Version 1.11.3

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.3-alt1
- Version 1.10.3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1
- Version 1.9

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt2
- Added necessary requirements

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1
- Initial build for Sisyphus

