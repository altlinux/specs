%define oname grok
Name: python-module-%oname
Version: 1.10.3
Release: alt1
Summary: A Smashing Web Framework
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grok/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel python-module-zope.interface

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

%description
Grok is a smashing web framework based on Zope Toolkit technology.

Grok uses the Component Architecture and builds on Zope concepts like
content objects (models), views, and adapters. Its simplicity lies in
using convention over configuration and sensible defaults when wiring
components together. That means neither a configuration language like
ZCML nor a lot of repetition are needed to create a web application with
grok.

%package tests
Summary: Tests for grok
Group: Development/Python
Requires: %name = %version-%release

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

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%install
%python_install

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

%changelog
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

