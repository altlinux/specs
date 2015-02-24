%define mname ztfy
%define oname %mname.sendit
Name: python-module-%oname
Version: 0.1.16
Release: alt1
Summary: ZTFY application used to share files
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.sendit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-uuid
BuildPreReq: python-module-hurry.query
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formjs
BuildPreReq: python-module-z3c.jsonrpc
BuildPreReq: python-module-z3c.language.negotiator
BuildPreReq: python-module-z3c.language.switch
BuildPreReq: python-module-z3c.table
BuildPreReq: python-module-zc.catalog
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.content
BuildPreReq: python-module-zope.app.file
BuildPreReq: python-module-zope.app.publication
BuildPreReq: python-module-zope.authentication
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.catalog
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.componentvocabulary
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.pluggableauth
BuildPreReq: python-module-zope.processlifetime
BuildPreReq: python-module-zope.principalannotation
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.sendmail
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.appskin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-ztfy.security
BuildPreReq: python-module-ztfy.mail
BuildPreReq: python-module-ztfy.scheduler
BuildPreReq: python-module-ztfy.captcha
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-ztfy.file
BuildPreReq: python-module-ztfy.extfile
BuildPreReq: python-module-ztfy.base
BuildPreReq: python-module-ztfy.i18n
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname fanstatic hurry.query uuid z3c.form z3c.formjs
%py_requires z3c.jsonrpc z3c.language.negotiator z3c.language.switch
%py_requires z3c.table zc.catalog zope.annotation zope.app.content
%py_requires zope.app.file zope.app.publication zope.authentication
%py_requires zope.browserpage zope.catalog zope.component zope.container
%py_requires zope.componentvocabulary zope.dublincore zope.event
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.intid
%py_requires zope.lifecycleevent zope.location zope.pluggableauth
%py_requires zope.processlifetime zope.principalannotation zope.schema
%py_requires zope.publisher zope.security zope.sendmail zope.site
%py_requires zope.tales zope.traversing ztfy.skin ztfy.appskin ztfy.mail
%py_requires ztfy.utils ztfy.security ztfy.scheduler ztfy.captcha
%py_requires ztfy.jqueryui ztfy.file ztfy.extfile ztfy.base ztfy.i18n

%description
ztfy.sendit is a small package which provides an application which
authenticated users can use to send files to remote contacts, like in
SendIt web site.

It's main use case is for principals from inside an organization who
want to share documents with their remote contacts; contacts selection
can be done via any registered authentication plug-in.

You can customize your application so that external users registration
is opened or made only by organization's inner principals.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.sendit is a small package which provides an application which
authenticated users can use to send files to remote contacts, like in
SendIt web site.

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
* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.16-alt1
- Initial build for Sisyphus

