%define mname ztfy
%define oname %mname.blog
Name: python-module-%oname
Version: 0.6.2
Release: alt1
Summary: ZTFY blog handling package
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.blog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-Pygments
BuildPreReq: python-module-pytz python-module-transaction
BuildPreReq: python-module-hurry.query
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formui
BuildPreReq: python-module-z3c.formjs
BuildPreReq: python-module-z3c.json
BuildPreReq: python-module-z3c.jsonrpc
BuildPreReq: python-module-z3c.language.negotiator
BuildPreReq: python-module-z3c.language.switch
BuildPreReq: python-module-z3c.menu.simple
BuildPreReq: python-module-z3c.table
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-z3c.viewlet
BuildPreReq: python-module-z3c.zrtresource
BuildPreReq: python-module-zc.catalog
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.content
BuildPreReq: python-module-zope.app.publication
BuildPreReq: python-module-zope.authentication
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.catalog
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.copypastemove
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.pluggableauth
BuildPreReq: python-module-zope.processlifetime
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zopyx.txng3.core
BuildPreReq: python-module-zopyx.txng3.ext
BuildPreReq: python-module-ztfy.base
BuildPreReq: python-module-ztfy.extfile
BuildPreReq: python-module-ztfy.file
BuildPreReq: python-module-ztfy.i18n
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-ztfy.security
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-ztfy.workflow
BuildPreReq: python-module-ztfy.comment
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner

%py_provides %oname
%py_requires %mname fanstatic hurry.query pygments pytz transaction
%py_requires z3c.form z3c.formui z3c.formjs z3c.json z3c.jsonrpc
%py_requires z3c.language.negotiator z3c.language.switch z3c.menu.simple
%py_requires z3c.table z3c.template z3c.viewlet z3c.zrtresource
%py_requires zc.catalog zope.annotation zope.app.content zope.catalog
%py_requires zope.app.publication zope.authentication zope.browserpage
%py_requires zope.component zope.container zope.copypastemove zope.i18n
%py_requires zope.dublincore zope.i18nmessageid zope.interface zope.site
%py_requires zope.intid zope.location zope.pluggableauth zope.schema
%py_requires zope.processlifetime zope.tales zope.traversing ztfy.base
%py_requires zope.viewlet zopyx.txng3.core zopyx.txng3.ext ztfy.extfile
%py_requires ztfy.file ztfy.i18n ztfy.jqueryui ztfy.security ztfy.skin
%py_requires ztfy.utils ztfy.workflow ztfy.comment

%description
ztfy.blog is a set of modules which allows easy management of a simple
web site based on Zope3 application server.

It's main goal is to be simple to use and manage.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.testrunner

%description tests
ztfy.blog is a set of modules which allows easy management of a simple
web site based on Zope3 application server.

It's main goal is to be simple to use and manage.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
rm -fR build
py.test -vv

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus

